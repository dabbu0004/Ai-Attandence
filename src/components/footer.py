import streamlit as st


def footer_home():
    logo_url = "/Logo.webp"
    
    st.markdown(f"""
        <div class="snap-footer snap-footer-dark">
        <p>Created with care by</p>
        <img src='{logo_url}' alt='Himanshu' />
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "/Logo.webp"
    
    st.markdown(f"""
        <div class="snap-footer">
        <p>Created with care by</p>
        <img src='{logo_url}' alt='Himanshu' />
        </div>
    """, unsafe_allow_html=True)
