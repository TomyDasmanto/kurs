import streamlit as st
import yfinance as yf
import time

st.set_page_config(page_title="USD/IDR Real-Time", layout="centered")

st.title("💱 Kurs USD/IDR Real-Time")

# Placeholder untuk update data
placeholder = st.empty()

# Looping untuk refresh data setiap 60 detik
while True:
    ticker = yf.Ticker("USDIDR=X")
    data = ticker.fast_info
    
    current_price = data['lastPrice']
    prev_close = data['previousClose']
    change = current_price - prev_close
    pct_change = (change / prev_close) * 100
    
    with placeholder.container():
        st.metric(
            label="USD ke IDR", 
            value=f"Rp {current_price:,.2f}", 
            delta=f"{change:+.2f} ({pct_change:+.2f}%)"
        )
        st.caption(f"Update terakhir: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    time.sleep(60)
