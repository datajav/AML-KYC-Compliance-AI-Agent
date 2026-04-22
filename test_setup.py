"""
test_setup.py
Verifies all API connections and configurations before running the agent.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_env_variables():
    """Check if required environment variables are set."""
    print("🔍 Checking Environment Variables...")
    print("=" * 50)
    
    required_vars = {
        "ANTHROPIC_API_KEY": "Anthropic API Key",
        "SANCTIONS_API_URL": "Sanctions API URL",
    }
    
    all_present = True
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value and len(value) > 10:
            print(f"✅ {description}: Found")
        else:
            print(f"❌ {description}: Missing or invalid")
            all_present = False
    
    print("=" * 50)
    return all_present

def test_anthropic_connection():
    """Test connection to Anthropic API."""
    print("\n🔍 Testing Anthropic API Connection...")
    print("=" * 50)
    
    try:
        from anthropic import Anthropic
        
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("❌ Anthropic API Key not found")
            return False
        
        client = Anthropic(api_key=api_key)
        
        # Simple test message
        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=50,
            messages=[{"role": "user", "content": "Say 'Connection OK'"}]
        )
        
        print(f"✅ Anthropic API: Connected")
        print(f"   Model: claude-3-5-sonnet-20240620")
        print(f"   Response: {response.content[0].text}")
        print("=" * 50)
        return True
        
    except ImportError:
        print("❌ Anthropic SDK not installed. Run: pip install anthropic")
        return False
    except Exception as e:
        print(f"❌ Anthropic API Error: {str(e)}")
        return False

def test_local_data_files():
    """Check if local mock data files exist."""
    print("\n🔍 Checking Local Data Files...")
    print("=" * 50)
    
    files_to_check = [
        "data/sanctions_list.json",
        "data/pep_registry.json",
        "data/synthetic/transactions.json",
    ]
    
    all_exist = True
    for file_path in files_to_check:
        if os.path.exists(file_path):
            print(f"✅ {file_path}: Found")
        else:
            print(f"⚠️  {file_path}: Not found (will use mock data)")
            all_exist = False
    
    print("=" * 50)
    return all_exist

def test_config_loading():
    """Test if config.py loads correctly."""
    print("\n🔍 Testing Configuration Loading...")
    print("=" * 50)
    
    try:
        from config import settings
        print(f"✅ Config loaded successfully")
        print(f"   Model: {settings.model_name}")
        print(f"   Risk Threshold (High): {settings.risk_threshold_high}")
        print("=" * 50)
        return True
    except Exception as e:
        print(f"❌ Config Error: {str(e)}")
        return False

def main():
    """Run all setup tests."""
    print("\n" + "=" * 50)
    print("🚀 AML/KYC Compliance Agent - Setup Verification")
    print("=" * 50 + "\n")
    
    results = {
        "Environment": check_env_variables(),
        "Anthropic API": test_anthropic_connection(),
        "Local Data": test_local_data_files(),
        "Config": test_config_loading(),
    }
    
    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)
    
    for test, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test}: {status}")
    
    print("=" * 50)
    
    if all(results.values()):
        print("\n🎉 All tests passed! Ready to run the agent.")
        print("\nNext steps:")
        print("  1. Run: python app.py  (Streamlit UI)")
        print("  2. Run: python agents/orchestrator.py  (CLI)")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
