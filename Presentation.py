import streamlit as st

# Set page configuration
st.set_page_config(page_title="CRF Report App | Financial Reporting Solution", layout="centered")

# Title Section (Global for all Tabs)
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #4A90E2;
        padding-top: 10px;
        padding-bottom: 30px;
    }
    .sub-title {
        font-size: 22px;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    .text {
        font-size: 18px;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# Display the main title
st.markdown('<div class="main-title">CRF Report App - Financial Reporting Solution</div>', unsafe_allow_html=True)

# Create Tabs for the Presentation
tabs = st.tabs(["Overview", "Key Features", "Why Choose This App?", "Get Started"])

# Tab 1: Overview
with tabs[0]:
    st.markdown('<div class="sub-title">Overview</div>', unsafe_allow_html=True)
    st.write("""
    The **CRF Report App** is a cutting-edge financial reporting solution designed for the **Children's Rescue Fund (CRF)**. 
    The app processes, analyzes, and visualizes financial and operational data to streamline reporting. 
    By automating report generation, this tool enables CRF to focus on key decision-making based on clear financial trends and insights.
    """)
    st.markdown('<div class="text">Key Features Include:</div>', unsafe_allow_html=True)
    st.write("""
    - Data aggregation from multiple sources.
    - Structured and automated financial reporting.
    - Real-time visualizations to highlight key metrics.
    """)

# Tab 2: Key Features
with tabs[1]:
    st.markdown('<div class="sub-title">Key Features</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">This app provides a variety of powerful features designed to enhance financial reporting and analysis:</div>', unsafe_allow_html=True)
    st.write("""
    1. **Data Processing**: Automatically cleans and structures data, making it easier to generate accurate reports.
    2. **Automated Reporting**: Generate structured financial reports with the click of a button.
    3. **Interactive Visualizations**: Get real-time insights into financial trends through interactive charts and graphs.
    4. **Operational Insights**: Analyze shelter operations, daily costs, and funding allocations to optimize resource usage.
    """)

# Tab 3: Why Choose This App?
with tabs[2]:
    st.markdown('<div class="sub-title">Why Choose This App?</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">The CRF Report App offers unique benefits that make it an indispensable tool for nonprofits:</div>', unsafe_allow_html=True)
    st.write("""
    - **Increased Efficiency**: Say goodbye to hours spent on manual reporting. Our automated solution reduces reporting time by 80%.
    - **Data-Driven Decisions**: Provides clear and actionable insights that lead to smarter, data-driven decision-making.
    - **User-Friendly Interface**: No need to be a data expert—this app makes financial reporting accessible for all.
    - **Tailored for Nonprofits**: Specifically designed to meet the unique reporting needs of organizations like CRF.
    """)

# Tab 4: Get Started
with tabs[3]:
    st.markdown('<div class="sub-title">Ready to Transform Your Reporting?</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Use the CRF Report App to simplify your financial reporting and make informed decisions faster.</div>', unsafe_allow_html=True)
    st.write("""
    - **Contact Us**: Reach out to learn more about how we can customize this solution for your organization's unique needs.
    - **Demo**: Request a live demo to see the app in action.
    - **Get Started**: Visit our [website](https://yourwebsite.com) to start using the app today.
    """)
    
    st.markdown("""
    ---
    *Note*: The CRF Report App is a part of our ongoing mission to support nonprofit organizations with tools that streamline financial operations and improve transparency.
    """)
