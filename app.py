import streamlit as st

# Set page config
st.set_page_config(
    page_title="RAVEN Dashboard - AI & Software Education",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for home page - Clean black and white design
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 40px 20px;
        border-bottom: 3px solid #000;
        margin-bottom: 40px;
    }
    .main-title {
        color: #000;
        font-size: 48px;
        font-weight: 900;
        margin: 0;
        letter-spacing: 2px;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    .main-subtitle {
        color: #333;
        font-size: 20px;
        margin-top: 10px;
        font-weight: 300;
    }
    .author-credit {
        color: #000;
        font-size: 16px;
        margin-top: 15px;
        font-weight: 500;
    }
    .feature-card {
        background: white;
        padding: 30px;
        border: 2px solid #000;
        height: 100%;
        transition: all 0.2s;
    }
    .feature-card:hover {
        background: #f9f9f9;
    }
    .nav-instruction {
        background: white;
        padding: 25px;
        border: 2px solid #000;
        margin: 30px 0;
    }
    .logo-display {
        text-align: center;
        margin: 40px 0;
    }
    h2 {
        color: #000;
        font-weight: 700;
        margin-top: 30px;
    }
    h3 {
        color: #000;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Main header - clean black and white
st.markdown("""
<div class="main-header">
    <h1 class="main-title">RAVEN DASHBOARD</h1>
    <p class="main-subtitle">Bridging AI Education & Software Development Excellence</p>
    <p class="author-credit">By Lee Akpareva MBA, MA</p>
</div>
""", unsafe_allow_html=True)


# Welcome message
st.markdown("""
## Welcome to RAVEN Dashboard

This platform combines two critical perspectives on the future of technology:

1. **The Silent Crisis** - An in-depth analysis of how AI is undermining software development fundamentals
2. **RAVEN** - The solution through AI-powered education that bridges theory and practice
""")

# Navigation instruction
st.markdown("""
<div class="nav-instruction">
    <h3>Navigation</h3>
    <p>Use the <strong>sidebar menu</strong> on the left to explore:</p>
    <ul>
        <li><strong>Crisis Dashboard</strong> - Explore the data and impact of AI on software development</li>
        <li><strong>RAVEN</strong> - Learn about the AI education platform and investment opportunity</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Feature cards
st.markdown("---")
st.markdown("## Platform Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>Crisis Dashboard</h3>
        <p><strong>Data-Driven Insights</strong></p>
        <ul>
            <li>Real-time statistics on AI adoption</li>
            <li>Skills gap analysis</li>
            <li>Economic impact visualization</li>
            <li>Case studies of AI-related failures</li>
            <li>The path forward with educational AI</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>RAVEN Platform</h3>
        <p><strong>AI Education Revolution</strong></p>
        <ul>
            <li>Open-source AI device</li>
            <li>360-degree learning approach</li>
            <li>Edge computing capabilities</li>
            <li>Market-ready solution</li>
            <li>Investment opportunity</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Call to action
st.markdown("---")
st.markdown("""
## Our Mission

To transform AI from a crutch into an enabler by:
- **Educating** developers on fundamentals
- **Empowering** learners with hands-on AI experience
- **Building** a future where technology enhances rather than replaces understanding

### Start Exploring
**Use the sidebar** to navigate to the Crisis Dashboard or RAVEN platform pages.
""")

# Technology Stack Section
st.markdown("---")
st.markdown("## Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>Core Framework</h4>
        <p><strong>Streamlit</strong> - Interactive web application framework</p>
        <p><strong>Python 3.8+</strong> - Programming language</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>Data Visualization</h4>
        <p><strong>Plotly</strong> - Interactive charts and graphs</p>
        <p><strong>Pandas</strong> - Data manipulation and analysis</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h4>Deployment</h4>
        <p><strong>GitHub</strong> - Version control</p>
        <p><strong>Streamlit Cloud</strong> - Hosting platform</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>© 2024 RAVEN Dashboard | Designed & Developed by Lee Akpareva MBA, MA</p>
    <p>Empowering the Future of AI Education</p>
</div>
""", unsafe_allow_html=True)