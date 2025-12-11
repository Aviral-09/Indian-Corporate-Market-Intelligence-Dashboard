import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

# --- Page Config ---
st.set_page_config(
    page_title="Fresher Market Intelligence 2025",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom Styling (Reference Image Matching) ---
st.markdown("""
    <style>
    /* Import Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global */
    * {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Background - Dark Navy with Gradient Globs */
    .stApp {
        background-color: #050511; /* Very dark navy/black */
        background-image: 
            radial-gradient(circle at 10% 10%, rgba(124, 58, 237, 0.15) 0%, transparent 40%),
            radial-gradient(circle at 90% 90%, rgba(59, 130, 246, 0.15) 0%, transparent 40%),
            radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.05) 0%, transparent 50%);
        background-attachment: fixed;
    }

    /* Card Containers (KPIs & Charts) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(8px);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    
    /* KPI Specifics */
    .kpi-title {
        color: #9CA3AF;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 5px;
    }
    .kpi-value {
        color: #FFFFFF;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .kpi-sub {
        font-size: 13px;
        color: #34D399; /* Green for growth */
        display: flex;
        align-items: center;
        gap: 5px;
    }
    .kpi-icon {
        float: right;
        background: rgba(255,255,255,0.05);
        padding: 8px;
        border-radius: 8px;
        color: #8B5CF6;
    }

    /* Chart Titles inside Cards */
    .chart-header {
        color: #E2E8F0;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 15px;
    }

    /* Predictor Section (Bottom) */
    .predictor-container {
        background: linear-gradient(180deg, rgba(30, 30, 50, 0.6) 0%, rgba(20, 20, 30, 0.8) 100%);
        border: 1px solid rgba(139, 92, 246, 0.3); /* Purple accent border */
        border-radius: 16px;
        padding: 24px;
        margin-top: 10px;
    }
    
    /* Input Styling */
    .stSelectbox label, .stTextInput label, .stSlider label {
        color: #9CA3AF !important;
    }
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 10px !important;
    }

    /* Plotly specifics to remove whitespace */
    .js-plotly-plot .plotly .modebar {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- Data Logic ---
@st.cache_data
def load_data():
    file_path = "archive (4)/companies.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        # Fallback to absolute path if relative fails
        abs_path = r"c:\Users\aviral\Desktop\data analyst\Indian companies\archive (4)\companies.csv"
        if os.path.exists(abs_path):
            df = pd.read_csv(abs_path)
        else:
            return pd.DataFrame() # Return empty if totally not found

    # --- Data Cleaning helper ---
    def clean_metric(value):
        if isinstance(value, str):
            value = str(value).lower().replace(',', '').strip()
            try:
                if 'l' in value:
                    return float(value.replace('l', '')) * 100000
                elif 'k' in value:
                    return float(value.replace('k', '')) * 1000
                return float(value)
            except ValueError:
                return 0.0
        return float(value) if value else 0.0

    # Apply cleaning to specific columns
    for col in ['reviews', 'salaries', 'interviews', 'jobs']:
        if col in df.columns:
            df[col] = df[col].apply(clean_metric)
            
    if 'rating' in df.columns:
        df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    
    # Fill NAs instead of dropping to show ALL companies
    df = df.fillna(0)
    # Ensure names are strings and handle duplicates
    df['name'] = df['name'].astype(str)
    df = df.drop_duplicates(subset=['name'])
        
    return df

# --- Layout ---
def main():
    df = load_data()
    
    if df.empty:
        st.error("⚠️ Data not found. Please ensure 'companies.csv' is in 'archive (4)' folder.")
        st.stop()

    # --- Main Title ---
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 30px; font-weight: 700;'>Indian Corporate Market Intelligence</h1>", unsafe_allow_html=True)

    # --- Top Header & Filtering ---
    with st.container():
        st.markdown('<div class="glass-card" style="padding: 15px;">', unsafe_allow_html=True)
        # Filters for Company Dashboard
        f1, f2, f3 = st.columns([2, 2, 1])
        with f1:
            # Filter by Rating (Default 0 to show ALL)
            min_rating = st.slider("Filter by Rating", 0.0, 5.0, 0.0, 0.1)
        with f2:
            # Search by Name (Multiselect to show list)
            all_companies = sorted(df['name'].unique())
            selected_companies = st.multiselect("Select Companies", all_companies, placeholder="Search or Select...")
        with f3:
            st.markdown(f"<div style='text-align:right; color: #6B7280; font-size: 12px; padding-top: 35px;'>Showing {len(df)} Companies</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Apply Filters
    filtered_df = df[df['rating'] >= min_rating]
    if selected_companies:
        filtered_df = filtered_df[filtered_df['name'].isin(selected_companies)]

    # --- Main Canvas ---
    
    # Row 1: KPI Cards
    kpi1, kpi2, kpi3 = st.columns(3)
    
    avg_rating = filtered_df['rating'].mean()
    total_jobs = filtered_df['jobs'].sum()
    total_reviews = filtered_df['reviews'].sum()
    
    with kpi1:
        st.markdown(f"""
        <div class="glass-card">
            <div class="kpi-icon">⭐</div>
            <div class="kpi-title">Average Rating</div>
            <div class="kpi-value">{avg_rating:.1f} / 5.0</div>
            <div class="kpi-sub" style="color: #6B7280;">Across selected companies</div>
        </div>
        """, unsafe_allow_html=True)

    with kpi2:
        st.markdown(f"""
        <div class="glass-card">
            <div class="kpi-icon">📢</div>
            <div class="kpi-title">Total Job Openings</div>
            <div class="kpi-value">{total_jobs:,.0f}</div>
            <div class="kpi-sub" style="color: #34D399;">Active Opportunities</div>
        </div>
        """, unsafe_allow_html=True)

    with kpi3:
        st.markdown(f"""
        <div class="glass-card">
            <div class="kpi-icon">💬</div>
            <div class="kpi-title">Total Reviews</div>
            <div class="kpi-value">{total_reviews:,.0f}</div>
            <div class="kpi-sub" style="color: #6B7280;">Employee Feedback</div>
        </div>
        """, unsafe_allow_html=True)

    # --- Charts Section ---
    
    # Row 2: Top Lists (Ratings & Jobs)
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-header">🏆 Top 8 Rated Companies</div>', unsafe_allow_html=True)
        top_rated = filtered_df.sort_values('rating', ascending=False).head(8)
        if not top_rated.empty:
            fig_bar = go.Figure(data=[go.Bar(
                x=top_rated['rating'], y=top_rated['name'], orientation='h',
                marker=dict(color=top_rated['rating'], colorscale=[[0, '#7C3AED'], [1, '#2DD4BF']], showscale=False)
            )])
            fig_bar.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#9CA3AF'), margin=dict(l=0, r=0, t=0, b=0), height=320,
                xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)'),
                yaxis=dict(showgrid=False, autorange="reversed"), bargap=0.4
            )
            st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("No data")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-header">🚀 Most Active Hiring (Top 8)</div>', unsafe_allow_html=True)
        most_jobs = filtered_df.sort_values('jobs', ascending=False).head(8)
        if not most_jobs.empty:
            fig_jobs = go.Figure(data=[go.Bar(
                x=most_jobs['name'], y=most_jobs['jobs'],
                marker=dict(color=most_jobs['jobs'], colorscale='Magma', showscale=False)
            )])
            fig_jobs.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#9CA3AF'), margin=dict(l=0, r=0, t=0, b=0), height=320,
                xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)')
            )
            st.plotly_chart(fig_jobs, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("No data")
        st.markdown('</div>', unsafe_allow_html=True)

    # Row 3: Distribution & Reviews
    c3, c4 = st.columns(2)
    
    with c3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-header">📊 Rating Distribution</div>', unsafe_allow_html=True)
        if not filtered_df.empty:
            fig_hist = px.histogram(filtered_df, x="rating", nbins=20, 
                                  color_discrete_sequence=['#8B5CF6'])
            fig_hist.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#9CA3AF'), margin=dict(l=0, r=0, t=0, b=0), height=320,
                xaxis=dict(showgrid=False, title="Rating"), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Count"),
                showlegend=False
            )
            st.plotly_chart(fig_hist, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("No data")
        st.markdown('</div>', unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-header">� Most Reviewed Companies (Top 8)</div>', unsafe_allow_html=True)
        top_reviews = filtered_df.sort_values('reviews', ascending=False).head(8)
        if not top_reviews.empty:
            fig_rev = go.Figure(data=[go.Bar(
                x=top_reviews['reviews'], y=top_reviews['name'], orientation='h',
                marker=dict(color=top_reviews['reviews'], colorscale='Viridis', showscale=False)
            )])
            fig_rev.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#9CA3AF'), margin=dict(l=0, r=0, t=0, b=0), height=320,
                xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)'), 
                yaxis=dict(showgrid=False, autorange="reversed"),
                bargap=0.4
            )
            st.plotly_chart(fig_rev, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("No data")
        st.markdown('</div>', unsafe_allow_html=True)

    # Row 4: Interviews & Salaries
    c5, c6 = st.columns(2)
    
    with c5:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-header">🗣️ Most Interviews Reported (Top 8)</div>', unsafe_allow_html=True)
        top_interviews = filtered_df.sort_values('interviews', ascending=False).head(8)
        if not top_interviews.empty:
            fig_int = go.Figure(data=[go.Bar(
                x=top_interviews['interviews'], y=top_interviews['name'], orientation='h',
                marker=dict(color=top_interviews['interviews'], colorscale='Plasma', showscale=False)
            )])
            fig_int.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#9CA3AF'), margin=dict(l=0, r=0, t=0, b=0), height=320,
                xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)'),
                yaxis=dict(showgrid=False, autorange="reversed")
            )
            st.plotly_chart(fig_int, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("No data")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c6:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-header">� Most Salary Data Points (Top 8)</div>', unsafe_allow_html=True)
        top_salaries = filtered_df.sort_values('salaries', ascending=False).head(8)
        if not top_salaries.empty:
            fig_sal = go.Figure(data=[go.Bar(
                x=top_salaries['salaries'], y=top_salaries['name'], orientation='h',
                marker=dict(color=top_salaries['salaries'], colorscale='Inferno', showscale=False)
            )])
            fig_sal.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#9CA3AF'), margin=dict(l=0, r=0, t=0, b=0), height=320,
                xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)'),
                yaxis=dict(showgrid=False, autorange="reversed")
            )
            st.plotly_chart(fig_sal, use_container_width=True, config={'displayModeBar': False})
        else:
            st.info("No data")
        st.markdown('</div>', unsafe_allow_html=True)

    # Row 3: Company Explorer (Replaces Predictor)
    st.markdown('<div class="header-text" style="color: #60A5FA; font-weight: 600; margin-bottom: 10px;">Full Company Database</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="predictor-container">', unsafe_allow_html=True)
        
        # Comprehensive Data Grid
        st.dataframe(
            filtered_df[['name', 'rating', 'reviews', 'salaries', 'interviews', 'jobs']].sort_values('rating', ascending=False),
            use_container_width=True,
            column_config={
                "rating": st.column_config.ProgressColumn("Rating", min_value=0, max_value=5, format="%.1f"),
                "jobs": st.column_config.NumberColumn("Open Jobs", format="%d"),
                "reviews": st.column_config.NumberColumn("Reviews", format="%d"),
                "salaries": st.column_config.NumberColumn("Salaries Reported", format="%d"),
                "interviews": st.column_config.NumberColumn("Interviews", format="%d"),
            },
            hide_index=True
        )
            
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
