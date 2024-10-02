import streamlit as st

# Set page configuration
st.set_page_config(page_title="CRF Report App Overview", layout="centered")

# Create Tabs
tabs = st.tabs(["Overview", "Key Features", "Why Use This App?", "Explore"])

# Tab 1: Overview
with tabs[0]:
    st.title("Overview")
    st.write("""
    This app processes and visualizes financial and operational data for the **Children's Rescue Fund (CRF)**. 
    It automates the generation of reports, making it easier to track financial trends, generate visual reports, and provide insights for stakeholders.
    """)

# Tab 2: Key Features
with tabs[1]:
    st.title("Key Features")
    st.write("""
    1. **Data Processing**: Cleans and structures financial data from multiple sources.
    2. **Automated Reporting**: Automatically generates structured financial reports for easy review.
    3. **Visualization**: Provides clear and interactive charts and graphs to better understand financial trends.
    4. **Operational Insights**: Delivers insights into shelter operations, costs, and funding allocations.
    """)

# Tab 3: Why Use This App?
with tabs[2]:
    st.title("Why Use This App?")
    st.write("""
    - **Efficiency**: Automates reporting tasks that would take hours to complete manually.
    - **Clarity**: Visualizes complex financial data for easy analysis.
    - **Decision-Making**: Provides real-time insights to support data-driven decisions for the CRF's operations.
    """)

# Tab 4: Explore
with tabs[3]:
    st.title("Ready to Explore?")
    st.write("""
    Use this app to quickly generate and visualize comprehensive financial reports for CRF.
    """)
    st.markdown("""
    ---
    *Note*: This app is part of an ongoing project aimed at enhancing the financial reporting capabilities for nonprofit organizations.
    """)

