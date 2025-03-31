import streamlit as st
from components import chinese_version_link, save_invite_code, vibtitle_link

st.set_page_config(
    page_title="GCP GenAI",
    page_icon="👋",
)

save_invite_code()

with st.sidebar:
    st.markdown(chinese_version_link(), unsafe_allow_html=True)
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
    st.page_link("pages/page_09_gaming_servicebot.py", label="Gaming Servicebot", icon="🤖")
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

left_co, cent_co,last_co = st.columns([0.15,0.75,0.1])
with cent_co:
    st.title("GCP GenAI Privacy Policy")

left_co, cent_co,last_co = st.columns([0.37,0.5,0.13])
with cent_co:
    st.write("Effective Date: August 1, 2024")

st.text("")

st.markdown("""




This Privacy Policy describes how the GCP GenAI application (hereinafter referred to as "the Application") collects, uses, and protects your personal information. We value your privacy and are committed to protecting your personal data. Please read this policy carefully to understand our practices.

## 1. Information Collection

1.1 The Application does not collect, store, or process any user personal information.

1.2 When using the Application, you need to log in with your Google company account. The Application only verifies your email address domain to confirm whether you have permission to use the Application, but does not record or store any of your personal information, including but not limited to name, email address, phone number, etc.

1.3 The Application does not have any form of backend storage service, including but not limited to databases, disks, and object storage services, therefore it cannot and has no ability to store any form of personal information or other information.

## 2. Information Use

2.1 The Application only immediately transmits the data provided by users (such as prompts, images, videos, or documents) to the relevant APIs of Google Cloud Vertex AI, and immediately displays the results returned by the API to users.

2.2 Since the Application does not store user data, it cannot and has no ability to use user data for any other purpose, let alone share user data with any third party.

## 3. Data Security

3.1 Since the Application does not store any user data, there is no risk of data leakage.

3.2 All data transmission is done through secure HTTPS protocol to ensure data security during transmission.

## 4. Cookies and Tracking Technologies

The Application does not use cookies or any other tracking technologies. Each login is a brand new visit.

## 5. Third-Party Services

The Application uses Google Cloud Vertex AI's API. According to Google Cloud's usage policy, Google Cloud has the right to refuse to respond to requests that violate its "Responsible AI" policy.

## 6. Data Retention

6.1 The Application does not retain any user data.

6.2 When users finish using the Application (for example, closing the browser or clearing the conversation history), all data and information generated during this process will be immediately cleared. This is determined by the code mechanism and logic of the Application.

## 7. User Rights

Since the Application does not collect or store any personal data, it does not involve the usual data subject rights such as the right of access, right of rectification, right of erasure, etc.

## 8. Children's Privacy

The Application does not provide services to individuals under 18 years of age and does not knowingly collect any information from individuals under 18 years of age.

## 9. International Data Transfer

The Application may involve transferring data to Google servers in the United States or other countries/regions. However, please note that this transfer is instantaneous and does not involve data storage.

## 10. Changes to Privacy Policy

The Application may update this Privacy Policy from time to time. Any significant changes will be posted on this page. We recommend that you regularly review this policy to stay informed of any updates.

## 11. Contact Us

If you have any questions or concerns about this Privacy Policy, please contact the developer of the Application: """ + f"{st.secrets['developer_email']}" + ".")


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