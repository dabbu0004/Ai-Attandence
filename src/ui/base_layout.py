import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background:
                    radial-gradient(circle at 15% 10%, rgba(45, 212, 191, .14), transparent 28rem),
                    radial-gradient(circle at 90% 85%, rgba(14, 165, 164, .12), transparent 24rem),
                    #0b1220 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background: rgba(255, 255, 255, .97) !important;
                padding: 2rem !important;
                border: 1px solid rgba(148, 163, 184, .18);
                border-radius: 1.25rem !important;
                box-shadow: 0 18px 45px rgba(2, 8, 23, .18);
                transition: transform .25s ease, box-shadow .25s ease;
            }

            .stApp div[data-testid="stColumn"]:hover {
                transform: translateY(-4px);
                box-shadow: 0 24px 55px rgba(2, 8, 23, .28);
            }
        </style>  
    """, unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background:
                    radial-gradient(circle at 100% 0%, rgba(20, 184, 166, .08), transparent 28rem),
                    #f3f6fa !important;
            }
        </style>
    """, unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                max-width: 1180px;
                padding-top: 2.25rem !important;
                padding-bottom: 3rem !important;
            }

            h1, h2 {
                font-family: 'Space Grotesk', sans-serif !important;
                color: #0f172a !important;
                letter-spacing: -.035em;
                line-height: 1.1 !important;
            }

            h1 {
                font-size: clamp(2.2rem, 5vw, 3.5rem) !important;
            }

            h2 {
                font-size: clamp(1.7rem, 3vw, 2.3rem) !important;
            }

            .snap-home-header {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 1.25rem;
                margin: 1rem 0 2.5rem;
                animation: fade-up .45s ease-out both;
            }

            .snap-home-header img {
                width: 92px;
                height: 92px;
                object-fit: contain;
            }

            .snap-home-header h1, .snap-home-header .snap-tagline {
                color: #f8fafc !important;
            }

            .snap-home-header h1 {
                margin: 0 !important;
                font-size: clamp(2.4rem, 7vw, 4.5rem) !important;
            }

            .snap-home-header h1 span, .snap-dashboard-header h2 span {
                color: #2dd4bf;
            }

            .snap-kicker {
                color: #14b8a6;
                font-size: .72rem;
                font-weight: 700;
                letter-spacing: .14em;
                margin: 0 0 .25rem;
                text-transform: uppercase;
            }

            .snap-tagline {
                font-size: .95rem;
                margin: .45rem 0 0;
                opacity: .8;
            }

            .snap-home-intro, .auth-hero, .section-hero {
                margin: 0 auto 2rem;
                max-width: 700px;
                text-align: center;
            }

            .snap-home-intro h2, .auth-hero h2, .section-hero h2 {
                margin: .35rem 0 .65rem !important;
            }

            .snap-home-intro h2 span {
                color: #14b8a6;
            }

            .snap-home-intro > p:last-child, .auth-hero > p:last-child, .section-hero > p:last-child {
                color: #64748b;
                font-size: 1rem;
                margin: 0;
            }

            .auth-hero {
                background: linear-gradient(135deg, rgba(255, 255, 255, .9), rgba(240, 253, 250, .88));
                border: 1px solid #dbe5ed;
                border-radius: 1.25rem;
                box-shadow: 0 12px 30px rgba(15, 23, 42, .06);
                padding: 1.5rem 1.75rem;
            }

            .snap-eyebrow, .snap-card-label {
                color: #0f766e;
                font-size: .72rem;
                font-weight: 700;
                letter-spacing: .14em;
                margin: 0;
                text-transform: uppercase;
            }

            .snap-card-label {
                margin-bottom: .35rem;
            }

            .dashboard-eyebrow {
                margin-bottom: .35rem;
            }

            .dashboard-welcome {
                color: #5683e9 !important;
                font-family: 'Space Grotesk', sans-serif;
                margin: 0 !important;
            }

            .section-heading {
                align-items: center;
            }

            .dashboard-metrics {
                display: grid;
                gap: .75rem;
                grid-template-columns: repeat(3, 1fr);
                margin: 1.5rem 0 2rem;
            }

            .metric-card {
                background: rgba(255, 255, 255, .86);
                border: 1px solid #e2e8f0;
                border-radius: .9rem;
                padding: 1rem 1.1rem;
            }

            .metric-card strong {
                color: #0f172a;
                display: block;
                font-family: 'Space Grotesk', sans-serif;
                font-size: 1.7rem;
                line-height: 1;
            }

            .metric-card span {
                color: #64748b;
                display: block;
                font-size: .75rem;
                margin-top: .45rem;
                text-transform: uppercase;
                letter-spacing: .08em;
            }

            .empty-state {
                background: linear-gradient(135deg, #f8fafc, #ecfeff);
                border: 1px dashed #99f6e4;
                border-radius: 1rem;
                color: #475569;
                padding: 2rem;
                text-align: center;
            }

            .empty-state strong {
                color: #0f172a;
                display: block;
                font-family: 'Space Grotesk', sans-serif;
                font-size: 1.1rem;
                margin-bottom: .35rem;
            }

            .workspace-tabs {
                background: rgba(255, 255, 255, .7);
                border: 1px solid #e2e8f0;
                border-radius: .9rem;
                padding: .5rem;
            }

            .snap-dashboard-header {
                align-items: center;
                display: flex;
                gap: .85rem;
                justify-content: center;
            }

            .snap-dashboard-header img {
                height: 64px;
                object-fit: contain;
                width: 64px;
            }

            .snap-dashboard-header h2 {
                margin: 0 !important;
            }

            .snap-dashboard-header .snap-kicker {
                color: #0f766e;
                margin-bottom: .15rem;
            }

            .snap-footer {
                align-items: center;
                color: #64748b;
                display: flex;
                gap: .45rem;
                justify-content: center;
                margin-top: 2.5rem;
            }

            .snap-footer p {
                font-size: .8rem;
                margin: 0;
            }

            .snap-footer img {
                max-height: 22px;
            }

            .snap-footer-dark {
                color: #cbd5e1;
            }

            .subject-card {
                background: #fff;
                border: 1px solid #e2e8f0;
                border-radius: 1rem;
                box-shadow: 0 8px 24px rgba(15, 23, 42, .06);
                margin-bottom: 1rem;
                overflow: hidden;
                padding: 1.35rem;
                position: relative;
                transition: border-color .2s ease, box-shadow .2s ease, transform .2s ease;
            }

            .subject-card:hover {
                border-color: #99f6e4;
                box-shadow: 0 14px 30px rgba(15, 23, 42, .1);
                transform: translateY(-3px);
            }

            .subject-card-accent {
                background: #14b8a6;
                height: 4px;
                left: 0;
                position: absolute;
                right: 0;
                top: 0;
            }

            .subject-card h3 {
                color: #0f172a;
                font-family: 'Space Grotesk', sans-serif;
                font-size: 1.25rem;
                margin: .2rem 0 .65rem;
            }

            .subject-meta {
                align-items: center;
                color: #64748b;
                display: flex;
                font-size: .85rem;
                gap: .45rem;
                margin: 0 0 1rem;
            }

            .subject-code {
                background: #ccfbf1;
                border-radius: .35rem;
                color: #0f766e;
                font-weight: 700;
                padding: .2rem .45rem;
            }

            .subject-divider {
                background: #cbd5e1;
                height: 1rem;
                width: 1px;
            }

            .subject-stats {
                display: flex;
                flex-wrap: wrap;
                gap: .55rem;
            }

            .subject-stat {
                align-items: center;
                background: #f8fafc;
                border: 1px solid #e2e8f0;
                border-radius: .55rem;
                display: flex;
                gap: .35rem;
                padding: .4rem .65rem;
            }

            .subject-stat b {
                color: #0f172a;
            }

            .subject-stat small {
                color: #64748b;
                font-size: .76rem;
            }

            h3, h4, p, label, input, textarea, button, [data-testid="stMarkdownContainer"] {
                font-family: 'DM Sans', sans-serif;
            }

            button {
                border-radius: .7rem !important;
                border: 1px solid transparent !important;
                font-weight: 600 !important;
                padding: .65rem 1rem !important;
                transition: transform .2s ease, box-shadow .2s ease, background .2s ease !important;
            }

            button[kind="primary"] {
                background: #0f766e !important;
                color: #fff !important;
                box-shadow: 0 7px 16px rgba(15, 118, 110, .2);
            }

            button[kind="secondary"] {
                background: #e2e8f0 !important;
                color: #1e293b !important;
                border-color: #cbd5e1 !important;
            }

            button[kind="tertiary"] {
                background: transparent !important;
                color: #475569 !important;
                border-color: #cbd5e1 !important;
            }

            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 18px rgba(15, 23, 42, .12) !important;
            }

            button[kind="primary"]:hover {
                background: #115e59 !important;
            }

            [data-testid="stTextInput"],
            [data-testid="stTextArea"],
            [data-testid="stNumberInput"],
            [data-testid="stSelectbox"],
            [data-testid="stDateInput"],
            [data-testid="stFileUploader"],
            [data-testid="stCameraInput"],
            [data-testid="stAudioInput"] {
                margin-bottom: .85rem;
            }

            [data-testid="stTextInput"] label,
            [data-testid="stTextArea"] label,
            [data-testid="stNumberInput"] label,
            [data-testid="stSelectbox"] label,
            [data-testid="stDateInput"] label,
            [data-testid="stFileUploader"] label,
            [data-testid="stCameraInput"] label,
            [data-testid="stAudioInput"] label {
                color: #334155 !important;
                font-weight: 600 !important;
            }

            div[data-baseweb="input"], div[data-baseweb="base-input"] {
                background-color: #fff !important;
                border-radius: .65rem !important;
                border: 1px solid #cbd5e1 !important;
            }

            input, textarea, [data-baseweb="select"] input {
                color: #0f172a !important;
                -webkit-text-fill-color: #0f172a !important;
               background-color: #ffffff !important;
            }

            input::placeholder, textarea::placeholder {
                color: #64748b !important;
                -webkit-text-fill-color: #64748b !important;
            }

            [data-testid="stFileUploaderDropzone"] {
            border-radius: .65rem !important;
            border-color: #cbd5e1 !important;
            background: #fff !important;
            color: #0f172a !important;
            }

            [data-testid="stFileUploaderDropzone"] small,
            [data-testid="stFileUploaderDropzone"] span {
                color: #475569 !important;
            }

            input:focus, textarea:focus, [data-baseweb="select"] > div:focus-within {
                border-color: #14b8a6 !important;
                box-shadow: 0 0 0 3px rgba(20, 184, 166, .14) !important;
            }

            [data-testid="stAlert"], [data-testid="stExpander"] {
                border-radius: .75rem !important;
            }

            [data-testid="stDialog"] {
                border-radius: 1rem !important;
                box-shadow: 0 25px 70px rgba(15, 23, 42, .25) !important;
                animation: dialog-in .22s ease-out;
            }

            [data-testid="stImage"] img {
                border-radius: .75rem;
            }

            [data-testid="stSpinner"] {
                color: #0f766e !important;
            }

            @keyframes dialog-in {
                from { opacity: 0; transform: translateY(10px) scale(.98); }
                to { opacity: 1; transform: translateY(0) scale(1); }
            }

            @keyframes fade-up {
                from { opacity: 0; transform: translateY(12px); }
                to { opacity: 1; transform: translateY(0); }
            }

            @media (prefers-reduced-motion: reduce) {
                *, *::before, *::after {
                    animation-duration: .01ms !important;
                    transition-duration: .01ms !important;
                }

            }

            @media (max-width: 700px) {
                .dashboard-metrics {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    """, unsafe_allow_html=True)