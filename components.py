import streamlit as st

def save_invite_code():
    """Save invite code from URL to session state"""
    # Get invite code from URL
    invite_code = st.query_params.get("invite_code", "")
    
    # If there is an invite code in the URL, save it to session_state
    if invite_code and "invite_code" not in st.session_state:
        st.session_state.invite_code = invite_code
    
    # If there is no invite code in the URL but there is one in session_state, use the value from session_state
    elif not invite_code and "invite_code" in st.session_state:
        invite_code = st.session_state.invite_code

def chinese_version_link():
    """Add Chinese version link at the top of the sidebar, automatically passing the invite code"""
    # First save the invite code to the session state
    save_invite_code()
    
    # Get invite code from session state
    invite_code = st.session_state.get("invite_code", "")
    
    # Construct Chinese version link with invite code
    chinese_version_url = f"https://gcp-genai-zh.streamlit.app/?invite_code={invite_code}" if invite_code else "https://gcp-genai-zh.streamlit.app/"
    
    # Return HTML markup
    return f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <a href="{chinese_version_url}" target="_blank" style="color: #4285F4; text-decoration: underline; font-weight: bold; font-family: 'Google Sans', sans-serif;">
                中文版
            </a>
        </div>
    """ 

def vibtitle_link():
    """在侧边栏顶部添加Vibtitle链接，自动传递邀请码"""
    # 先保存邀请码到会话状态
    save_invite_code()
    
    # 从会话状态获取邀请码
    invite_code = st.session_state.get("invite_code", "")
    
    # 构建带邀请码的Vibtitle链接
    vibtitle_url = f"https://vibtitle-en.deepblue.cc/?invite_code={invite_code}" if invite_code else "https://vibtitle-en.deepblue.cc"
    
    return st.page_link(vibtitle_url, label="Vibtitle - Video Subtitles Generator", icon="🎬")