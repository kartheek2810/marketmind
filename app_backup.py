import streamlit as st
import random

# --- Page Config ---
st.set_page_config(page_title="MarketMind", page_icon="📈", layout="wide")

# --- Header ---
st.title("📊 MarketMind - AI Market Trend Analysis")
st.markdown("Your AI-powered dashboard for analyzing stock market trends.")

# --- Sidebar ---
st.sidebar.header("🔎 Search Market Trends")
user_input = st.sidebar.text_input("Enter stock/company/sector:", "AI stocks")

if st.sidebar.button("Analyze"):
    st.session_state['query'] = user_input

# --- Main Dashboard ---
if 'query' in st.session_state:
    query = st.session_state['query']
    st.subheader(f"📌 Analysis for: **{query}**")

    # Dummy AI response (replace later with real model)
    fake_trends = [
        f"Growing investor interest in {query}",
        f"{query} shows volatility due to global events",
        f"{query} sector is predicted to grow in 2025",
        f"AI indicates bullish trend in {query}",
        f"Bearish signals in {query} short-term"
    ]
    st.success(random.choice(fake_trends))

    # Example chart
    st.line_chart([random.randint(50, 200) for _ in range(10)])

else:
    st.info("👈 Enter a stock/company/sector in the sidebar and click **Analyze** to start.")
