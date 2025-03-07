import streamlit as st
import base64
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import vertexai
from vertexai.generative_models import GenerativeModel, Part, Tool
import vertexai.preview.generative_models as generative_models
from vertexai.preview.generative_models import grounding
import io
import uuid
import streamlit.components.v1 as components
import PyPDF2
import time
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

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_files' not in st.session_state:
    st.session_state.current_files = None
if 'file_key' not in st.session_state:
    st.session_state.file_key = 0
if 'file_uploaded' not in st.session_state:
    st.session_state.file_uploaded = False
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""
if 'need_api_call' not in st.session_state:
    st.session_state.need_api_call = False
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []

tools = [
    Tool.from_google_search_retrieval(
        google_search_retrieval=grounding.GoogleSearchRetrieval()
    ),
]

def reset_conversation():
    st.session_state.messages = []
    st.session_state.current_file = None
    st.session_state.file_uploaded = False
    st.session_state.file_key += 1
    st.session_state.need_api_call = False
    if 'model' in st.session_state and 'current_role' in st.session_state:
        st.session_state.chat = st.session_state.model.start_chat()
    else:
        st.session_state.pop('chat', None)

# Streamlit application interface
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.43,0.38,0.29])
with cent_co:
    st.caption(":blue[_Enterprise-ready Chatbot_]")
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
        Temperature is used for sampling during response generation, which happens after applying topP and topK. Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that require a less open-ended or creative response, while higher temperatures can lead to more diverse or creative results. A temperature of 0 means the highest probability token is always selected. In this case, the response for a given prompt is mostly deterministic, but some variation may still occur.
        
        If the model returns responses that are too generic, too short, or the model gives a fallback response, try increasing the temperature.
        """
    ))
    top_p = st.slider ("Adjust Model Top_p", min_value=0.00, max_value=1.00, value=0.95, help=(
        """
        Top-P changes how the model selects tokens for output. Tokens are selected from most probable to least until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have probabilities 0.3, 0.2, and 0.1 and the top-P value is 0.5, the model will select the next token from A or B using temperature and discard C as a candidate.

        Specifying a lower value will result in less random responses, while specifying a higher value will result in more random responses.
        """
    ))
    
    generic_chat = "You are a helpful human assistant, please respond to users in the same language they use to communicate with you. If users ask about current or up-to-date information, you should always use Google Search to get the latest information and provide users with the Google Search link."
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
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Start a New Conversation", use_container_width=True):
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
        
# Handle uploaded files
def process_uploaded_files(uploaded_files):
    if uploaded_files:
        new_files = []
        for uploaded_file in uploaded_files:
            file_id = str(uuid.uuid4())
            file_content = uploaded_file.getvalue()
            mime_type = uploaded_file.type
            encoded_content = base64.b64encode(file_content).decode('utf-8')
            
            extracted_text = ""
            if mime_type == 'application/pdf':
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
                extracted_text = "\n".join([page.extract_text() for page in pdf_reader.pages])
            elif mime_type == 'text/plain':
                extracted_text = file_content.decode('utf-8')
            else:
                extracted_text = "Text extraction is not supported for this file type."
            
            file_info = {
                'id': file_id,
                'mime_type': mime_type,
                'data': encoded_content,
                'raw_data': file_content,
                'extracted_text': extracted_text,
                'timestamp': time.time()
            }
            
            new_files.append(file_info)
        
        st.session_state.uploaded_files.extend(new_files)
        st.session_state.current_files = new_files
        st.session_state.file_uploaded = True

def clear_files():
    st.session_state.current_files = []
    st.session_state.file_uploaded = False
    st.session_state.file_key += 1
 
def generate_text(prompt, chat, messages):
    message_parts = [prompt]
    
    for msg in messages:
        if isinstance(msg, dict):
            if "content" in msg:
                message_parts.append(Part.from_text(msg["content"]))
            if "files" in msg:
                for file_data in msg["files"]:
                    if isinstance(file_data, dict):
                        mime_type = file_data.get('mime_type')
                        if mime_type in ['application/pdf', 'text/plain']:
                            extracted_text = file_data.get('extracted_text', '')
                            if extracted_text:
                                message_parts.append(Part.from_text(f"File content: {extracted_text}"))
                        elif mime_type and (mime_type.startswith('image/') or mime_type.startswith('video/')):
                            data = file_data.get('data')
                            if data:
                                message_parts.append(Part.from_data(mime_type=mime_type, data=data))
    
    response = chat.send_message(
        message_parts,
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    return response

# Define model parameters
generation_config = {
    "max_output_tokens": 8192,
    "temperature": temperature,
    "top_p": top_p,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

# Initialize Streamlit application
if "current_role" not in st.session_state or "model" not in st.session_state:
    st.session_state.current_role = None
    st.session_state.model = None

if system_instruction_option and (system_instruction_option != st.session_state.current_role or st.session_state.model is None):
    st.session_state.current_role = system_instruction_option
    st.session_state.messages = []
    st.session_state.model = GenerativeModel(
        "gemini-1.5-pro",
        tools=tools,
        system_instruction=system_instruction_option
    )
    st.session_state.chat = st.session_state.model.start_chat()

# Create a container for all conversation content
chat_container = st.container()

# Display chat history and new messages in the container
with chat_container:
    # Display chat history
    for idx, msg in enumerate(st.session_state.messages):
        st.chat_message(msg["role"]).write(msg["content"])
        if "files" in msg:
            for file_data in msg["files"]:
                if 'image' in file_data['mime_type']:
                    st.image(file_data['raw_data'])
                elif 'video' in file_data['mime_type']:
                    st.video(file_data['raw_data'])
                elif file_data['mime_type'] in ['application/pdf', 'text/plain']:
                    st.text_area("File Content Preview", file_data['preview'], height=200, key=f"history_{idx}_{file_data['id']}")

    # Handle new API calls and responses
    if st.session_state.need_api_call:
        with st.chat_message("assistant"):
            thinking_placeholder = st.empty()
            thinking_placeholder.image("https://storage.googleapis.com/ghackathon/typing-dots-40.gif")
            last_message = st.session_state.messages[-1]
            response = generate_text(last_message.get("content", ""), st.session_state.chat, st.session_state.messages)
            assistant_msg = response.candidates[0].content.parts[0].text
            thinking_placeholder.empty()
            st.write(assistant_msg)
            st.session_state.messages.append({"role": "assistant", "content": assistant_msg})
            st.session_state.need_api_call = False
            if st.session_state.file_uploaded:
                clear_files()
            
uploaded_files = st.file_uploader("Upload images, videos, PDFs, or TXT files", type=['jpg', 'jpeg', 'png', 'mp4', 'pdf', 'txt'], accept_multiple_files=True, key=f"file_uploader_{st.session_state.file_key}")

if uploaded_files:
    process_uploaded_files(uploaded_files)

# Display currently uploaded files
if st.session_state.current_files:
    for file_data in st.session_state.current_files:
        if 'image' in file_data['mime_type']:
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.image(file_data['raw_data'], caption='Uploaded Image', use_column_width=True)
        elif 'video' in file_data['mime_type']:
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.video(file_data['raw_data'], start_time=0)
        elif file_data['mime_type'] in ['application/pdf', 'text/plain']:
            st.text_area("File Content Preview", file_data.get('extracted_text', 'Unable to extract text content'), height=200, key=f"preview_{file_data['id']}")
        else:
            st.warning("Preview is not supported for the uploaded file type.")

# Chat input
user_input = st.chat_input("Input your message")

if user_input:
    if not st.session_state.current_role:
        st.error("👈 Please define a role: select from the menu or customize")
        st.stop()
    else:
        user_message = {"role": "user", "content": user_input or ""}
        if st.session_state.current_files:
            user_message["files"] = []
            for file_data in st.session_state.current_files:
                user_message["files"].append({
                    "id": file_data['id'],
                    "mime_type": file_data['mime_type'],
                    "extracted_text": file_data.get('extracted_text', ''),
                    "preview": file_data['extracted_text'] if file_data['mime_type'] in ['application/pdf', 'text/plain'] else None,
                    "raw_data": file_data['raw_data'] if 'image' in file_data['mime_type'] or 'video' in file_data['mime_type'] else None,
                    "data": file_data['data']
                })

        st.session_state.messages.append(user_message)
        st.session_state.need_api_call = True
        st.session_state.current_files = None
        st.experimental_rerun()


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