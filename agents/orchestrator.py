import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv

# Import tools
from tools.sanctions_checker import check_sanctions
from tools.risk_scorer import calculate_risk_score
from utils.cache import get_cache_key, load_from_cache, save_to_cache

load_dotenv()

class ComplianceOrchestrator:
    def __init__(self, model_name="claude-3-5-sonnet-20240620", use_cache=True):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model_name = model_name
        self.use_cache = use_cache
        
    def run_screening(self, name: str, country: str, amount: float) -> dict:
        """
        Main entry point for transaction screening.
        """
        # 1. Check Cache first (Save money!)
        if self.use_cache:
            cache_key = get_cache_key({"name": name, "country": country, "amount": amount})
            cached_result = load_from_cache(cache_key)
            if cached_result:
                cached_result["from_cache"] = True
                return cached_result
        
        # 2. Run Deterministic Tools First
        sanctions_result = check_sanctions(name)
        
        # 3. Prepare LLM Prompt
        system_prompt = """
        You are an AML Compliance Officer. 
        Analyze the tool outputs and provide a final recommendation.
        Return ONLY valid JSON.
        """
        
        user_prompt = f"""
        Transaction Details:
        - Name: {name}
        - Country: {country}
        - Amount: ${amount}
        
        Tool Output (Sanctions): {json.dumps(sanctions_result)}
        
        Based on this, determine risk and recommendation.
        """
        
        # 4. Call LLM
        try:
            response = self.client.messages.create(
                model=self.model_name,
                max_tokens=1000,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}]
            )
            
            # 5. Parse LLM Response
            llm_text = response.content[0].text
            # Clean markdown code blocks if present
            llm_text = llm_text.replace("```json", "").replace("```", "").strip()
            llm_json = json.loads(llm_text)
            
            # 6. Combine with Tool Data
            final_result = {
                "name": name,
                "country": country,
                "amount": amount,
                "sanctions_match": sanctions_result["is_sanctioned"],
                "llm_analysis": llm_json,
                "from_cache": False,
                "timestamp": str(datetime.now())
            }
            
            # 7. Save to Cache
            if self.use_cache:
                save_to_cache(cache_key, final_result)
            
            return final_result
            
        except Exception as e:
            return {"error": str(e), "from_cache": False}

# For testing directly
if __name__ == "__main__":
    agent = ComplianceOrchestrator()
    result = agent.run_screening("Ivan Petrov", "RU", 50000)
    print(json.dumps(result, indent=2))
