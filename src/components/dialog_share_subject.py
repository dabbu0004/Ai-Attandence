import streamlit as st

import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "Ai-Attendence-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.markdown('<p class="snap-eyebrow">INVITE CLASSMATES</p>', unsafe_allow_html=True)
    st.header(f"Join {subject_name}")
    st.caption("Share the code or scan the QR to join this subject.")

    qr = segno.make(join_url)  # for make qr by segno

    out = io.BytesIO()

    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('#### Share details')
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info('Copy the link or subject code to share via WhatsApp or email.')

    with col2:
        st.markdown('#### Scan to join')
        st.image(out.getvalue(), caption='QRCODE for class joining')

        
