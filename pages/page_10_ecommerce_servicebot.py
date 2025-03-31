import streamlit as st
import streamlit.components.v1 as components
from auth import login, logout
from components import chinese_version_link, save_invite_code, vibtitle_link

st.set_page_config(
    page_title="GCP GenAI",
    page_icon="👋",
)

save_invite_code()

if not login():
    st.stop()

with st.sidebar:
    st.markdown(chinese_version_link(), unsafe_allow_html=True)
    st.markdown(f"""
        <div style="background-color: #d4edda; border-color: #c3e6cb; color: #155724; 
                    padding: 10px; border-radius: 0.25rem; text-align: center; margin-bottom: 10px;">
            <p style="margin-bottom: 0;">Welcome!</p>
        </div>
    """, unsafe_allow_html=True)
    left_co, cent_co,last_co = st.columns([0.35,0.33,0.32])
    with cent_co:
        if st.button("log out"):
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
            <div class="row-widget stPageLink" style="width: 282px; margin: -0.4rem 0 0.cbec99246ab9ab5rem 0;">
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

# Streamlit UI
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.3,0.45,0.25])
with cent_co:
    st.caption(":blue[_Enterprise-ready Customer Service Bot Platform_]")
st.image('https://storage.googleapis.com/ghackathon/page_7.png')
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
    st.page_link("homepage.py", label="Home", icon="🏠")
    st.page_link("pages/page_01_text_generation.py", label="Text Generation", icon="📖")
    st.page_link("pages/page_13_prompt_generator.py", label="Prompt Generator", icon="✨")
    st.page_link("pages/page_02_media_understanding.py", label="Media Understanding", icon="🎞️")
    st.page_link("pages/page_03_translation.py", label="Text Translation", icon="🇺🇳")
    st.page_link("pages/page_04_travel_advisor.py", label="Travel Advisor", icon="✈️")
    st.page_link("pages/page_05_rag_search.py", label="RAG Search", icon="🔍")
    st.page_link("pages/page_06_media_search.py", label="Media Search", icon="🎥")
    st.page_link("pages/page_07_image_generation.py", label="Image Generation", icon="🎨")
    st.page_link("pages/page_08_chatbot.py", label="Chatbot", icon="💬")
    custom_page_link("https://gcp-genai-en.streamlit.app/page_09_gaming_servicebot", label="Gaming Servicebot", icon="🤖")
    st.page_link("pages/page_10_ecommerce_servicebot.py", label="E-commerce Servicebot", icon="🤖")
    st.page_link("pages/page_11_claude_chatbot.py", label="Claude 3.5 Chatbot", icon="💬")
    st.page_link("pages/page_12_llama_chatbot.py", label="Llama 3.1 Chatbot", icon="💬")
    vibtitle_link()
    st.page_link("https://pantheon.corp.google.com/translation/hub", label="GCP Translation Hub", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/vertex-ai/generative/multimodal/gallery", label="GCP Console - Gemini", icon="🌎")
    st.page_link("https://pantheon.corp.google.com/gen-app-builder/engines", label="GCP Console - App Builder", icon="🌎")
    st.text("")
    st.subheader('', divider='rainbow')
    st.text("")
    st.page_link("pages/page_14_user_manual.py", label="Demo Manual", icon="🧭")
    st.markdown(
        """
    ## About
    This is a generative AI platform and enterprise-ready RAG search engine powered by :blue[Google Cloud Vertex AI]
        """
    )
    st.page_link("https://cloud.google.com/vertex-ai?hl=en", label="Google Cloud Vertex AI", icon="☁️")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    st.page_link("pages/terms_of_service.py", label="Terms of Service", icon="📄")
    st.page_link("pages/privacy_policy.py", label="Privacy Policy", icon="🔒")

# Embed Dialogflow code within an HTML component
components.html("""
<link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
<script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
<df-messenger
  project-id="lwk-genai-test"
  agent-id="da56aedf-e73e-4ae2-bcc3-ece9429c6328"
  language-code="en"
  max-query-length="-1">
  <df-messenger-chat
   chat-title="Google Store Assistant"
   chat-title-icon="https://storage.googleapis.com/ghackathon/GoogleG_FullColor_192px_3x.png"
   bot-writing-image="https://storage.googleapis.com/lwk-cai-demo-gstore/google-store-assistant-dialog-contents/typing-2.gif"
   </df-messenger-chat>
</df-messenger>
<style>
    df-messenger {
        z-index: 999;
        position: fixed;
        --df-messenger-chat-border-radius: 10px;
        --df-messenger-titlebar-padding: 0 15px;
        --df-messenger-titlebar-icon-width: 25px;
        --df-messenger-titlebar-icon-height: 25px;
        --df-messenger-titlebar-icon-padding: 5px 10px 5px 230px;
        --df-messenger-titlebar-padding: 0;
        --df-messenger-titlebar-title-align: start;
        --df-messenger-titlebar-title-font-size: 20px;
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