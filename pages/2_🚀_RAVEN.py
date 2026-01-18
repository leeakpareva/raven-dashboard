import streamlit as st
import base64

# Page config is already set in main app

# Custom CSS for RAVEN page
st.markdown("""
    <style>
    .raven-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .raven-title {
        color: white;
        font-size: 48px;
        font-weight: bold;
        margin: 0;
    }
    .raven-subtitle {
        color: #f0f0f0;
        font-size: 24px;
        margin-top: 10px;
    }
    .slide-container {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 10px;
        margin: 20px 0;
        border-left: 5px solid #667eea;
    }
    .slide-title {
        color: #667eea;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .spec-box {
        background: white;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .logo-container {
        text-align: center;
        margin: 30px 0;
    }
    .author-credit {
        text-align: center;
        font-size: 20px;
        color: #666;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header with gradient background
st.markdown("""
<div class="raven-header">
    <h1 class="raven-title">RAVEN</h1>
    <p class="raven-subtitle">Empowering the Future of AI Education</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="author-credit">Designed & Developed by Lee Akpareva MBA, MA</p>', unsafe_allow_html=True)

# Logo placeholder - would display the actual logo if provided
st.markdown("""
<div class="logo-container">
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                width: 200px; height: 80px; margin: 0 auto; border-radius: 10px;
                display: flex; align-items: center; justify-content: center;">
        <span style="color: white; font-size: 48px; font-weight: bold;">RAVEN</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 📋 Investor Deck")

# Slide 1: The Vision
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">📌 Slide 1: The Vision</h3>
""", unsafe_allow_html=True)
st.markdown("""
RAVEN is an innovative educational technology platform designed to democratise artificial intelligence education through hands-on, immersive learning experiences. As a portable computing revolution, it serves as a statement of freedom and empowerment, allowing users to carry the power of AI in the palm of their hand. Our mission is to bridge the gap between theoretical AI knowledge and practical, real-world application.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Slide 2: The Problem & Opportunity
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">🔍 Slide 2: The Problem & Opportunity</h3>
""", unsafe_allow_html=True)
st.markdown("""
Traditional AI education often lacks a physical foundation, leaving a gap between abstract algorithms and tangible hardware. There is a growing need in educational institutions and small businesses for a platform that simplifies complex AI concepts into concrete learning experiences. RAVEN addresses this by providing a cost-effective, accessible, and high-performance gateway to AI literacy.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Slide 3: The Solution
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">💡 Slide 3: The Solution – RAVEN</h3>
""", unsafe_allow_html=True)
st.markdown("""
RAVEN is an AI-powered open-source device designed and developed by Lee Akpareva. It is built on the robust foundation of the Raspberry Pi 4 Model B, combining high-performance computing with a compact, customisable form factor. The platform transforms curiosity into capability by allowing users to build, programme, and experiment with edge AI technology.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Slide 4: Product Specifications
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">⚙️ Slide 4: Product Specifications</h3>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="spec-box">
    <strong>🖥️ Core Compute</strong><br>
    Quad-core ARM Cortex-A72 (64-bit) @ 1.5GHz with 4GB or 8GB LPDDR4 RAM
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="spec-box">
    <strong>📱 Interface</strong><br>
    3.5"–4" IPS Capacitive Multi-touchscreen optimized for mobile UIs and edge apps
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="spec-box">
    <strong>🌐 Connectivity</strong><br>
    Dual-band Wi-Fi, Bluetooth 5.0, and full GPIO access for hardware expansion
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="spec-box">
    <strong>🏗️ Enclosure & Design</strong><br>
    Precision 3D-printed chassis in matte polymer or transparent technical shells. Meticulously crafted using Shaper3D and Blender
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Slide 5: 360-Degree Learning
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">🎯 Slide 5: The 360-Degree Learning Approach</h3>
""", unsafe_allow_html=True)

st.markdown("**RAVEN fosters deep understanding across four fundamental pillars of AI education:**")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    #### 💻 Programming
    Interactive environments for teaching AI algorithms and ML best practices
    """)

with col2:
    st.markdown("""
    #### 🤖 Robotics
    Hands-on exploration of autonomous systems and sensor integration
    """)

with col3:
    st.markdown("""
    #### 🔧 Hardware
    Understanding physical foundations from microprocessors to embedded systems
    """)

with col4:
    st.markdown("""
    #### 🎨 3D Design
    Exploring spatial computing, computer vision, and AI-driven creative tech
    """)

st.markdown("</div>", unsafe_allow_html=True)

# Slide 6: AI Capabilities
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">🧠 Slide 6: AI & Edge Computing Capabilities</h3>
""", unsafe_allow_html=True)

st.markdown("**RAVEN is engineered for both local and cloud-connected AI workflows:**")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    **Local Inference**
    Runs Large Language Models (LLMs), vision, and speech processing directly on device
    """)

    st.info("""
    **Framework Support**
    Fully compatible with Python, TensorFlow Lite, PyTorch, LangChain, and CrewAI
    """)

with col2:
    st.success("""
    **Cloud Integration**
    Seamlessly connects to AI agents: OpenAI, Claude, and Gemini
    """)

    st.info("""
    **Edge Utility**
    Functions as gateway for IoT automation and robotics control
    """)

st.markdown("</div>", unsafe_allow_html=True)

# Slide 7: Market Focus
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">🎯 Slide 7: Market Focus – Education & Small Business</h3>
""", unsafe_allow_html=True)

st.markdown("**RAVEN is uniquely positioned to empower:**")

tab1, tab2, tab3 = st.tabs(["🎓 Educational Institutions", "💼 Small Businesses", "🔬 Makers & Researchers"])

with tab1:
    st.markdown("""
    Providing students with a tangible platform to progress from basic coding to advanced machine learning
    """)

with tab2:
    st.markdown("""
    Enabling the development of custom AI agents and edge computing solutions to automate operations
    """)

with tab3:
    st.markdown("""
    Offering a fully open-source environment (including CAD files and firmware) for endless hardware modification
    """)

st.markdown("</div>", unsafe_allow_html=True)

# Slide 8: Innovation & Accessibility
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">🌍 Slide 8: Innovation & Accessibility</h3>
""", unsafe_allow_html=True)

st.markdown("""
By leveraging the Raspberry Pi architecture, RAVEN remains **globally accessible and cost-effective** without sacrificing computational power.

The **open-source nature** of the project—including its STL files and software—ensures that innovators can adapt the hardware to their specific needs.

This deliberate design choice reflects a commitment to **making advanced AI education available to everyone**, regardless of economic barriers.
""")

st.markdown("</div>", unsafe_allow_html=True)

# Slide 9: The Future
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">🚀 Slide 9: The Future of AI Innovation</h3>
""", unsafe_allow_html=True)

st.markdown("""
RAVEN represents the foundation for tomorrow's technological breakthroughs.

We are seeking **partners and investors** to help scale this platform into classrooms and businesses worldwide, fostering a new generation of AI innovators.

### **Join us in unleashing the future where curiosity meets capability!**
""")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h3>Contact & Connect</h3>
    <p>For partnership and investment inquiries</p>
    <p><strong>Lee Akpareva MBA, MA</strong></p>
    <p>Creator of RAVEN | AI Education Pioneer</p>
</div>
""", unsafe_allow_html=True)