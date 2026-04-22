import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class Config(BaseModel):
    # API Keys
    anthropic_api_key: str = Field(default_factory=lambda: os.getenv("ANTHROPIC_API_KEY"))
    
    # Endpoints
    sanctions_api_url: str = Field(default_factory=lambda: os.getenv("SANCTIONS_API_URL"))
    pep_registry_url: str = Field(default_factory=lambda: os.getenv("PEP_REGISTRY_URL"))
    
    # Risk Thresholds
    risk_threshold_high: float = Field(default=0.75)
    risk_threshold_medium: float = Field(default=0.45)
    
    # Model Settings
    # Note: Using stable 3.5 Sonnet as recommended
    model_name: str = "claude-3-5-sonnet-20240620" 
    max_tokens: int = 4096
    temperature: float = 0.0  # Keep temperature low for compliance determinism
    
    # Paths
    prompt_path: str = "prompts/system_prompt.txt"
    log_path: str = "logs/audit_trail.json"

    class Config:
        arbitrary_types_allowed = True

# Initialize global config
settings = Config()
