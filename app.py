"""
app.py
Streamlit UI for AML/KYC Compliance Agent Portfolio Demo
"""

import streamlit as st
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AML/KYC Compliance Agent",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .risk-high { border-left-color: #d9534f; }
    .risk-medium { border-left-color: #f0ad4e; }
    .risk-low { border-left-color: #5cb85c; }
    .json-output {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 15px;
        border-radius: 5px;
        font-family: monospace;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Title and header
st.title("🏦 Caribbean AML/KYC Compliance Agent")
st.markdown("""
**AI-Powered Screening for Jamaican Financial Institutions**  
*Aligned with BOJ, FSC, and CFATF Guidelines*
""")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    model_option = st.selectbox(
        "Model",
        ["claude-3-5-sonnet-20240620", "claude-3-haiku-20240307", "gpt-4o-mini"],
        index=0
    )
    
    risk_threshold = st.slider(
        "Risk Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.75,
        step=0.05
    )
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    st.metric("Transactions Processed", "0")
    st.metric("High Risk Flags", "0")
    st.metric("API Calls", "0")
    
    st.markdown("---")
    st.info("**Regional Focus:** Jamaica & CARICOM\n\nOptimized for local DFIs and Remittance Providers.")

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Transaction Screening",
    "👤 KYC Verification",
    "📈 Risk Dashboard",
    "📄 Audit Reports"
])

# Tab 1: Transaction Screening
with tab1:
    st.header("Transaction Screening")
    st.markdown("Screen transactions against sanctions lists and watchlists.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Transaction")
        transaction_name = st.text_input("Customer Name", "John Smith")
        transaction_amount = st.number_input("Amount (USD)", min_value=0, value=10000)
        transaction_country = st.selectbox(
            "Country",
            ["JM", "US", "GB", "CA", "TT", "BB", "KY", "BS", "HT", "CU"]
        )
        transaction_date = st.date_input("Date", datetime.now())
        
        screen_button = st.button("🔍 Run Screening", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("Screening Results")
        
        if screen_button:
            with st.spinner("Running sanctions check..."):
                # Mock response for portfolio (replace with actual agent call)
                mock_result = {
                    "entity_id": "TXN-2024-001",
                    "risk_score": 0.85 if transaction_country in ["CU", "HT", "BS"] else 0.25,
                    "risk_level": "HIGH" if transaction_country in ["CU", "HT", "BS"] else "LOW",
                    "flags": ["High-risk jurisdiction", "Large transaction"] if transaction_country in ["CU", "HT", "BS"] else [],
                    "sanctions_match": transaction_name.upper() in ["IVAN PETROV", "KIM JONG-SIK"],
                    "recommendation": "REVIEW" if transaction_country in ["CU", "HT", "BS"] else "APPROVE"
                }
                
                # Display risk level
                if mock_result["risk_level"] == "HIGH":
                    st.error(f"🚨 Risk Level: {mock_result['risk_level']}")
                elif mock_result["risk_level"] == "MEDIUM":
                    st.warning(f"⚠️ Risk Level: {mock_result['risk_level']}")
                else:
                    st.success(f"✅ Risk Level: {mock_result['risk_level']}")
                
                # Display metrics
                st.metric("Risk Score", f"{mock_result['risk_score']:.2f}")
                st.metric("Sanctions Match", "⚠️ YES" if mock_result["sanctions_match"] else "✅ NO")
                
                # Display flags
                if mock_result["flags"]:
                    st.markdown("**Flags:**")
                    for flag in mock_result["flags"]:
                        st.markdown(f"- {flag}")
                
                # Display recommendation
                st.markdown("**Recommendation:**")
                st.info(f"{mock_result['recommendation']}")
        
        else:
            st.info("Enter transaction details and click 'Run Screening'")

# Tab 2: KYC Verification
with tab2:
    st.header("KYC Document Verification")
    st.markdown("Verify customer identity and Ultimate Beneficial Owner (UBO) mapping.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Customer Information")
        kyc_name = st.text_input("Full Name", "Jane Doe")
        kyc_id_type = st.selectbox("ID Type", ["Passport", "Driver's License", "National ID"])
        kyc_id_number = st.text_input("ID Number", "AB1234567")
        kyc_country = st.selectbox("Country of Residence", ["US", "GB", "CA", "AU", "DE", "FR"])
        kyc_ubo = st.text_area("Ultimate Beneficial Owners (one per line)", "Jane Doe\n")
        
        verify_button = st.button("👤 Verify KYC", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("Verification Results")
        
        if verify_button:
            with st.spinner("Verifying documents..."):
                # Mock response for portfolio
                mock_kyc = {
                    "document_valid": True,
                    "identity_verified": True,
                    "pep_match": kyc_name.upper() in ["MARIA GONZALEZ", "DMITRI VOLKOV"],
                    "ubo_count": len(kyc_ubo.strip().split("\n")),
                    "risk_level": "HIGH" if kyc_name.upper() in ["MARIA GONZALEZ", "DMITRI VOLKOV"] else "LOW"
                }
                
                st.markdown("**Document Status:**")
                if mock_kyc["document_valid"]:
                    st.success("✅ Document Valid")
                else:
                    st.error("❌ Document Invalid")
                
                st.markdown("**Identity Verification:**")
                if mock_kyc["identity_verified"]:
                    st.success("✅ Identity Verified")
                else:
                    st.error("❌ Identity Failed")
                
                st.markdown("**PEP Check:**")
                if mock_kyc["pep_match"]:
                    st.warning("⚠️ PEP Match Found")
                else:
                    st.success("✅ No PEP Match")
                
                st.metric("UBOs Identified", mock_kyc["ubo_count"])

# Tab 3: Risk Dashboard
with tab3:
    st.header("Risk Analytics Dashboard")
    st.markdown("Visualize risk distribution and compliance metrics.")
    
    # Mock metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Screened", "1,247")
    with col2:
        st.metric("High Risk", "43", delta="-5%")
    with col3:
        st.metric("Sanctions Matches", "2", delta="0")
    with col4:
        st.metric("Pending Review", "15", delta="+3")
    
    st.markdown("---")
    
    # Mock chart data
    st.subheader("Risk Distribution")
    risk_data = {
        "LOW": 850,
        "MEDIUM": 354,
        "HIGH": 43
    }
    st.bar_chart(risk_data)
    
    st.subheader("Transactions by Country")
    country_data = {
        "JM": 500,
        "US": 300,
        "GB": 200,
        "CA": 150,
        "TT": 50,
        "BB": 47,
        "KY": 47,
        "BS": 47,
        "HT": 47, 
        "CU": 47
    }
    st.bar_chart(country_data)

# Tab 4: Audit Reports
with tab4:
    st.header("Audit Reports")
    st.markdown("Download compliance audit reports for regulatory review.")
    
    st.subheader("Generate Report")
    
    report_type = st.selectbox(
        "Report Type",
        ["Transaction Screening Report", "KYC Verification Report", "Full Audit Trail"]
    )
    
    report_format = st.selectbox(
        "Format",
        ["PDF", "JSON"]
    )
    
    if st.button("📄 Generate Report", type="primary"):
        with st.spinner("Generating report..."):
            # Mock report generation
            st.success("✅ Report generated successfully!")
            
            # Display mock report preview
            st.markdown("**Report Preview:**")
            mock_report = {
                "report_id": "RPT-2024-001",
                "generated_at": datetime.now().isoformat(),
                "report_type": report_type,
                "format": report_format,
                "total_transactions": 1247,
                "flags_raised": 43,
                "sanctions_matches": 2,
                "compliance_officer": "System Generated",
                "status": "Pending Review"
            }
            
            st.json(mock_report)
            
            st.download_button(
                label="📥 Download Report",
                data=json.dumps(mock_report, indent=2),
                file_name=f"compliance_report_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <small>
    🏦 AML/KYC Compliance Agent · Portfolio Project · Built with Claude Sonnet & Streamlit<br>
    <strong>Disclaimer:</strong> This is a demonstration tool. All decisions should be reviewed by qualified compliance officers.
    </small>
</div>
""", unsafe_allow_html=True)
