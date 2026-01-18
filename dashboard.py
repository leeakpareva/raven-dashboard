import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="The Silent Crisis: AI & Software Foundations",
    page_icon="🚨",
    layout="wide"
)

# Custom CSS for "Story Style"
st.markdown("""
    <style>
    .main {
        max-width: 1200px;
        margin: 0 auto;
    }
    .big-font {
        font-size: 24px !important;
        font-weight: 300;
    }
    .quote-box {
        border-left: 5px solid #ff4b4b;
        background-color: #f0f2f6;
        padding: 20px;
        margin: 20px 0;
        font-style: italic;
        color: #31333F;
    }
    h1 {
        color: #0E1117;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h2 {
        color: #ff4b4b;
        padding-top: 20px;
    }
    h3 {
        color: #31333F;
    }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.title("🚨 The Silent Crisis")
st.markdown("# When AI Eats the Foundations of Software Development")
st.markdown("---")

# Sidebar for Navigation
with st.sidebar:
    st.header("Navigation")
    st.markdown("""
    - [The Automation Avalanche](#the-automation-avalanche)
    - [The Fundamentals Crisis](#the-fundamentals-crisis)
    - [Real-World Catastrophes](#real-world-catastrophes)
    - [The Economic Impact](#the-economic-impact)
    - [The Path Forward](#the-path-forward-ai-as-enabler-not-crutch)
    """)
    st.markdown("---")
    st.info("**Data Sources**: Stack Overflow 2024, IEEE 2023, Gartner 2024, UC Berkeley 2023, MIT 2024, IDC 2024.")

# -----------------------------------------------------------------------------
# SECTION 1: The Automation Avalanche
# -----------------------------------------------------------------------------
st.header("The Automation Avalanche")
st.markdown("""
In 2023, GitHub Copilot achieved a remarkable milestone: **1 million developers** were using AI coding assistants daily. 
By 2024, that number exploded to over **4 million**. 
Stack Overflow's 2024 Developer Survey revealed that **83%** of professional developers now use AI coding tools regularly. 

On the surface, this looks like progress. **Beneath the surface, it masks a growing catastrophe.**
""")

col1, col2 = st.columns(2)

with col1:
    # Line chart for Copilot Users
    df_adoption = pd.DataFrame({
        'Year': ['2023', '2024'],
        'Users (Millions)': [1, 4]
    })
    fig_adoption = px.line(df_adoption, x='Year', y='Users (Millions)', 
                           title='GitHub Copilot Daily Users (Millions)',
                           markers=True, text='Users (Millions)')
    fig_adoption.update_traces(textposition="bottom right")
    fig_adoption.update_layout(yaxis_range=[0, 5])
    st.plotly_chart(fig_adoption, use_container_width=True)

with col2:
    # Gauge/Indicator for % Developers using AI
    fig_percent = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 83,
        title = {'text': "Professional Developers Using AI"},
        gauge = {'axis': {'range': [None, 100]},
                 'bar': {'color': "#ff4b4b"},
                 'steps': [
                     {'range': [0, 50], 'color': "lightgray"},
                     {'range': [50, 80], 'color': "gray"}],
                 'threshold': {
                     'line': {'color': "red", 'width': 4},
                     'thickness': 0.75,
                     'value': 90}}
    ))
    st.plotly_chart(fig_percent, use_container_width=True)

# -----------------------------------------------------------------------------
# SECTION 2: The Fundamentals Crisis
# -----------------------------------------------------------------------------
st.header("The Fundamentals Crisis")
st.markdown("""
### The Data Doesn't Lie
A 2023 study by the IEEE Computer Society found that **56%** of new developers struggle with basic algorithms and data structures. 
The same survey revealed that **72%** of recent graduates rely heavily on AI tools for tasks they should master manually.
""")

# Bar Chart for Skills Crisis
skills_data = {
    'Metric': [
        'Architecture Blindness (Gartner)',
        'Recent Grads Relying on AI (IEEE)',
        'Junior Devs Cant Debug (StackOverflow)',
        'New Devs Struggle w/ Algos (IEEE)'
    ],
    'Percentage': [81, 72, 67, 56]
}
df_skills = pd.DataFrame(skills_data)
df_skills = df_skills.sort_values('Percentage', ascending=True)

fig_skills = px.bar(df_skills, x='Percentage', y='Metric', orientation='h',
                    title='The Skill Gap Indicators (2023-2024)',
                    text='Percentage', color='Percentage',
                    color_continuous_scale='Reds')
fig_skills.update_traces(texttemplate='%{text}%', textposition='outside')
fig_skills.update_layout(xaxis_range=[0, 100])
st.plotly_chart(fig_skills, use_container_width=True)

st.markdown("""
<div class="quote-box">
"Computer science graduates' ability to write basic sorting algorithms dropped <b>28%</b> between 2018-2023." (UC Berkeley study)
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SECTION 3: The Hidden Cost & Economic Impact
# -----------------------------------------------------------------------------
st.header("The Economic Impact: A Billion-Dollar Blind Spot")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### The Cost of Technical Debt")
    st.markdown("""
    Technical debt in enterprise software reached **$2.7 trillion** globally in 2024, up 23% from 2023.
    **42%** of this debt stems from developers who don't understand fundamental concepts.
    """)
    
    # Donut chart for Technical Debt Source
    labels = ['Due to Fundamental Gaps', 'Other Causes']
    values = [42, 58]
    fig_debt = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6, marker_colors=['#ff4b4b', '#lightgray'])])
    fig_debt.update_layout(title_text="Sources of $2.7T Technical Debt")
    st.plotly_chart(fig_debt, use_container_width=True)

with col2:
    st.markdown("### The Cost of Poor Quality")
    st.markdown("""
    Global software development costs exceeded **$2.1 trillion** in 2024. 
    Poor code quality costs enterprises **$1.5 trillion** annually.
    """)
    
    # Bar chart comparing Total Cost vs Waste
    df_cost = pd.DataFrame({
        'Category': ['Total Dev Cost', 'Cost of Poor Quality'],
        'Amount (Trillions USD)': [2.1, 1.5]
    })
    fig_cost = px.bar(df_cost, x='Category', y='Amount (Trillions USD)',
                      title='Global Software Development Economics (2024)',
                      color='Category', color_discrete_map={'Total Dev Cost': 'gray', 'Cost of Poor Quality': 'red'})
    st.plotly_chart(fig_cost, use_container_width=True)

st.info("45% of development time is spent fixing issues from misunderstood fundamentals.")

# -----------------------------------------------------------------------------
# SECTION 4: Real-World Catastrophes
# -----------------------------------------------------------------------------
st.header("Real-World Catastrophes")
st.markdown("When the lack of fundamentals meets production environments, the results are disastrous.")

tab1, tab2, tab3 = st.tabs(["📉 Banking Meltdown", "🏥 Healthcare Breach", "🚀 Startup Graveyard"])

with tab1:
    st.subheader("The Banking Meltdown (2023)")
    st.error("Loss: $180 Million in Minutes")
    st.markdown("""
    A major U.S. bank deployed an AI-generated trading algorithm. When market volatility spiked, the system failed catastrophically.
    
    **The Cause**: The AI code lacked basic error handling and didn't account for edge cases that any intermediate developer would catch.
    
    > *"The code looked perfect on paper, but it crumbled under real-world conditions."* — Lead Investigator
    """)

with tab2:
    st.subheader("The Healthcare Data Breach (2024)")
    st.error("Exposure: 2.3 Million Patient Records")
    st.markdown("""
    A healthcare startup's AI-generated API endpoints contained a critical security vulnerability (SQL Injection).
    
    **The Cause**: Developers didn't understand fundamental security concepts like input validation.
    """)

with tab3:
    st.subheader("The Startup Graveyard")
    st.error("Failure Rate: 92% in 2024")
    st.markdown("""
    **34%** of failures cited "technical incompetence" as a primary factor. 
    Many founders admitted they relied on AI tools to "get by", only to discover critical flaws in production.
    """)

# -----------------------------------------------------------------------------
# SECTION 5: The Psychological Trap
# -----------------------------------------------------------------------------
st.header("The Psychological Trap: Dunning-Kruger in Code")
st.markdown("""
AI creates a dangerous illusion of competence. A 2024 MIT study found that **AI-assisted developers overestimate their skills by an average of 47%.**

> *"I thought I was a solid developer because Copilot helped me write complex functions. Then I tried to optimize performance and realized I didn't understand how the code actually worked."* — Senior Engineer, Fortune 500
""")

# -----------------------------------------------------------------------------
# SECTION 6: The Path Forward (RAVEN)
# -----------------------------------------------------------------------------
st.header("The Path Forward: AI as Enabler, Not Crutch")
st.markdown("""
**RAVEN Approach**: WHAT / HOW / WHY methodology.
Instead of generating code in a vacuum, AI should teach while it assists.
""")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### The Hybrid Developer Model")
    st.markdown("""
    1. Master fundamentals through deliberate practice
    2. Use AI as an accelerator, not a replacement
    3. Understand when to override AI
    4. Debug without constant AI assistance
    """)

with col2:
    st.markdown("### Success Metrics with Educational AI")
    # Horizontal bar for success metrics
    success_data = {
        'Metric': ['Developer Confidence', 'Skill Improvement', 'Reduction in Production Bugs'],
        'Percentage': [89, 73, 58]
    }
    df_success = pd.DataFrame(success_data)
    fig_success = px.bar(df_success, x='Percentage', y='Metric', orientation='h',
                         title='Impact of Educational AI Tools',
                         text='Percentage', color='Metric',
                         color_discrete_sequence=px.colors.qualitative.Prism)
    fig_success.update_traces(texttemplate='%{text}%', textposition='inside')
    st.plotly_chart(fig_success, use_container_width=True)

st.markdown("---")
st.subheader("Call to Action")
st.markdown("""
**AI should enable mastery, not create dependency.**
The choice is ours. The future of software depends on it.
""")
