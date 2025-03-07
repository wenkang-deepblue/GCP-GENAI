import streamlit as st
import streamlit.components.v1 as components
from auth import login, logout
from components import english_version_link, save_invite_code

st.set_page_config(
    page_title="GCP GenAI",
    page_icon="👋",
)

save_invite_code()

if not login():
    st.stop()

with st.sidebar:
    st.markdown(english_version_link(), unsafe_allow_html=True)
    st.markdown(f"""
        <div style="background-color: #d4edda; border-color: #c3e6cb; color: #155724; 
                    padding: 10px; border-radius: 0.25rem; text-align: center; margin-bottom: 10px;">
            <p style="margin-bottom: 0;">欢迎!</p>
        </div>
    """, unsafe_allow_html=True)
    left_co, cent_co,last_co = st.columns([0.35,0.33,0.32])
    with cent_co:
        if st.button("退出"):
            logout()

def custom_page_link(url, label, icon, new_tab=False):
    # 获取当前会话状态中的邀请码
    invite_code = st.session_state.get("invite_code", "")
    
    # 添加问号作为查询参数的开始
    if invite_code:
        if "?" in url:
            url = f"{url}&invite_code={invite_code}"
        else:
            url = f"{url}?invite_code={invite_code}"
    
    if new_tab:
        st.markdown(
            f'''
            <div class="row-widget stPageLink" style="width: 282px; margin: -0.4rem 0 0.65rem 0;">
                <div class="st-emotion-cache-j7qwjs e11k5jya2" style="padding: 0;">
                    <a href="/{url}" target="_blank" rel="noopener noreferrer" 
                       class="st-emotion-cache-n7e918 e11k5jya1" style="display: flex; align-items: center;">
                        <span color="#31333F" class="st-emotion-cache-6jwljf eyeqlp52" style="margin-right: 0rem;">
                            <span data-testid="stIconEmoji" aria-hidden="true" 
                                  class="st-emotion-cache-8hkptd eyeqlp50">{icon}</span>
                        </span>
                        <span class="st-emotion-cache-pkbazv e11k5jya0">
                            <div data-testid="stMarkdownContainer" 
                                 class="st-emotion-cache-187vdiz e1nzilvr4">
                                <p style="margin: 0;">{label}</p>
                            </div>
                        </span>
                    </a>
                </div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    else:
        st.page_link(url, label=label, icon=icon)

# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.4,0.32,0.28])
with cent_co:
    st.caption(":blue[_企业级客服机器人平台_]")
st.image('https://storage.googleapis.com/ghackathon/page_15_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')
    
with st.sidebar:
    
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
            st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.28,0.5,0.22])
    with cent_co:
            st.title(":blue[GCP Gen]:rainbow[AI]")
    st.page_link("homepage.py", label="主页", icon="🏠")
    st.page_link("pages/page_01_text_generation.py", label="文本生成", icon="📖")
    st.page_link("pages/page_13_prompt_generator.py", label="提示词生成器", icon="✨")
    st.page_link("pages/page_02_media_understanding.py", label="视频理解", icon="🎞️")
    st.page_link("pages/page_03_translation.py", label="文本翻译", icon="🇺🇳")
    st.page_link("pages/page_04_travel_advisor.py", label="旅游顾问", icon="✈️")
    st.page_link("pages/page_05_rag_search.py", label="RAG搜索", icon="🔍")
    st.page_link("pages/page_06_media_search.py", label="媒体搜索", icon="🎥")
    st.page_link("pages/page_07_image_generation.py", label="图片生成", icon="🎨")
    st.page_link("pages/page_08_chatbot.py", label="聊天机器人", icon="💬")
    st.page_link("pages/page_09_gaming_servicebot.py", label="游戏客服平台", icon="🤖")
    custom_page_link("https://gcp-genai-zh.streamlit.app/page_10_ecommerce_servicebot", label="电商客服平台", icon="🤖")
    st.page_link("pages/page_11_claude_chatbot.py", label="Claude3.5聊天机器人", icon="💬")
    st.page_link("pages/page_12_llama_chatbot.py", label="Llama3.1聊天机器人", icon="💬")
    st.page_link("https://pantheon.corp.google.com/translation/hub", label="GCP翻译门户", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/vertex-ai/generative/multimodal/gallery", label="GCP控制台 - Gemini", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/gen-app-builder/engines", label="GCP控制台 - Agent Builder", icon="🌎")
    st.text("")
    st.subheader('', divider='rainbow')
    st.text("")
    st.page_link("pages/page_14_user_manual.py", label="用户手册", icon="🧭")
    st.markdown(
        """
    ## 关于
    这是由:blue[Google Cloud Vertex AI]驱动的生成式AI平台以及企业级RAG搜索引擎
        """
    )
    st.page_link("https://cloud.google.com/vertex-ai?hl=en", label="Google Cloud Vertex AI", icon="☁️")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.page_link("pages/terms_of_service.py", label="用户服务协议", icon="📄")
    st.page_link("pages/privacy_policy.py", label="用户隐私政策", icon="🔒")

components.html("""
<link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
<script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
<df-messenger
  project-id="lwk-genai-test"
  agent-id="6cff449c-8ce8-44d8-982d-b8f49a55bc00"
  language-code="en"
  max-query-length="-1">
  <df-messenger-chat
   chat-title="Game Assistant"
   chat-title-icon="https://storage.googleapis.com/lwk-cai-demo-gstore/google-store-assistant-dialog-contents/Blizzard_Entertainment_Logo.png"
   bot-writing-image="https://storage.googleapis.com/lwk-cai-demo-gstore/google-store-assistant-dialog-contents/typing-2.gif"
   </df-messenger-chat>
</df-messenger>
<style>
    df-messenger {
        z-index: 999;
        position: fixed;
        --df-messenger-chat-border-radius: 10px;
        --df-messenger-titlebar-padding: 0 15px;
        --df-messenger-titlebar-icon-width: 70px;
        --df-messenger-titlebar-icon-height: 37px;
        --df-messenger-titlebar-icon-padding: 5px 10px 5px 208px;
        --df-messenger-titlebar-padding: 0;
        --df-messenger-titlebar-title-align: start;
        --df-messenger-titlebar-title-font-size: 30px;
        --df-messenger-titlebar-font-color: #000;
        --df-messenger-font-color: #1967D2;
        --df-messenger-font-family: Google Sans;
        --df-messenger-chat-background: #f3f6fc;
        --df-messenger-message-user-background: #D2E3FC;
        --df-messenger-message-user-font-color: #1967D2;
        --df-messenger-message-bot-background: #CEEAD6;
        --df-messenger-message-bot-font-color: #000;
        --df-messenger-chat-scroll-button-enabled-display: flex;
        --df-messenger-chat-scroll-button-align: center;
        --df-messenger-chat-scroll-button-text-display: inline;
        --df-messenger-message-bot-writing-font-color: #9AA0A6;
        --df-messenger-message-bot-writing-image-width: 70px;
        --df-messenger-message-bot-writing-image-height: 14px;
        left: 0;
        top: 0;
        bottom: 0;
        width: 702px;
        margin: auto;
    }
</style>
""", height=600)



st.markdown("<div style='margin-bottom: 60px;'></div>", unsafe_allow_html=True)

st.markdown('''
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 10px 0;
        margin-left: 11rem;
        text-align: center;
        z-index: 999;
        background-color: rgba(255, 255, 255, 0.5);
        color: black;
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
    }
    
    @media (prefers-color-scheme: dark) {
        .footer {
            background-color: rgba(14, 17, 23, 0.8) !important;
            color: white !important;
            backdrop-filter: blur(5px) !important;
            -webkit-backdrop-filter: blur(5px) !important;
        }
    }
    </style>

    <script>
    document.addEventListener("DOMContentLoaded", function() {
        setTimeout(function() {
            const isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
            const footer = document.querySelector('.footer');
            
            if (footer) {
                if (isDark) {
                    footer.style.backgroundColor = 'rgba(14, 17, 23, 0.8)';
                    footer.style.color = 'white';
                    footer.style.backdropFilter = 'blur(5px)';
                    footer.style.webkitBackdropFilter = 'blur(5px)';
                } else {
                    footer.style.backgroundColor = 'rgba(255, 255, 255, 0.5)';
                    footer.style.color = 'black';
                    footer.style.backdropFilter = 'blur(5px)';
                    footer.style.webkitBackdropFilter = 'blur(5px)';
                }
            }
            
            if (window.matchMedia) {
                window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
                    const isDarkNow = e.matches;
                    const footerNow = document.querySelector('.footer');
                    
                    if (footerNow) {
                        if (isDarkNow) {
                            footerNow.style.backgroundColor = 'rgba(14, 17, 23, 0.8)';
                            footerNow.style.color = 'white';
                            footerNow.style.backdropFilter = 'blur(5px)';
                            footerNow.style.webkitBackdropFilter = 'blur(5px)';
                        } else {
                            footerNow.style.backgroundColor = 'rgba(255, 255, 255, 0.5)';
                            footerNow.style.color = 'black';
                            footerNow.style.backdropFilter = 'blur(5px)';
                            footerNow.style.webkitBackdropFilter = 'blur(5px)';
                        }
                    }
                });
            }
        }, 500);
    });
    </script>
''', unsafe_allow_html=True)

# footer HTML
st.markdown('''
    <div class="footer">
      <div class="footer-content">
        <p style="margin: 0;">
          <span>© LWK &nbsp;&nbsp;|&nbsp;&nbsp Designed &amp; Developed by 
            <a href="{developer_profile_link}" style="text-decoration: underline; font-weight: bold;">{developer_name}</a>
          </span>
          <span> &nbsp;&nbsp;|&nbsp;&nbsp Powered by </span>
          <img src="https://storage.googleapis.com/ghackathon/GoogleCloud_logo_36px.png" alt="Logo" style="height: 18px; vertical-align: middle; margin: 0 2px; transform: translateY(-1px);">
          <span>Vertex AI</span>
        </p>
      </div>
    </div>
'''.format(
    developer_profile_link=st.secrets["developer_profile_link"],
    developer_name=st.secrets["developer_name"]
), unsafe_allow_html=True)