import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time

from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.markdown(f'<p class="snap-eyebrow dashboard-eyebrow">STUDENT WORKSPACE</p><h3 class="dashboard-welcome">Welcome back, {student_data["name"]}</h3>', unsafe_allow_html=True)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data 
            st.rerun()

    st.space()

    c1, c2 =st.columns(2)
    with c1:
        st.header('Your enrolled subjects')
    with c2:
        if st.button('Enroll in a subject', type='primary', width='stretch', icon=':material/add:'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total":0, "attended": 0}

        stats_map[sid]['total'] +=1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    total_sessions = len(logs)
    attended_sessions = sum(1 for log in logs if log.get('is_present'))
    attendance_rate = round((attended_sessions / total_sessions) * 100) if total_sessions else 0
    st.markdown(f"""
        <div class="dashboard-metrics">
            <div class="metric-card"><strong>{len(subjects)}</strong><span>Enrolled subjects</span></div>
            <div class="metric-card"><strong>{attended_sessions}</strong><span>Sessions attended</span></div>
            <div class="metric-card"><strong>{attendance_rate}%</strong><span>Overall attendance</span></div>
        </div>
    """, unsafe_allow_html=True)

    cols = st.columns(2)
    if not subjects:
        st.markdown("""
            <div class="empty-state">
                <strong>Your learning space is ready.</strong>
                Join your first subject using the code shared by your teacher.
            </div>
        """, unsafe_allow_html=True)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']

        stats = stats_map.get(sid,{"total":0, "attended": 0} )
        def unenroll_button():
                if st.button("Leave subject", type='tertiary', width='stretch', icon=':material/delete_forever:'):
                    unenroll_student_to_subject(student_id, sid)
                    st.toast(f"Unenrolled from {sub['name']} successfully!")
                    st.rerun()

        with cols[i % 2]:
            subject_card(
                name = sub['name'],
                code =sub['subject_code'],
                section = sub['section'],
                stats = [
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=unenroll_button
            )
    footer_dashboard()

def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return
    
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.markdown("""
        <div class="auth-hero">
            <p class="snap-eyebrow">STUDENT ACCESS</p>
            <h2>Pick up where you left off.</h2>
            <p>Position your face in the frame and let Ai-Attendance verify you securely.</p>
        </div>
    """, unsafe_allow_html=True)
    
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        if "last_photo" not in st.session_state or st.session_state.last_photo != photo_source.getvalue():
            st.session_state.last_photo = photo_source.getvalue()
            img = np.array(Image.open(photo_source))
            
            with st.spinner('AI is scanning..'):
                detected, all_ids, num_faces = predict_attendance(img)
                st.session_state.scan_results = (detected, num_faces)
        
        detected, num_faces = st.session_state.scan_results

        if num_faces == 0:
            st.warning('Face not found!')
            st.session_state.show_registration = False
        elif num_faces > 1:
            st.warning('Multiple faces found')
            st.session_state.show_registration = False
        else:
            if detected:
                student_id = list(detected.keys())[0]
                all_students = get_all_students()
                student = next((s for s in all_students if s['student_id']==student_id), None)

                if student:
                    st.session_state.is_logged_in = True
                    st.session_state.user_role = 'student'
                    st.session_state.student_data = student
                    st.toast(f"Welcome Back {student['name']}")
                    time.sleep(1)
                    st.rerun()
            else:
                st.info('Face not recognized! You might be a new student!')
                st.session_state.show_registration = True

    if st.session_state.get('show_registration', False):
        with st.container(border=True):
            st.markdown('<p class="snap-eyebrow">NEW PROFILE</p>', unsafe_allow_html=True)
            st.header('Create your student profile')
            new_name = st.text_input("Enter your name", placeholder='E.g. Robert Downey Jr.')

            st.subheader('Optional voice enrollment')
            st.info("Add a short voice sample to enable voice-only attendance later.")

            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like I am present, My name is Akash.')
            except Exception:
                st.error('Audio Data failed!')

            if st.button('Create Account', type='primary'):
                if new_name:
                    with st.spinner('Creating profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings= get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Couldnt capture your facial features for registration')

                else:
                    st.warning('Please enter your name!')

    footer_dashboard()