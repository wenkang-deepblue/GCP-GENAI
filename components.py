import streamlit as st

def save_invite_code():
    """保存URL中的邀请码到会话状态"""
    # 获取URL中的邀请码
    invite_code = st.query_params.get("invite_code", "")
    
    # 如果URL中有邀请码，则保存到session_state
    if invite_code and "invite_code" not in st.session_state:
        st.session_state.invite_code = invite_code
    
    # 如果URL中没有邀请码但session_state中有，使用session_state中的值
    elif not invite_code and "invite_code" in st.session_state:
        invite_code = st.session_state.invite_code

def english_version_link():
    """在侧边栏顶部添加英文版链接，自动传递邀请码"""
    # 先保存邀请码到会话状态
    save_invite_code()
    
    # 从会话状态获取邀请码
    invite_code = st.session_state.get("invite_code", "")
    
    # 构建带邀请码的英文版链接
    english_version_url = f"https://gcp-genai-en.streamlit.app/?invite_code={invite_code}" if invite_code else "https://gcp-genai-en.streamlit.app/"
    
    # 返回HTML标记
    return f"""
        <div style="text-align: center; margin-bottom: 15px;">
            <a href="{english_version_url}" target="_blank" style="color: #4285F4; text-decoration: underline; font-weight: bold; font-family: 'Google Sans', sans-serif;">
                English Version
            </a>
        </div>
    """ 