import streamlit as st


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div class="snap-home-header">
            <img src='{logo_url}' alt='SnapClass logo' />
            <div>
                <p class="snap-kicker">AI-powered attendance</p>
                <h1>SNAP<span>CLASS</span></h1>
                <p class="snap-tagline">Attendance, made effortless.</p>
            </div>
        </div>   
    """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div class="snap-dashboard-header">
            <img src='{logo_url}' alt='SnapClass logo' />
            <div>
                <p class="snap-kicker">AI attendance platform</p>
                <h2>SNAP<span>CLASS</span></h2>
            </div>
        </div>   
    """, unsafe_allow_html=True)
