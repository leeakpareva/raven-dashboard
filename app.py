import streamlit as st

# Set page config
st.set_page_config(
    page_title="RAVEN Dashboard - AI & Software Education",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for home page
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 40px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 30px;
    }
    .main-title {
        color: white;
        font-size: 56px;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .main-subtitle {
        color: #f0f0f0;
        font-size: 24px;
        margin-top: 15px;
    }
    .author-credit {
        color: #e0e0e0;
        font-size: 18px;
        margin-top: 20px;
    }
    .feature-card {
        background: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        height: 100%;
        transition: transform 0.3s;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .nav-instruction {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 20px 0;
    }
    .logo-display {
        text-align: center;
        margin: 30px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Main header with gradient background
st.markdown("""
<div class="main-header">
    <h1 class="main-title">RAVEN DASHBOARD</h1>
    <p class="main-subtitle">Bridging AI Education & Software Development Excellence</p>
    <p class="author-credit">By Lee Akpareva MBA, MA</p>
</div>
""", unsafe_allow_html=True)

# RAVEN Logo Display (styled placeholder)
st.markdown("""
<div class="logo-display">
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                width: 250px; height: 100px; margin: 0 auto; border-radius: 15px;
                display: flex; align-items: center; justify-content: center;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);">
        <span style="color: white; font-size: 56px; font-weight: bold; letter-spacing: 3px;">RAVEN</span>
    </div>
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
    <h3>📍 Navigation</h3>
    <p>Use the <strong>sidebar menu</strong> on the left to explore:</p>
    <ul>
        <li><strong>📊 Crisis Dashboard</strong> - Explore the data and impact of AI on software development</li>
        <li><strong>🚀 RAVEN</strong> - Learn about the AI education platform and investment opportunity</li>
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
        <h3>📊 Crisis Dashboard</h3>
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
        <h3>🚀 RAVEN Platform</h3>
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
## 🎯 Our Mission

To transform AI from a crutch into an enabler by:
- **Educating** developers on fundamentals
- **Empowering** learners with hands-on AI experience
- **Building** a future where technology enhances rather than replaces understanding

### Start Exploring
👈 **Use the sidebar** to navigate to the Crisis Dashboard or RAVEN platform pages.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>© 2024 RAVEN Dashboard | Designed & Developed by Lee Akpareva MBA, MA</p>
    <p>Empowering the Future of AI Education</p>
</div>
""", unsafe_allow_html=True)