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
        font-size: 42px;
        font-weight: 900;
        margin: 0;
        letter-spacing: 2px;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    .raven-subtitle {
        color: #333;
        font-size: 20px;
        margin-top: 10px;
        font-weight: 300;
    }
    .section-container {
        background: white;
        padding: 30px;
        border: 2px solid #000;
        margin: 25px 0;
    }
    .section-title {
        color: #000;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .methodology-table {
        width: 100%;
        border: 2px solid #000;
        margin: 20px 0;
    }
    .methodology-table th {
        background: #000;
        color: white;
        padding: 15px;
        text-align: left;
        font-weight: 700;
    }
    .methodology-table td {
        padding: 15px;
        border-bottom: 1px solid #ddd;
    }
    .feature-box {
        background: white;
        padding: 20px;
        border: 1px solid #000;
        margin: 10px 0;
    }
    .author-credit {
        text-align: center;
        font-size: 16px;
        color: #000;
        margin-top: 10px;
        font-weight: 500;
    }
    .stat-highlight {
        background: #000;
        color: white;
        padding: 3px 8px;
        font-weight: 700;
        display: inline-block;
    }
    h2 {
        color: #000;
        font-weight: 800;
        margin-top: 30px;
    }
    h3 {
        color: #000;
        font-weight: 700;
        margin-top: 20px;
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
    ul li {
        margin: 10px 0;
    }
    .language-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
        gap: 15px;
        margin: 20px 0;
    }
    .language-item {
        border: 2px solid #000;
        padding: 10px;
        text-align: center;
        font-weight: 600;
    }
    .footer-note {
        background: #f8f8f8;
        border: 2px solid #000;
        padding: 20px;
        margin-top: 30px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="raven-header">
    <h1 class="raven-title">RAVEN TERMINAL</h1>
    <p class="raven-subtitle">Your Guide to Learning Code Intuitively</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="author-credit">Designed & Developed by Lee Akpareva MBA, MA</p>', unsafe_allow_html=True)

st.markdown("---")

# Introduction
st.markdown("""
<div class="section-container">
    <h3 class="section-title">Introduction: Beyond Just Writing Code</h3>
""", unsafe_allow_html=True)

st.markdown("""
Learning to code can be a daunting journey, often filled with complex syntax and abstract concepts. Many tools promise to make it easier by simply generating code for you, but this can leave you with a superficial grasp of the subject.

**RAVEN Terminal** is an intelligent platform designed for a different purpose: not just to generate code, but to build a deep, foundational understanding of programming. It is engineered to bridge the gap between natural language and programming, transforming how you learn and interact with code. This unique approach is designed to solve a growing challenge in modern software education.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Section 1: The Modern Coder's Dilemma
st.markdown("""
<div class="section-container">
    <h3 class="section-title">1. The Modern Coder's Dilemma: The "Fundamentals Crisis"</h3>
""", unsafe_allow_html=True)

st.markdown("""
In today's fast-paced development world, there is a rising trend of "vibe coders"—programmers who can use AI tools to write functional code but often lack a deep understanding of why it works or how to solve problems systematically. This dependency on AI is creating a **"fundamentals crisis."**

Developers are becoming overly reliant on AI coding assistants, which can quickly turn from powerful enablers into intellectual crutches. This masks critical gaps in fundamental knowledge, leading to a generation of developers who can prompt an AI but cannot truly program.
""")

# Highlight the statistic
st.markdown("""
<div style="background: #f8f8f8; padding: 20px; border-left: 4px solid #000; margin: 20px 0;">
<strong>This trend is more than an inconvenience; it is a growing catastrophe in the software industry.</strong><br><br>
According to a 2024 Stack Overflow survey, a staggering <span class="stat-highlight">67%</span> of junior developers now cannot debug their code without AI assistance, producing lower-quality software and hindering innovation.
</div>
""", unsafe_allow_html=True)

st.markdown("**RAVEN was built on a philosophy designed to reverse this trend.**")
st.markdown("</div>", unsafe_allow_html=True)

# Section 2: The RAVEN Philosophy
st.markdown("""
<div class="section-container">
    <h3 class="section-title">2. The RAVEN Philosophy: Learning with the "WHAT/HOW/WHY" Method</h3>
""", unsafe_allow_html=True)

st.markdown("""
RAVEN's core educational philosophy is to make learning intuitive by focusing on genuine understanding rather than rote memorization. The platform demystifies complex programming concepts by frequently using real-world analogies, making them accessible and relatable for beginners. This entire approach is built upon the **WHAT/HOW/WHY methodology**.
""")

# Create the methodology table
st.markdown("""
<table class="methodology-table">
<tr>
    <th>Component</th>
    <th>Explanation</th>
</tr>
<tr>
    <td><strong>WHAT</strong></td>
    <td>Clarifies what a piece of code does and its specific role within the application.</td>
</tr>
<tr>
    <td><strong>HOW</strong></td>
    <td>Demonstrates how to implement the code and explains the trade-offs of different approaches.</td>
</tr>
<tr>
    <td><strong>WHY</strong></td>
    <td>Reveals why the code works by connecting it to fundamental computer science principles.</td>
</tr>
</table>
""", unsafe_allow_html=True)

st.markdown("This structured learning method ensures that as you build, you are also building knowledge. This philosophy is directly integrated into the platform's core features.")
st.markdown("</div>", unsafe_allow_html=True)

# Section 3: Core Capabilities
st.markdown("""
<div class="section-container">
    <h3 class="section-title">3. Core Capabilities: Your AI-Powered Learning Toolkit</h3>
""", unsafe_allow_html=True)

st.markdown("""
RAVEN is an AI-powered platform that teaches while it assists, turning every interaction into a learning opportunity. Its toolkit is designed to guide you from idea to mastery.
""")

# Core features
features = [
    ("Natural language to code generation", "Translate your ideas into functional code and see complete project blueprints, providing a clear path from concept to execution."),
    ("Code explanation with real-life analogies", "Go beyond syntax to understand complex programming concepts through simple, relatable examples that stick."),
    ("Intelligent debugging, optimization, and language conversion", "Learn to fix, improve, and adapt code like an expert. RAVEN doesn't just correct errors; it explains why the fix works, teaching you critical problem-solving skills for the future."),
    ("Real-time syntax highlighting", "Visualize code structure with clear, color-coded notation that makes it easier to read and comprehend."),
    ("Automatic test generation", "Learn the professional practice of writing tests to prove your code works. RAVEN shows you how to build comprehensive test coverage, a crucial skill that separates amateurs from production-ready developers.")
]

for feature, description in features:
    st.markdown(f"""
    <div class="feature-box">
    <strong>{feature}:</strong> {description}
    </div>
    """, unsafe_allow_html=True)

st.markdown("With these tools, you can confidently explore a variety of modern programming languages.")
st.markdown("</div>", unsafe_allow_html=True)

# Section 4: Languages
st.markdown("""
<div class="section-container">
    <h3 class="section-title">4. Languages You Can Master with RAVEN</h3>
""", unsafe_allow_html=True)

st.markdown("RAVEN provides robust support for a range of popular and in-demand programming languages, allowing you to build a versatile and marketable skill set.")

# Create columns for languages
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="language-item">Python</div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="language-item">JavaScript</div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="language-item">TypeScript</div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="language-item">Java</div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="language-item">SQL</div>
    """, unsafe_allow_html=True)

st.markdown("**...with more coming soon.**")
st.markdown("</div>", unsafe_allow_html=True)

# Section 5: Begin Your Journey
st.markdown("""
<div class="section-container">
    <h3 class="section-title">5. Begin Your Journey to Deeper Understanding</h3>
""", unsafe_allow_html=True)

st.markdown("""
RAVEN Terminal is more than just a coding assistant; it is a dedicated educational partner. It is designed to build your skills, mastery, and confidence by systematically turning AI from a "crutch" into a powerful "enabler."

By focusing on the fundamentals, RAVEN empowers you to become a developer who can truly program, not just prompt.

**Start your journey into the world of intuitive and effective coding education today.**
""")
st.markdown("</div>", unsafe_allow_html=True)

# Footer - Open Source Note
st.markdown("""
<div class="footer-note">
    <h4>Open Source Initiative</h4>
    <p>RAVEN is an Open Source initiative with the objective of re-educating and empowering users to learn and appreciate the basis of coding in an engaging way.</p>
</div>
""", unsafe_allow_html=True)

# Contact Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h3 style="color: #000; font-weight: 700;">Contact & Connect</h3>
    <p style="color: #333;">For partnership and collaboration inquiries</p>
    <p style="color: #000;"><strong>Lee Akpareva MBA, MA</strong></p>
    <p style="color: #333;">Creator of RAVEN Terminal | AI Education Pioneer</p>
</div>
""", unsafe_allow_html=True)