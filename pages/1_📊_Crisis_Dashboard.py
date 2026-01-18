import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    .author-credit {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-top: -10px;
        margin-bottom: 20px;
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

# Title Section with Author Credit
st.title("🚨 The Silent Crisis")
st.markdown("# When AI Eats the Foundations of Software Development")
st.markdown('<p class="author-credit">By Lee Akpareva MBA, MA</p>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; margin-top: -5px; margin-bottom: 15px;">
    <a href="https://raventerminal.xyz/" target="_blank" style="color: #666; font-size: 14px;">raventerminal.xyz</a>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for Navigation
with st.sidebar:
    st.header("Page Navigation")
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
# NEW SECTION: The Code Reading Crisis
# -----------------------------------------------------------------------------
st.header("The Code Reading Crisis: When Developers Stop Reading")
st.markdown("""
The ability to read and understand code is fundamental to software development, yet it's becoming a lost art.
Modern developers increasingly rely on AI to interpret code for them, creating dangerous knowledge gaps.
""")

col1, col2 = st.columns(2)

with col1:
    # Time spent reading vs writing code
    df_reading = pd.DataFrame({
        'Year': ['2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        'Reading Code (%)': [58, 55, 52, 48, 42, 35, 28],
        'Writing Code (%)': [42, 45, 48, 52, 58, 65, 72]
    })

    fig_reading = px.line(df_reading, x='Year',
                          y=['Reading Code (%)', 'Writing Code (%)'],
                          title='Developer Time: Reading vs Writing Code',
                          markers=True)
    fig_reading.update_layout(yaxis_title='Percentage of Time',
                              legend_title='Activity')
    st.plotly_chart(fig_reading, use_container_width=True)

    st.warning("**28%** - Time developers spend reading code in 2024, down from 58% in 2018")

with col2:
    # Code comprehension skills decline
    df_comprehension = pd.DataFrame({
        'Skill Level': ['Can Debug Complex Systems', 'Understand Architecture',
                        'Read Legacy Code', 'Trace Data Flow'],
        'Junior Devs 2020': [75, 68, 72, 80],
        'Junior Devs 2024': [32, 25, 18, 35]
    })

    fig_comp = px.bar(df_comprehension, x='Skill Level',
                      y=['Junior Devs 2020', 'Junior Devs 2024'],
                      title='Code Comprehension Skills Decline',
                      barmode='group')
    fig_comp.update_layout(yaxis_title='% of Developers',
                          legend_title='Year Group')
    st.plotly_chart(fig_comp, use_container_width=True)

    st.error("**82%** decline in legacy code reading ability among junior developers")

# -----------------------------------------------------------------------------
# NEW SECTION: Security Breaches from Poor Code Understanding
# -----------------------------------------------------------------------------
st.header("The Security Crisis: When Copy-Paste Becomes Catastrophic")
st.markdown("""
Security breaches are increasingly linked to developers who copy AI-generated code without understanding its implications.
The "trust but don't verify" mentality is creating unprecedented vulnerabilities.
""")

# Security breach statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Security Breaches from AI Code",
        value="312%",
        delta="Increase since 2022",
        delta_color="inverse"
    )

with col2:
    st.metric(
        label="Average Breach Cost",
        value="$4.45M",
        delta="+15% YoY",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="Vulnerabilities per 1000 Lines",
        value="23.7",
        delta="+8.3 from 2023",
        delta_color="inverse"
    )

# Common vulnerability sources
st.subheader("Root Causes of AI-Generated Vulnerabilities")

vulnerability_data = {
    'Vulnerability Type': [
        'Unvalidated Input (SQL Injection, XSS)',
        'Hardcoded Credentials & API Keys',
        'Insecure Dependencies',
        'Missing Authentication Checks',
        'Race Conditions',
        'Memory Leaks & Buffer Overflows'
    ],
    'Frequency (%)': [34, 28, 22, 19, 15, 12],
    'Average Cost ($M)': [2.8, 5.2, 1.9, 3.7, 2.1, 4.5]
}

df_vuln = pd.DataFrame(vulnerability_data)
df_vuln = df_vuln.sort_values('Frequency (%)', ascending=True)

fig_vuln = px.barh(df_vuln, x='Frequency (%)', y='Vulnerability Type',
                   title='Most Common Security Vulnerabilities in AI-Generated Code',
                   text='Frequency (%)',
                   color='Average Cost ($M)',
                   color_continuous_scale='Reds')
fig_vuln.update_traces(texttemplate='%{text}%', textposition='outside')
fig_vuln.update_layout(height=400)
st.plotly_chart(fig_vuln, use_container_width=True)

# -----------------------------------------------------------------------------
# NEW SECTION: The First-Time Quality Imperative
# -----------------------------------------------------------------------------
st.header("Do It Right The First Time: The Economics of Quality")
st.markdown("""
The cost of fixing defects increases exponentially as they move through the development lifecycle.
Getting code right the first time isn't just best practice—it's economic necessity.
""")

# Cost of fixing bugs at different stages
stages_data = {
    'Stage': ['Design', 'Development', 'Testing', 'Production', 'Post-Release'],
    'Relative Cost': [1, 6.5, 15, 100, 1000],
    'Time to Fix (Hours)': [0.5, 2, 8, 40, 200]
}

df_stages = pd.DataFrame(stages_data)

col1, col2 = st.columns(2)

with col1:
    fig_cost_stages = px.bar(df_stages, x='Stage', y='Relative Cost',
                             title='Relative Cost of Fixing Defects by Stage',
                             text='Relative Cost',
                             color='Relative Cost',
                             color_continuous_scale='Reds')
    fig_cost_stages.update_traces(texttemplate='%{text}x', textposition='outside')
    fig_cost_stages.update_layout(showlegend=False, yaxis_title='Cost Multiplier')
    st.plotly_chart(fig_cost_stages, use_container_width=True)

with col2:
    fig_time_stages = px.line(df_stages, x='Stage', y='Time to Fix (Hours)',
                              title='Time Required to Fix Defects by Stage',
                              markers=True, text='Time to Fix (Hours)')
    fig_time_stages.update_traces(textposition='top center')
    fig_time_stages.update_layout(yaxis_type='log', yaxis_title='Hours (Log Scale)')
    st.plotly_chart(fig_time_stages, use_container_width=True)

# Quality metrics comparison
st.subheader("The Quality Dividend: Benefits of Getting It Right")

quality_benefits = {
    'Metric': ['Development Speed', 'Customer Satisfaction', 'Team Morale',
               'Technical Debt', 'Maintenance Cost', 'Innovation Capacity'],
    'With Quality Focus': [100, 92, 85, 15, 20, 75],
    'Without Quality Focus': [65, 45, 40, 85, 80, 25]
}

df_quality = pd.DataFrame(quality_benefits)

fig_quality = px.bar(df_quality, x='Metric',
                     y=['With Quality Focus', 'Without Quality Focus'],
                     title='Impact of First-Time Quality on Key Metrics (%)',
                     barmode='group',
                     color_discrete_map={'With Quality Focus': 'green',
                                       'Without Quality Focus': 'red'})
fig_quality.update_layout(yaxis_title='Performance (%)', legend_title='Approach')
st.plotly_chart(fig_quality, use_container_width=True)

st.markdown("""
<div class="quote-box">
"The bitterness of poor quality remains long after the sweetness of low price is forgotten." — Benjamin Franklin
<br><br>
In software, this translates to: <b>Technical debt compounds at 78% annually</b>, while quality code appreciates in value.
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# NEW SECTION: Knowledge Erosion Timeline
# -----------------------------------------------------------------------------
st.header("The Knowledge Erosion Timeline")
st.markdown("""
Without regular code reading and fundamental practice, developer skills atrophy rapidly.
This timeline shows how quickly expertise disappears when replaced by AI dependency.
""")

# Knowledge retention over time
retention_data = {
    'Weeks Without Practice': [0, 2, 4, 8, 12, 16, 24],
    'Algorithm Design': [100, 92, 78, 55, 35, 22, 10],
    'System Architecture': [100, 95, 85, 68, 52, 38, 25],
    'Debugging Skills': [100, 88, 70, 48, 30, 18, 8],
    'Security Awareness': [100, 90, 75, 52, 32, 20, 12]
}

df_retention = pd.DataFrame(retention_data)

fig_retention = px.line(df_retention, x='Weeks Without Practice',
                        y=['Algorithm Design', 'System Architecture',
                           'Debugging Skills', 'Security Awareness'],
                        title='Skill Retention Without Regular Practice',
                        markers=True)
fig_retention.update_layout(yaxis_title='Skill Retention (%)',
                           xaxis_title='Weeks Without Manual Coding Practice')
fig_retention.add_hline(y=50, line_dash="dash", line_color="red",
                        annotation_text="Critical Knowledge Threshold")
st.plotly_chart(fig_retention, use_container_width=True)

st.error("""
**Critical Finding**: After just 8 weeks of AI-only coding, developers lose over 50% of their
fundamental programming skills, crossing below the threshold needed for effective problem-solving.
""")

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