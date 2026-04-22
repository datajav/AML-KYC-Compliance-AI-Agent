import json
import os

def check_sanctions(name: str) -> dict:
    """
    Checks a name against the local sanctions list.
    Returns match status and confidence.
    """
    file_path = "data/sanctions_list.json"
    
    if not os.path.exists(file_path):
        return {"error": "Sanctions list not found"}
    
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Simple fuzzy match (case-insensitive)
    matches = []
    for entity in data.get("entities", []):
        if name.lower() in entity["name"].lower() or entity["name"].lower() in name.lower():
            matches.append(entity)
    
    is_sanctioned = len(matches) > 0
    
    return {
        "is_sanctioned": is_sanctioned,
        "matches": matches,
        "confidence": 0.95 if is_sanctioned else 0.0,
        "tool_name": "sanctions_checker"
    }
