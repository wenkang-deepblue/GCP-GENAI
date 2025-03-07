import streamlit as st

def english_version_link():
    # 获取当前URL中的邀请码
    invite_code = st.query_params.get("invite_code", "")
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