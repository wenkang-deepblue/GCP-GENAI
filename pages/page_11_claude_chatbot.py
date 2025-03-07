import streamlit as st
import base64
from anthropic import AnthropicVertex
import httpx
import io
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
from PIL import Image
import time
import uuid
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

# Initialize client
client = AnthropicVertex(region="europe-west1", project_id="lwk-genai-test", credentials=creds)

APP_ID = "claude_chat"

CURSOR_GIF_URL = "https://storage.googleapis.com/ghackathon/%E5%85%89%E6%A0%87-16.gif"

# Initialize session state
if f"{APP_ID}_current_role" not in st.session_state:
    st.session_state[f"{APP_ID}_current_role"] = None
if f'{APP_ID}_messages' not in st.session_state:
    st.session_state[f'{APP_ID}_messages'] = []
if f'{APP_ID}_current_file' not in st.session_state:
    st.session_state[f'{APP_ID}_current_file'] = None
if f'{APP_ID}_file_key' not in st.session_state:
    st.session_state[f'{APP_ID}_file_key'] = 0
if f'{APP_ID}_file_uploaded' not in st.session_state:
    st.session_state[f'{APP_ID}_file_uploaded'] = False
    
def load_gif(gif_url):
    return gif_url

# Load GIF image
thinking_gif = load_gif("https://storage.googleapis.com/ghackathon/typing-dots-40.gif")

def reset_conversation():
    st.session_state[f'{APP_ID}_messages'] = []
    st.session_state[f'{APP_ID}_current_file'] = None
    st.session_state[f'{APP_ID}_file_uploaded'] = False
    st.session_state[f'{APP_ID}_file_key'] += 1

# Streamlit application interface
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.42,0.43,0.15])
with cent_co:
    st.caption(":blue[_Claude 3.5 Chatbot_]")
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
    
    generic_chat = "You are a helpful human assistant. Please converse with the user in the language they use to talk to you."
    python_expert = "You are a Python expert who can help users generate Python code, explain Python code, and improve Python code."
    
    st.subheader('', divider='rainbow')
    
    system_instruction_option = ""
        
    system_instruction_option1 = st.radio(
        "Please select the AI role:",
        ("Friendly Assistant", "Python Expert", "Custom"),
        index=None,
    )
    
    if system_instruction_option1 == "Custom":
        system_instruction_option2 = st.text_area ("Please define the AI role here:", "")
        submitted = st.button("Submit")
        if submitted:
            st.session_state[f"{APP_ID}_custom_role_description"] = system_instruction_option2
    
    if system_instruction_option1 == "Friendly Assistant":
        system_instruction_option = generic_chat
    elif system_instruction_option1 == "Python Expert":
        system_instruction_option = python_expert
    elif system_instruction_option1 == "Custom" and f"{APP_ID}_custom_role_description" in st.session_state:
        system_instruction_option = st.session_state[f"{APP_ID}_custom_role_description"]
    
    if system_instruction_option:
        if system_instruction_option != st.session_state[f"{APP_ID}_current_role"]:
            st.session_state[f"{APP_ID}_current_role"] = system_instruction_option
            st.session_state[f'{APP_ID}_messages'] = []
            st.experimental_rerun()
        st.write(f"The AI role description you selected is: {system_instruction_option}")
    else:
        st.error("Please select or define an AI role")
   
    st.text("")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Start a new conversation", use_container_width=True):
            reset_conversation()
            st.experimental_rerun()
    
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
        
# Handle uploaded file
def process_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        file_id = str(uuid.uuid4())
        # Read file content
        file_content = uploaded_file.getvalue()
        # Get MIME type
        mime_type = uploaded_file.type
        # Encode file content to base64
        encoded_content = base64.b64encode(file_content).decode('utf-8')
        
        st.session_state[f'{APP_ID}_current_file'] = {
            'id': file_id,
            'mime_type': mime_type,
            'data': encoded_content,
            'raw_data': file_content
        }
        st.session_state[f'{APP_ID}_file_uploaded'] = True

def clear_file():
    st.session_state[f'{APP_ID}_current_file'] = None
    st.session_state[f'{APP_ID}_file_uploaded'] = False
    st.session_state[f'{APP_ID}_file_key'] += 1
 
def generate_text(messages, file_data=None):
    claude_messages = []
    for msg in messages:
        if msg["role"] == "user":
            content = [{"type": "text", "text": msg["content"]}]
            if "file" in msg:
                content.append({
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": msg["file"]['mime_type'],
                        "data": msg["file"]['data'],
                    },
                })
            claude_messages.append({"role": "user", "content": content})
        elif msg["role"] == "assistant":
            claude_messages.append({"role": "assistant", "content": [{"type": "text", "text": msg["content"]}]})

    try:
        with client.messages.stream(
            model="claude-3-5-sonnet@20240620",
            max_tokens=4096,
            messages=claude_messages,
            system=st.session_state[f"{APP_ID}_current_role"],
        ) as stream:
            for text in stream.text_stream:
                yield text
    except Exception as e:
        st.error(f"An error occurred while generating text: {str(e)}")
        yield None

# Create a container for conversation content
chat_container = st.container()

# Display chat history and new messages in the container
with chat_container:
    for msg in st.session_state[f'{APP_ID}_messages']:
        st.chat_message(msg["role"]).write(msg["content"])
        if "file" in msg:
            file_data = msg["file"]
            if 'image' in file_data['mime_type']:
                st.image(file_data['raw_data'])

thinking_placeholder = st.empty()

# Define image preview function
def image_preview():
    if st.session_state[f'{APP_ID}_current_file']:
        file_data = st.session_state[f'{APP_ID}_current_file']
        if 'image' in file_data['mime_type']:
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.image(file_data['raw_data'], caption='Currently uploaded image', use_column_width=True)
        else:
            st.warning("The uploaded file type does not support preview.")
            
uploaded_file = st.file_uploader("Upload image file", type=['jpg', 'jpeg', 'png'], key=f"file_uploader_{st.session_state[f'{APP_ID}_file_key']}")

# Create a placeholder for preview
preview_placeholder = st.empty()

if uploaded_file is not None:
    process_uploaded_file(uploaded_file)
    with preview_placeholder:
        image_preview()
        
user_input = st.chat_input("Input your message")

if user_input:
    if not st.session_state[f"{APP_ID}_current_role"]:
        st.error("👈 Please define a role: select from the menu or customize")
        st.stop()
    else:
        # Clear file preview
        preview_placeholder.empty()
        
        user_message = {"role": "user", "content": user_input}
        if st.session_state[f'{APP_ID}_current_file'] and st.session_state[f'{APP_ID}_file_uploaded']:
            user_message["file"] = st.session_state[f'{APP_ID}_current_file']
        
        st.session_state[f'{APP_ID}_messages'].append(user_message)
        
        # Update chat history
        with chat_container:
            st.chat_message("user").write(user_input)
            if st.session_state[f'{APP_ID}_file_uploaded']:
                file_data = st.session_state[f'{APP_ID}_current_file']
                if 'image' in file_data['mime_type']:
                    st.image(file_data['raw_data'])
                elif 'video' in file_data['mime_type']:
                    st.video(file_data['raw_data'])
                    
        thinking_placeholder.markdown(
            f'<div style="display: flex; justify-content: center;">'
            f'<img src="{thinking_gif}" alt="Thinking" style="width:30px;">'
            f'</div>',
            unsafe_allow_html=True
        )
        
        # Handle API call and response
        with chat_container:
            with st.chat_message("assistant"):
                response_placeholder = st.empty()

                full_response = ""
                for response in generate_text(st.session_state[f'{APP_ID}_messages']):
                    if response is not None:
                        full_response += response
                        response_placeholder.markdown(f"{full_response} ![Cursor]({CURSOR_GIF_URL})")
                        time.sleep(0.1)

                response_placeholder.markdown(full_response)
                st.session_state[f'{APP_ID}_messages'].append({"role": "assistant", "content": full_response})
                
        thinking_placeholder.empty()

        if st.session_state[f'{APP_ID}_file_uploaded']:
            clear_file()

# Scroll to the bottom of the page
st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)


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