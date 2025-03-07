import streamlit as st
from components import english_version_link, save_invite_code

st.set_page_config(
    page_title="GCP GenAI",
    page_icon="👋",
)

save_invite_code()

with st.sidebar:
    st.markdown(english_version_link(), unsafe_allow_html=True)
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

left_co, cent_co,last_co = st.columns([0.15,0.7,0.15])
with cent_co:
    st.title("GCP GenAI用户服务协议")

left_co, cent_co,last_co = st.columns([0.35,0.5,0.15])
with cent_co:
    st.write("生效日期: 2024年8月1日")

st.text("")

st.markdown("""

欢迎使用 GCP GenAI 应用（以下简称"本应用"）。在您使用本应用之前，请仔细阅读以下服务条款。通过访问或使用本应用，您同意接受这些条款的约束。如果您不同意这些条款，请不要使用本应用。

## 1. 服务描述

本应用是一个演示性质的web应用，旨在展示Google Cloud的Vertex AI的生成式AI (GenAI) 能力，包括但不限于文本生成、多模态理解、RAG搜索、图片生成以及聊天机器人等功能。本应用仅供Google员工向其客户演示Google Cloud的GenAI产品或服务的能力使用。

## 2. 使用资格

本应用仅面向Google内部员工提供服务，不对外部任何第三方开放使用。您需要使用您的Google公司账号登录，本应用将验证您的邮件地址域名，以确保您有权限使用本应用。

## 3. 用户责任

3.1 您同意仅将本应用用于其预期目的，即演示Google Cloud的GenAI能力。

3.2 您应当遵守所有适用的法律法规，并避免使用任何可能被视为敏感或不适当的内容，包括但不限于敏感词、敏感图片、敏感视频或敏感文档。

3.3 您理解并同意，如果由于使用了敏感信息而导致API拒绝返回结果，本应用不承担任何责任。

## 4. 数据处理

4.1 本应用没有后端服务，不会以任何形式存储任何个人信息或其他信息，包括但不限于用户提供的提示词、图片、视频或文档。

4.2 用户提供的所有数据都是通过本应用即时传递给Vertex AI相关API，API返回的所有信息和数据也都是即时通过浏览器显示给用户。

4.3 当用户结束使用本应用(例如关闭浏览器或清空对话记录)后，所有在此过程中产生的数据和信息都将被即时清除。这是由本应用的代码机制和逻辑所决定的。

4.4 本应用没有任何cookie设置，每次登录都是一次全新访问。

## 5. 知识产权

本应用为开放源代码应用，其相关的所有知识产权归开发者所有。本应用所使用的Streamlit框架，以及Google Cloud Vertex AI API，均归其各自开发者所有。用户复制或修改本应用的任何部分，请注明来源。用户不得将本应用用于商业化目的。

## 6. 免责声明

6.1 本应用"按现状"提供，不提供任何明示或暗示的保证。

6.2 本应用托管在Streamlit的应用托管服务上，不保证将不间断运行或无错误，也不保证任何缺陷将被纠正。

6.3 本应用免费提供给用户使用，不对用户使用所产生的任何直接、间接、偶然、特殊或后果性损害负责。

6.4 本应用为生成式AI应用，不对GenAI生成的结果或信息负责，请用户自行甄别生成信息的可靠性及真实性，并自主决定对生成信息的采纳和使用方式。

## 7. 服务变更和终止

本应用保留随时修改或终止的权利，无需事先通知。

## 8. 适用法律

这些条款受加利福尼亚州法律管辖，不考虑法律冲突原则。

## 9. 条款变更

本应用可能会不时更新这些服务条款。我们将在本页面上发布任何重大变更的通知。持续使用本应用即表示您接受任何此类变更。

## 10. 联系我们

如果您对这些服务条款有任何疑问，请联系：""" + f"{st.secrets['developer_email']}" + "。")



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