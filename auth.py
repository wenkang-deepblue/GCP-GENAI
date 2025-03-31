import streamlit as st
import os
from components import save_invite_code

INVITE_CODES = st.secrets["INVITE_CODES"]

def login():
    if "logged_in" not in st.session_state:
        save_invite_code()
        
        # 从会话状态获取邀请码
        auto_invite_code = st.session_state.get("invite_code", "")
        
        # 如果有有效邀请码，自动登录
        if auto_invite_code in INVITE_CODES:
            st.session_state.logged_in = True
            st.session_state.user_email = "invited_user@example.com"
            st.experimental_rerun()

        background_image_url = "https://storage.googleapis.com/ghackathon/nebula_1_2.jpg"
        background_style = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap');
        .stApp {{
            background-image: url('{background_image_url}');
            background-size: cover;
            background-repeat: center center;
            background-attachment: fixed;
        }}
        .welcome-text {{
            font-family: 'Google Sans', sans-serif;
            font-weight: 500;
            color: white;
            font-size: 48px;
            text-align: center;
            margin-bottom: 30px;
        }}
        .chinese-version-link {{
            position: fixed;
            top: 80px;
            right: 10px;
            z-index: 1000;
        }}
        .chinese-version-link a {{
            font-family: 'Google Sans', sans-serif;
            color: white;
            text-decoration: none;
            font-size: 25px;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 10px 20px;
            border-radius: 10px;
            text-decoration: underline;
            text-decoration-color: white;
        }}
        </style>
        """
        st.markdown(background_style, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="welcome-text-container">
            <h1 class="welcome-text">Welcome to GCP-GenAI Project</h1>
        </div>
        """, unsafe_allow_html=True)
        st.text("")
        st.text("")
        st.text("")
        chinese_version_html = """
        <div class="chinese-version-link">
            <a href="https://gcp-genai-zh.streamlit.app/" target="_blank">中文版</a>
        </div>
        """
        st.markdown(chinese_version_html, unsafe_allow_html=True)
        
        # Create invite code input and login button
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            invite_code = st.text_input("Please Enter Your Invite Code", placeholder="Please Enter Your Invite Code", type="password")
            
            # Custom login button
            button_gif_url = "https://storage.googleapis.com/ghackathon/blue-gold.gif"
            
            st.markdown(
                f"""
                <style>
                    div.stButton > button {{
                        background-color: white;
                        color: #3c4043;
                        border: 1px solid #dadce0;
                        width: 100px;
                        padding: 6px 10px;
                        height: 32px;
                        border-radius: 5px;
                        font-weight: 500;
                        font-family: 'Google Sans', sans-serif;
                        position: relative;
                        overflow: hidden;
                        transition: transform 0.3s ease;
                        outline: none;
                        margin-left: 110px;
                    }}
                    
                    div.stButton > button:focus,
                    div.stButton > button:active,
                    div.stButton > button:hover,
                    div.stButton > button:focus-visible {{
                        outline: none !important;
                        box-shadow: none !important;
                        border-color: #dadce0 !important;
                    }}
                    
                    div.stButton > button:hover {{
                        transform: scale(1.05);
                        color: white;
                        background-image: url('{button_gif_url}');
                        background-size: cover;
                        background-position: center;
                    }}
                    
                    div.stButton {{
                        align-items: center;
                        margin-top: 10px;
                    }}
                                        
                    div[data-baseweb="notification"] {{
                        background-color: white !important;
                        border-left-color: #ff4b4b !important;
                        border-left-width: 4px !important;
                        color: #ff4b4b !important;
                        border-radius: 4px !important;
                        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2) !important;
                        text-align: center;
                    }}
                    
                    div[data-baseweb="notification"] p {{
                        color: #ff4b4b !important;
                        font-weight: 500 !important;
                    }}
                    
                    div[data-baseweb="notification"] svg {{
                        fill: #ff4b4b !important;
                    }}
                </style>
                """,
                unsafe_allow_html=True
            )
            
            btn_col1, btn_col2, btn_col3 = st.columns([1, 5, 1])
            with btn_col2:
                if st.button("Login"):
                    if invite_code in INVITE_CODES:
                        st.session_state.logged_in = True
                        st.session_state.user_email = "invited_user@example.com"
                        st.session_state.invite_code = invite_code
                        st.experimental_rerun()
                    else:
                        st.error("Invalid invite code, please try again")
        
        footer_html = f"""
        <style>
        .footer-links {{
            position: fixed;
            left: 0;
            bottom: 10px;
            width: 100%;
            text-align: center;
        }}
        .footer-links a {{
            color: white;
            text-decoration: underline;
        }}
        .policy-links {{
            margin-bottom: 10px;
        }}
        .copyright-text {{
            font-size: 14px;
            background-color: rgba(0, 0, 0, 0.5);
            display: inline-block;
            padding: 8px 15px;
            border-radius: 10px;
        }}
        </style>
        <div class="footer-links">
            <div class="policy-links">
                <a href="https://gcp-genai-zh.streamlit.app/terms_of_service" target="_blank">Terms of Service</a>
                &nbsp;&nbsp;&nbsp;&nbsp;
                <a href="https://gcp-genai-zh.streamlit.app/privacy_policy" target="_blank">Privacy Policy</a>
            </div>
            <div class="copyright-text">
                <p style="text-align: center; margin: 0;">
                <span style="color: white;">© LWK &nbsp;&nbsp;|&nbsp;&nbsp; </span>
                <span style="color: white;">Designed & Developed by</span>
                <a href="{st.secrets["developer_profile_link"]}" 
                style="color: #8AB4F8; text-decoration: underline; font-weight: bold;" target="_blank">{st.secrets["developer_name"]}</a>
                <span style="color: white;"> &nbsp;&nbsp;|&nbsp;&nbsp; Powered by </span>
                <img src="https://storage.googleapis.com/ghackathon/GoogleCloud_logo_36px.png" alt="Logo" style="height: 18px; vertical-align: middle; margin: 0 2px; transform: translateY(-1px);">
                <span style="color: white; font-weight: bold;">Vertex AI</span>
                </p>
            </div>
        </div>
        """
        st.markdown(footer_html, unsafe_allow_html=True)
        
        return False

    return True

def logout():
    if "logged_in" in st.session_state:
        del st.session_state.logged_in
    if "user_email" in st.session_state:
        del st.session_state.user_email
    st.experimental_rerun()
