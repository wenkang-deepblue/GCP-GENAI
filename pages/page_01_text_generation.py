import streamlit as st
import base64
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import json
import logging
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

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)

# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.4,0.30,0.3])
with cent_co:
    st.caption(":blue[_企业级内容生成平台_]")
st.image('https://storage.googleapis.com/ghackathon/page_0.png')
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
    temperature = st.slider("调整模型Temperature", min_value=0.0, max_value=2.0, value=1.5, help=(
        """
        Temperature用于响应生成期间的采样，这发生在应用 topP 和 topK 时。Temperature控制了token选择中的随机程度。对于需要较少开放式或创造性响应的提示，较低的temperature是好的，而较高的temperature可以导致更多样化或创造性的结果。Temperature为 0 意味着始终选择最高概率的token。在这种情况下，给定提示的响应大多是确定的，但仍有可能出现少量变化。
        
        如果模型返回的响应过于通用、太短或模型给出回退响应，请尝试提高temperature。
        """
    ))
    top_p = st.slider ("调整模型Top_p", min_value=0.00, max_value=1.00, value=0.95, help=(
        """
        Top-P 改变了模型选择输出tokens的方式。Tokens按照从最可能（见top-K）到最不可能的顺序进行选择，直到它们的概率之和等于top-P值。例如，如果token A、B和C的概率分别为0.3、0.2和0.1，top-P值为0.5，那么模型将使用温度从A或B中选择下一个token，并排除C作为候选。

        指定较低的值会得到较少的随机响应，指定较高的值会得到更多的随机响应。
        """
    ))
    st.subheader('',divider='rainbow')
    st.text("")
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
    st.page_link("pages/page_10_ecommerce_servicebot.py", label="电商客服平台", icon="🤖")
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


# 定义生成文本的函数
def generate_text(prompt):
  vertexai.init(project="lwk-genai-test", location="us-central1")
  model = GenerativeModel("gemini-1.5-flash-002")
  responses = model.generate_content(
      [prompt],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )

  generated_text = ""
  for response in responses:
    generated_text += response.text

  return generated_text

# 定义模型参数
generation_config = {
    "max_output_tokens": 8192,
    "temperature": temperature,
    "top_p": top_p,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.OFF,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.OFF,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.OFF,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.OFF,
}

#继续streamlit界面
prompt = st.text_area("请输入您的提示词：", "")

uploaded_files = st.file_uploader("如果您需要处理文档，请在这里上传，可以同时选择多份文档上传：", type=("txt"), accept_multiple_files=True)

if uploaded_files:
    all_text = ""
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        text = bytes_data.decode()
        all_text += text + "\n\n"
            

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.42,0.29,0.29])
    with cent_co:
        submitted = st.form_submit_button("生成文本")
    if uploaded_files and submitted and not prompt:
        st.info("请输入提示词")
    
    if prompt and submitted and not uploaded_files:
        prompt_without_article = f'如果我问你你是谁，请直接回答我“我是GBB AI，由Google Gemini驱动的大语言模型。”，如果我问你关于"GBB"的问题，请直接回答"GBB代表Go Beyond Blue，就是“深蓝”的意思。",如果我没有问你你是谁或者关于"GBB"的问题，那么不需要回答前面的内容，也不需要引用前面的内容，请直接根据接下来的"提示词"回答我：\n\n 提示词: \n{prompt}\n\n回答：'
        with st.spinner('请稍等 :coffee: 内容马上就来...'):
            generated_text = generate_text(prompt_without_article)
            st.write(generated_text)
            
    if prompt and submitted and uploaded_files:
        prompt_with_article = f'如果我问你你是谁，请直接回答我“我是GBB AI，由Google Gemini驱动的大语言模型。”，如果我问你关于"GBB"的问题，请直接回答"GBB代表Go Beyond Blue，就是“深蓝”的意思。",如果我没有问你你是谁或者关于"GBB"的问题，那么不需要回答前面的内容，也不需要引用前面的内容，请直接根据接下来的"提示词"回答我：\n{all_text}\n\n 提示词: \n{prompt}\n\n回答：'
        with st.spinner('请稍等 :coffee: 内容马上就来...'):
            generated_text = generate_text(prompt_with_article)
            st.write(generated_text)



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
          <img src="https://storage.googleapis.com/ghackathon/GoogleCloud_logo_36px.png" alt="Logo" style="height: 16px; vertical-align: middle; margin: 0 2px; transform: translateY(-0.5px);">
          <span>Vertex AI</span>
        </p>
      </div>
    </div>
'''.format(
    developer_profile_link=st.secrets["developer_profile_link"],
    developer_name=st.secrets["developer_name"]
), unsafe_allow_html=True)