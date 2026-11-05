import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div class="snap-footer snap-footer-dark">
        <p>Created with care by</p>
        <img src='{logo_url}' alt='Apna College' />
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div class="snap-footer">
        <p>Created with care by</p>
        <img src='{logo_url}' alt='Apna College' />
        </div>
    """, unsafe_allow_html=True)
