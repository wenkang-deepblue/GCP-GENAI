import streamlit as st
from auth import login, logout
from components import english_version_link

#this will showed on the top of user's
st.set_page_config(
    page_title="GCP GenAI",
    page_icon="👋",
)

if not login():
    st.stop()

manual_link = st.secrets["manual_link"]

invite_code = st.query_params.get("invite_code", "")

english_version_url = f"https://gcp-genai-en.streamlit.app/?invite_code={invite_code}" if invite_code else "https://gcp-genai-en.streamlit.app/"

st.markdown(f"""
    <div style="background-color: #D2E3FC; padding: 10px; border-radius: 5px; text-align: center; margin-bottom: 20px;">
        <span style="color: #5F6368;">请点击这里获取</span>
        <a href="{manual_link}" target="_blank" style="color: #4285F4; text-decoration: underline; font-weight: bold; font-family: 'Google Sans', sans-serif;">
            GCP-GenAI Demo手册
        </a>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    # 使用组件函数添加英文版链接
    st.markdown(english_version_link(), unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="background-color: #d4edda; border-color: #c3e6cb; color: #155724; 
                    padding: 10px; border-radius: 0.25rem; text-align: center; margin-bottom: 10px;">
            <p style="margin-bottom: 0;">欢迎!</p>
        </div>
    """, unsafe_allow_html=True)
    left_co, cent_co,last_co = st.columns([0.35,0.33,0.32])
    with cent_co:
        if st.button("log out"):
            logout()

st.image("https://storage.googleapis.com/ghackathon/galaxy%20banner%20with%20logo.png")


st.write("# 您好！欢迎使用 :blue[GCP Gen]:rainbow[AI] !")


st.markdown(
    """
    <div style="font-family: 'Google Sans', sans-serif;">
    GCP GenAI项目是利用<span style="color: #1A73E8;">Google Cloud Vertex AI</span>平台搭建的GenAI系统，其目的是演示Vertex AI各个模块可为企业实现的内容生成，媒体理解，RAG检索增强生成以及媒体搜索等功能。该项目所用到的Vertex AI模块包括：<span style="color: orange;">Gemini 1.5 Pro/Flash多模态模型，Agent Builder - Vertex AI Search，Imagen，DialogFlow</span>等等。Google Cloud中国销售及架构师团队愿意全力协助您利用Google强大的AI基础能力，以及GCP全面的AI生态及技术架构，搭建企业级的AI应用，帮助您的企业快速迭代，灵活开发，降低成本，提高效率。
    </div>
    """,
    unsafe_allow_html=True
)

st.text("")

st.markdown(
    """
    **👈 请点击左边开始体验吧！**
    
    
"""
)

with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.3,0.5,0.2])
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

st.markdown("<div style='margin-bottom: 60px;'></div>", unsafe_allow_html=True)

# 将 CSS 和 JS 注入到页面中
st.markdown("""
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
    }
    </style>

    <script>
    function setFooterTheme(){
       const isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
       let style = document.getElementById("custom-footer-style");
       if(!style) {
          // 如果没有style元素，则新建一个
          style = document.createElement('style');
          style.id = "custom-footer-style";
          document.head.appendChild(style);
       }
       if(isDark){
          style.innerText = `
          .footer {
              background-color: rgba(30, 34, 39, 1);
              color: white;
          }
          `;
       } else {
          style.innerText = `
          .footer {
              background-color: white;
              color: black;
          }
          `;
       }
    }
    
    // 初始化设置
    setFooterTheme();
    
    // 监听系统主题变化
    if(window.matchMedia){
       window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', setFooterTheme);
    }
    </script>
""", unsafe_allow_html=True)

# 添加 footer HTML 代码
st.markdown("""
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
""".format(
    developer_profile_link=st.secrets["developer_profile_link"],
    developer_name=st.secrets["developer_name"]
), unsafe_allow_html=True)