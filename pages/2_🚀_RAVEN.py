import streamlit as st

# Page config is already set in main app

# Custom CSS for RAVEN page - Clean black and white design
st.markdown("""
    <style>
    .raven-header {
        text-align: center;
        padding: 30px 20px;
        border-bottom: 3px solid #000;
        margin-bottom: 30px;
    }
    .raven-title {
        color: #000;
        font-size: 48px;
        font-weight: 900;
        margin: 0;
        letter-spacing: 3px;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    .raven-subtitle {
        color: #333;
        font-size: 20px;
        margin-top: 10px;
        font-weight: 300;
    }
    .slide-container {
        background: white;
        padding: 30px;
        border: 2px solid #000;
        margin: 25px 0;
    }
    .slide-title {
        color: #000;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .spec-box {
        background: white;
        padding: 20px;
        border: 1px solid #000;
        margin: 10px 0;
    }
    .logo-container {
        text-align: center;
        margin: 30px 0;
    }
    .author-credit {
        text-align: center;
        font-size: 16px;
        color: #000;
        margin-top: 10px;
        font-weight: 500;
    }
    h2 {
        color: #000;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 30px;
    }
    h3 {
        color: #000;
        font-weight: 700;
    }
    h4 {
        color: #000;
        font-weight: 600;
        margin-top: 15px;
    }
    strong {
        color: #000;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# Header - clean black and white
st.markdown("""
<div class="raven-header">
    <h1 class="raven-title">RAVEN</h1>
    <p class="raven-subtitle">Empowering the Future of AI Education</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="author-credit">Designed & Developed by Lee Akpareva MBA, MA</p>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("## Investor Deck")

# Slide 1: The Vision
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">Slide 1: The Vision</h3>
""", unsafe_allow_html=True)
st.markdown("""
RAVEN is an innovative educational technology platform designed to democratise artificial intelligence education through hands-on, immersive learning experiences. As a portable computing revolution, it serves as a statement of freedom and empowerment, allowing users to carry the power of AI in the palm of their hand. Our mission is to bridge the gap between theoretical AI knowledge and practical, real-world application.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Slide 2: The Problem & Opportunity
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">Slide 2: The Problem & Opportunity</h3>
""", unsafe_allow_html=True)
st.markdown("""
Traditional AI education often lacks a physical foundation, leaving a gap between abstract algorithms and tangible hardware. There is a growing need in educational institutions and small businesses for a platform that simplifies complex AI concepts into concrete learning experiences. RAVEN addresses this by providing a cost-effective, accessible, and high-performance gateway to AI literacy.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Slide 3: The Solution
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">Slide 3: The Solution – RAVEN</h3>
""", unsafe_allow_html=True)
st.markdown("""
RAVEN is an AI-powered open-source device designed and developed by Lee Akpareva. It is built on the robust foundation of the Raspberry Pi 4 Model B, combining high-performance computing with a compact, customisable form factor. The platform transforms curiosity into capability by allowing users to build, programme, and experiment with edge AI technology.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Slide 4: Product Specifications
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">Slide 4: Product Specifications</h3>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="spec-box">
    <strong>Core Compute</strong><br>
    Quad-core ARM Cortex-A72 (64-bit) @ 1.5GHz with 4GB or 8GB LPDDR4 RAM
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="spec-box">
    <strong>Interface</strong><br>
    3.5"–4" IPS Capacitive Multi-touchscreen optimized for mobile UIs and edge apps
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="spec-box">
    <strong>Connectivity</strong><br>
    Dual-band Wi-Fi, Bluetooth 5.0, and full GPIO access for hardware expansion
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="spec-box">
    <strong>Enclosure & Design</strong><br>
    Precision 3D-printed chassis in matte polymer or transparent technical shells. Meticulously crafted using Shaper3D and Blender
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Slide 5: 360-Degree Learning
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">Slide 5: The 360-Degree Learning Approach</h3>
""", unsafe_allow_html=True)

st.markdown("**RAVEN fosters deep understanding across four fundamental pillars of AI education:**")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    #### Programming
    Interactive environments for teaching AI algorithms and ML best practices
    """)

with col2:
    st.markdown("""
    #### Robotics
    Hands-on exploration of autonomous systems and sensor integration
    """)

with col3:
    st.markdown("""
    #### Hardware
    Understanding physical foundations from microprocessors to embedded systems
    """)

with col4:
    st.markdown("""
    #### 3D Design
    Exploring spatial computing, computer vision, and AI-driven creative tech
    """)

st.markdown("</div>", unsafe_allow_html=True)

# Slide 6: AI Capabilities
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">Slide 6: AI & Edge Computing Capabilities</h3>
""", unsafe_allow_html=True)

st.markdown("**RAVEN is engineered for both local and cloud-connected AI workflows:**")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="spec-box">
    <strong>Local Inference</strong><br>
    Runs Large Language Models (LLMs), vision, and speech processing directly on device
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="spec-box">
    <strong>Framework Support</strong><br>
    Fully compatible with Python, TensorFlow Lite, PyTorch, LangChain, and CrewAI
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="spec-box">
    <strong>Cloud Integration</strong><br>
    Seamlessly connects to AI agents: OpenAI, Claude, and Gemini
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="spec-box">
    <strong>Edge Utility</strong><br>
    Functions as gateway for IoT automation and robotics control
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Slide 7: Market Focus
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">Slide 7: Market Focus – Education & Small Business</h3>
""", unsafe_allow_html=True)

st.markdown("**RAVEN is uniquely positioned to empower:**")

st.markdown("""
**Educational Institutions**
Providing students with a tangible platform to progress from basic coding to advanced machine learning

**Small Businesses**
Enabling the development of custom AI agents and edge computing solutions to automate operations

**Makers & Researchers**
Offering a fully open-source environment (including CAD files and firmware) for endless hardware modification
""")

st.markdown("</div>", unsafe_allow_html=True)

# Slide 8: Innovation & Accessibility
st.markdown("""
<div class="slide-container">
    <h3 class="slide-title">Slide 8: Innovation & Accessibility</h3>
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
    <h3 class="slide-title">Slide 9: The Future of AI Innovation</h3>
""", unsafe_allow_html=True)

st.markdown("""
RAVEN represents the foundation for tomorrow's technological breakthroughs.

We are seeking **partners and investors** to help scale this platform into classrooms and businesses worldwide, fostering a new generation of AI innovators.

### Join us in unleashing the future where curiosity meets capability
""")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h3 style="color: #000; font-weight: 700;">Contact & Connect</h3>
    <p style="color: #333;">For partnership and investment inquiries</p>
    <p style="color: #000;"><strong>Lee Akpareva MBA, MA</strong></p>
    <p style="color: #333;">Creator of RAVEN | AI Education Pioneer</p>
</div>
""", unsafe_allow_html=True)