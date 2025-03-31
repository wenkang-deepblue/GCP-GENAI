import streamlit as st
import base64
import openai
from google.auth import default, transport
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import vertexai
import re
from PIL import Image
import io
import base64
import requests
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

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]
creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Refresh credentials
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

# Initialize Vertex AI
project_id = "lwk-genai-test"
location = "us-central1"
vertexai.init(project=project_id, location=location, credentials=creds)

# Set OpenAI client URL
url = f"https://us-central1-aiplatform.googleapis.com/v1beta1/projects/{project_id}/locations/{location}/endpoints/openapi"

# Create OpenAI client
client = openai.OpenAI(
    base_url=url,         
    api_key=creds.token,
)

APP_ID = "llama_chat"

def load_gif(gif_url):
    response = requests.get(gif_url)
    if response.status_code == 200:
        contents = response.content
        data_url = base64.b64encode(contents).decode("utf-8")
        return f"data:image/gif;base64,{data_url}"
    else:
        st.error(f"Unable to load GIF image: HTTP status code {response.status_code}")
        return ""

thinking_gif = load_gif("https://storage.googleapis.com/ghackathon/typing-dots-40.gif")

# Streamlit application interface
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.47,0.39,0.24])
with cent_co:
    st.caption(":blue[_Llama3.1 Chatbot_]")
st.image('https://storage.googleapis.com/ghackathon/page_18_en.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

# Sidebar interface
with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.28,0.5,0.22])
    with cent_co:
        st.title(":blue[GCP Gen]:rainbow[AI]")
    temperature = st.slider("Adjust Model Temperature", min_value=0.0, max_value=2.0, value=1.0, help=(
        """
        Temperature is used for sampling during response generation, which occurs when applying topP and topK. Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that require fewer open-ended or creative responses, while higher temperatures can lead to more diverse or creative results. A temperature of 0 means always selecting the highest probability token. In this case, the response for a given prompt is mostly deterministic, but some variation may still occur.
        
        If the model returns responses that are too generic, too short, or the model gives fallback responses, try increasing the temperature.
        """
    ))
    top_p = st.slider ("Adjust Model Top_p", min_value=0.00, max_value=1.00, value=0.95, help=(
        """
        Top-P changes how the model selects output tokens. Tokens are chosen from most likely to least likely until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have probabilities .3, .2, and .1, and the top-P value is .5, the model will select the next token from A or B using temperature and exclude C as a candidate.

        Specifying a lower value will result in less random responses, while specifying a higher value will result in more random responses.
        """
    ))
    
    generic_chat = "You are a helpful human assistant. Please converse with the user in the language they use to talk to you."
    python_expert = "You are a Python expert who can help users generate Python code, explain Python code, and improve Python code."
    
    st.subheader('', divider='rainbow')
    
    system_instruction_option = ""
        
    system_instruction_option1 = st.radio(
        "Please select the AI's role:",
        ("Friendly Assistant", "Python Expert", "Custom"),
        index=None,
    )
    
    if system_instruction_option1 == "Custom":
        system_instruction_option2 = st.text_area ("Please define the AI's role here:", "")
        submitted = st.button("Submit")
        if submitted:
            st.session_state.custom_role_description = system_instruction_option2
    
    if system_instruction_option1 == "Friendly Assistant":
        system_instruction_option = generic_chat
    elif system_instruction_option1 == "Python Expert":
        system_instruction_option = python_expert
    elif system_instruction_option1 == "Custom" and "custom_role_description" in st.session_state:
        system_instruction_option = st.session_state.custom_role_description
    
    if system_instruction_option:
        st.write(f"The AI role description you selected is: {system_instruction_option}")
    else:
        st.error("Please select or define an AI role")
   
    st.text("")
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

# LLaMA model
MODEL_ID = 'meta/llama3-405b-instruct-maas'

def generate_text(messages):    
    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=4000,
    )
    
    # Get message content
    content = response.choices[0].message.content
    
    content = re.sub(r'^assistant\s*|\s*assistant$', '', content, flags=re.IGNORECASE)
    
    code_blocks = re.findall(r'```[\s\S]*?```', content)
    for i, block in enumerate(code_blocks):
        content = content.replace(block, f'___CODE_BLOCK_{i}___')
    
    content = content.replace('\\n', '\n')
    
    content = re.sub(r'\n{2,}', '\n\n', content)
    content = re.sub(r'(?<!\n)\n(?!\n)', ' ', content)
    
    for i, block in enumerate(code_blocks):
        content = content.replace(f'___CODE_BLOCK_{i}___', block)
    
    return content.strip()
    
# Initialize Streamlit application
if f"{APP_ID}_messages" not in st.session_state:
    st.session_state[f"{APP_ID}_messages"] = []
if f"{APP_ID}_current_role" not in st.session_state:
    st.session_state[f"{APP_ID}_current_role"] = None

if system_instruction_option and system_instruction_option != st.session_state[f"{APP_ID}_current_role"]:
    st.session_state[f"{APP_ID}_current_role"] = system_instruction_option
    st.session_state[f"{APP_ID}_messages"] = [{"role": "system", "content": system_instruction_option}]

for msg in st.session_state.get(f"{APP_ID}_messages", [])[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not st.session_state.get(f"{APP_ID}_current_role"):
        st.error("👈 Please define a role: select from the menu or customize")
        st.stop()
    else:
        st.session_state[f"{APP_ID}_messages"].append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        gif_placeholder = st.empty()

        gif_placeholder.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="{thinking_gif}" alt="" style="width:30px;">'
            f'</div>',
            unsafe_allow_html=True
        )

        response = generate_text(st.session_state[f"{APP_ID}_messages"])

        gif_placeholder.empty()
        
        parts = re.split(r'(```[\s\S]*?```)', response)
        with st.chat_message("assistant"):
            for part in parts:
                if part.startswith('```') and part.endswith('```'):
                    language = part.split('\n')[0][3:].strip()
                    code = '\n'.join(part.split('\n')[1:-1])
                    st.code(code, language=language if language else None)
                else:
                    st.markdown(part)

        st.session_state[f"{APP_ID}_messages"].append({"role": "assistant", "content": response})


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