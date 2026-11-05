import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    st.markdown("""
        <div class="snap-home-intro">
            <p class="snap-eyebrow">WELCOME TO SNAPCLASS</p>
            <h2>Attendance that works<br><span>as hard as you do.</span></h2>
            <p>Join your classroom or manage every session from one focused workspace.</p>
        </div>
    """, unsafe_allow_html=True)


    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<p class="snap-card-label">FOR LEARNERS</p>', unsafe_allow_html=True)
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        st.subheader("Student portal")
        st.write("Mark your attendance with FaceID and keep track of every enrolled subject.")
        if st.button('Continue as student', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.markdown('<p class="snap-card-label">FOR EDUCATORS</p>', unsafe_allow_html=True)
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        st.subheader("Teacher portal")
        st.write("Run AI-powered attendance, share your subjects, and review class records.")
        if st.button('Continue as teacher', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()