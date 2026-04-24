def  calculate_risk_score(country: str, amount: float, is_pep: bool, is_sanctioned: bool) ->  dict:
    """Calculate a risk score based on various factors for Caribbean countries."""
    score = 0.0
    flags = []

    # 1. High Risk Jurisdictions//includes Caribbean countries that are considered high risk by CFATF
    high_risk_countries = ["JM", "HT", "VE", "CU", "KY", "BZ"]
    if country in high_risk_countries:
       score += 0.3
       flags.append("CFATF High Risk Jusrisdiction")

    # 2. Correspondent Banking Risk (USD Transactions)//Caribbean banks de-risking from US banks
    if country == "US" and amount > 50000: 
        score += 0.2
        flags.append("Large USD Transaction")

    # 3. Cash Intensive Businesses//Caribbean economies have a high prevalence of cash-based businesses
    highrisk_sectors = ["Casino", "Real Estate", "Precious Metals", "Import/Export"]
    if any(sector in business_type for sector in highrisk_sectors):
        score += 0.3
        flags.append("Cash Intensive Business Sector")
    
    # 4. Citizenship and Residency Programs//Caribbean countries offering citizenship by investment programs
    if "CBI" in business_type or "Citizenship" in business_type:
        score += 0.4
        flags.append("Citizenship by Investment Program")

    # 5. Politically Exposed Persons (PEPs)
    if is_pep:
        score += 0.3
        flags.append("Politically Exposed Person")
    
    # 6. Sanctions and Watchlists
    if is_sanctioned:
        score += 1.0
        flags.append("Sanctioned Individual or Entity")
    
    final_score = min(score, 1.0)

    #Determine level based on BOJ guidelines
    if final_score >= 0.75:
        risk_level = "High"
    elif final_score >= 0.45:
        risk_level = "Medium"
    else:
        risk_level = "Low"
    
    return {
        "risk_score": final_score, 
        "risk_level": level, 
        "flags": flags, 
        "tool_name": "risk_scorer",
        "region": "Caribbean"
    }

    

