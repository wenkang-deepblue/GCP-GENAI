import streamlit as st
import requests
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import json
from auth import login, logout
from components import chinese_version_link, save_invite_code

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

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

# Set Discovery Engine API variables
base_url = "https://discoveryengine.googleapis.com/v1alpha"

# Create endpoint URL
endpoint_url = f"{base_url}/projects/210890376426/locations/global/collections/default_collection/dataStores/lwk-rag-search-data-store_1713579228500/conversations/-:converse"

# Set request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(creds.token),
}

# Streamlit interface
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.35,0.36,0.29])
with cent_co:
    st.caption(":blue[_Enterprise-ready RAG Search Engine_]")
st.image('https://storage.googleapis.com/ghackathon/page_4.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

# Streamlit interface
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
    st.page_link("pages/page_09_gaming_servicebot.py", label="Gaming Servicebot", icon="🤖")
    st.page_link("pages/page_10_ecommerce_servicebot.py", label="E-commerce Servicebot", icon="🤖")
    st.page_link("pages/page_11_claude_chatbot.py", label="Claude 3.5 Chatbot", icon="💬")
    st.page_link("pages/page_12_llama_chatbot.py", label="Llama 3.1 Chatbot", icon="💬")
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

# Set query prompt
query = st.text_area("Please input your question:", "")  # Replace this with your actual query
body = {
    "query": {"input": query},
    "summarySpec": {
        "summaryResultCount": 5,
        "modelSpec": {"version": "preview"},
        "ignoreAdversarialQuery": True,
        "includeCitations": True,
    },
}

# Set result keywords to display corresponding images
content_dict = {
    "Israel": {
        "image": "https://storage.googleapis.com/lwk-rag-search-demo/%E4%BB%A5%E8%89%B2%E5%88%97.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E4%BB%A5%E8%89%B2%E5%88%97%EF%BC%9A%E4%B8%80%E4%B8%AA%E5%9B%BD%E5%AE%B6%E7%9A%84%E8%AF%9E%E7%94%9F.pdf"
    },
    "Calculus": {
        "image": "https://storage.googleapis.com/lwk-rag-search-demo/%E5%BE%AE%E7%A7%AF%E5%88%86.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E5%85%AB%E5%8D%A6%E5%BE%AE%E7%A7%AF%E5%88%86.pdf"
    },
    "Quantum": {
        "image": "https://storage.googleapis.com/lwk-rag-search-demo/%E9%87%8F%E5%AD%90%E9%80%9A%E4%BF%A1.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E9%87%8F%E5%AD%90%E9%80%9A%E4%BF%A1.pdf"
    },
    "Archaeology": {
        "image": "https://storage.googleapis.com/lwk-rag-search-demo/%E8%80%83%E5%8F%A4%E7%8E%B0%E5%9C%BA.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E5%9B%B4%E8%A7%82%E8%80%83%E5%8F%A4%E7%8E%B0%E5%9C%BA.pdf"
    },
    "Myopia": {
        "image": "https://storage.googleapis.com/lwk-rag-search-demo/%E8%BF%91%E8%A7%86.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E8%BF%91%E8%A7%86%E6%80%8E%E4%B9%88%E5%8A%9E.pdf"
    },
    "Story":{
        "image": "https://storage.googleapis.com/lwk-rag-search-demo/%E5%86%99%E6%95%85%E4%BA%8B.png",
        "file": "https://storage.googleapis.com/lwk-rag-search-demo/%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E5%86%99%E6%95%85%E4%BA%8B.pdf"
    }
}

# Send POST request to Discovery Engine API
with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.44,0.28,0.28])
    with cent_co:
        submitted = st.form_submit_button("Submit")
    if submitted:
        with st.spinner('Processing, please be patient, the answer is on its way...'):
            response = requests.post(endpoint_url, headers=headers, json=body)
            answer = response.json()["reply"]["reply"]
        
            st.info(response.json()["reply"]["reply"] if response.status_code == 200 else response.text)
# Check request response code and return request result

    # Check if the answer contains keywords and display corresponding images and links
    
            for keyword in content_dict:
                if keyword in answer:
                    content=content_dict[keyword]
                    left_co, cent_co,last_co = st.columns([0.15,0.7,0.15])
                    with cent_co:
                        st.image(content["image"])
                    left_co, cent_co,last_co = st.columns([0.44,0.28,0.28])
                    with cent_co:
                        st.write(f'[Read Online]({content["file"]})')         
                    break  # Only display the first matching keyword
            else:
                st.write("No matching keywords found")


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