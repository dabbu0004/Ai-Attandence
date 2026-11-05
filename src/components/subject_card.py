import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div class="subject-card">
        <div class="subject-card-accent"></div>
        <h3>{name}</h3>
        <p class="subject-meta">Code <span class="subject-code">{code}</span><span class="subject-divider"></span>Section {section}</p>
        
        """
    
    if stats:
        html += """
        <div class="subject-stats">
        """
        for icon, label, value in stats:
            html += f'<div class="subject-stat"><span>{icon}</span><b>{value}</b><small>{label}</small></div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
