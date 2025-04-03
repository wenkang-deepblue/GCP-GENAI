import streamlit as st
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, Tool
import vertexai.preview.generative_models as generative_models
import io
import uuid
import streamlit.components.v1 as components
import PyPDF2
import time
import json
import logging
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
from auth import login, logout
from components import chinese_version_link, save_invite_code, vibtitle_link

st.set_page_config(
    layout="wide",
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

APP_ID = "travel_advisor"

# Initialize session state
if f'{APP_ID}_messages' not in st.session_state:
    st.session_state[f'{APP_ID}_messages'] = []
if f'{APP_ID}_current_files' not in st.session_state:
    st.session_state[f'{APP_ID}_current_files'] = None
if f'{APP_ID}_file_key' not in st.session_state:
    st.session_state[f'{APP_ID}_file_key'] = 0
if f'{APP_ID}_file_uploaded' not in st.session_state:
    st.session_state[f'{APP_ID}_file_uploaded'] = False
if f'{APP_ID}_user_input' not in st.session_state:
    st.session_state[f'{APP_ID}_user_input'] = ""
if f'{APP_ID}_need_api_call' not in st.session_state:
    st.session_state[f'{APP_ID}_need_api_call'] = False
if f'{APP_ID}_uploaded_files' not in st.session_state:
    st.session_state[f'{APP_ID}_uploaded_files'] = []
if f'{APP_ID}_json_data' not in st.session_state:
    st.session_state[f'{APP_ID}_json_data'] = None

# Reset conversation function
def reset_conversation():
    st.session_state[f'{APP_ID}_messages'] = []
    st.session_state[f'{APP_ID}_current_file'] = None
    st.session_state[f'{APP_ID}_file_uploaded'] = False
    st.session_state[f'{APP_ID}_file_key'] += 1
    st.session_state[f'{APP_ID}_need_api_call'] = False
    st.session_state[f'{APP_ID}_json_data'] = None
    if f'{APP_ID}_model' in st.session_state:
        st.session_state[f'{APP_ID}_chat'] = st.session_state[f'{APP_ID}_model'].start_chat()
    else:
        st.session_state.pop(f'{APP_ID}_chat', None)
        
# Streamlit application interface
left_co, cent_co,last_co = st.columns([0.45,0.35,0.2])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.45,0.42,0.13])
with cent_co:
    st.caption(":blue[_Intelligent Professional Travel Advisor_]")
left_co, cent_co,last_co = st.columns([1,2,1])
with cent_co:
    st.image('https://storage.googleapis.com/ghackathon/travel_advisor_en.png')
left_co, cent_co,last_co = st.columns([0.01,0.98,0.01])
with cent_co:
    st.subheader('', divider='rainbow')

# Streamlit sidebar interface
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
        
# Custom CSS styles
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title colors
title_colors = {
    "main_title": "#4285F4",  # Blue
    "travel_info": "#9334e6",  # Purple
    "weather": "#FBBC04",     # Yellow
    "flight": "#EA4335",  # Red
    "shopping": "#A142F4",    # Purple
    "restaurant": "#24C1E0",  # Cyan
    "attractions": "#F439A0", # Pink
}

# Colored title function
def colored_title(text, color, class_name="title"):
    return f'<div class="{class_name}" style="color: {color};">{text}</div>'

# Main page layout
col1, col2 = st.columns([1.7, 1.3])

# Travel Advisor system instruction
TRAVEL_ADVISOR_INSTRUCTION = """
You are a professional travel advisor AI assistant. Your task is to provide comprehensive, accurate, and friendly travel advice and information to users. You should:
1. Answer user questions about travel destinations, attractions, culture, cuisine, etc.
2. Provide personalized travel recommendations, considering user preferences and needs
3. Help users plan itineraries, including transportation, accommodation, and activity arrangements
4. Provide travel safety tips and local precautions
5. Recommend travel options that fit the user's budget and interests
6. Share interesting travel trivia and cultural background information
7. You should reply in the following example format:
  Country: France (New line)
  City: Paris (New line)
  {Introduction about Paris, please keep it around 500 words, introduce the history of this city, current main attractions, and give users a travel plan for the specified dates:
   For example: Day 1: Arc de Triomphe
        Day 2: Eiffel Tower
        Day 3: Roland Garros
        ...}
8. Please be sure to include the following JSON-formatted information in your reply, and add the tag "json_tag" before the JSON data and the tag "end_json_tag" after the JSON data:
json_tag
{
  "city": "City name",
  "weather": {
    "Date 1": "Weather description",
    "Date 2": "Weather description"
  },
  "tourist attractions": ["Attraction 1", "Attraction 2", "Attraction 3", "Attraction 4", "Attraction 5","Attraction 6", "Attraction 7", "Attraction 8", "Attraction 9","Attraction 10"],
  "flight information": {
    "Departure date": "Outbound flight information",
    "Arrival date": "Return flight information"
  },
  "flight price": "Price information",
  "Popular Shopping Sites": ["Shopping location 1", "Shopping location 2", "Shopping location 3", "Shopping location 4", "Shopping location 5"],
  "Popular restaurant": ["Restaurant 1", "Restaurant 2", "Restaurant 3", "Restaurant 4", "Restaurant 5"]
}
end_json_tag
Please ensure the JSON format is correct and includes all necessary information.
9. If the user doesn't have specific dates, please use Google Search to search for specific, detailed weather conditions for the most recent week and the cheapest real flight information. If the user has specific dates, please use Google Search to search for specific, detailed weather conditions and the cheapest real flight information based on the user's dates:
Example: Weather conditions: July 1, Sunny, 25-30°C, July 2, Heavy rain, 26-29°C
Example: Flight information: July 1 CZ322 Guangzhou -- Los Angeles, $1000, July 2 CZ323 Los Angeles -- Guangzhou, $1200
10. When displaying weather conditions in json_tag, please use emoji expressions instead of words, for example:
    Sunny: ☀️
    Rain: 🌧️
    Cloudy: ☁️
    ...
10. When searching for flight information, you must consider the time difference factor, for example:
If a user is traveling from China to the US from July 1 to July 7, the outbound flight should be departing on July 1, and the return flight should be a flight on July 6 local time in the US, because there is a time difference between China and the US.
Always maintain a friendly, patient, and professional attitude to provide the best travel consultation experience for users.
"""

SAFETY_CONFIGS = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

# Initialize Gemini model
model = GenerativeModel(
    "gemini-1.5-pro",
    generation_config={
        "max_output_tokens": 8192,
        "temperature": 0.7,
        "top_p": 0.95,
    },
    safety_settings=SAFETY_CONFIGS,
    tools=[
        Tool.from_google_search_retrieval(
            google_search_retrieval=generative_models.grounding.GoogleSearchRetrieval()
        )
    ],
    system_instruction=TRAVEL_ADVISOR_INSTRUCTION
)


# Initialize chat
if f'{APP_ID}_chat' not in st.session_state:
    st.session_state[f'{APP_ID}_chat'] = model.start_chat()

# Process uploaded files
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
                extracted_text = "This file type does not support text extraction."
            file_info = {
                'id': file_id,
                'mime_type': mime_type,
                'data': encoded_content,
                'raw_data': file_content,
                'extracted_text': extracted_text,
                'timestamp': time.time()
            }
            new_files.append(file_info)
        st.session_state[f'{APP_ID}_uploaded_files'].extend(new_files)
        st.session_state[f'{APP_ID}_current_files'] = new_files
        st.session_state[f'{APP_ID}_file_uploaded'] = True

# Function of generating text
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
                                
    try:
        response = chat.send_message(
            message_parts,
            generation_config={
                "max_output_tokens": 8192,
                "temperature": 0.7,
                "top_p": 0.95,
            },
            safety_settings=SAFETY_CONFIGS
        )
    
        if 'json_tag' not in response.text:
            logging.warning("JSON data not found in AI response")
            st.warning("AI failed to generate travel information data. Please try rephrasing your question or describe your needs in a different way.")
        
        return response
    except Exception as e:
        logging.error(f"Error generating text: {e}")
        st.error(f"Error generating reply: {e}")
        return None

# Function of processing model response
def process_model_response(response):
    text_response = response.text
    logging.debug(f"Raw AI response: {text_response}")
    
    json_start = text_response.find('json_tag')
    if json_start != -1:
        json_data = text_response[json_start + 8:].strip()
        logging.debug(f"Extracted JSON data: {json_data}")
        try:
            # Try to remove any extra text
            json_end = json_data.rfind('}')
            if json_end != -1:
                json_data = json_data[:json_end+1]
            st.session_state[f'{APP_ID}_json_data'] = json.loads(json_data)
            logging.info(f"Successfully parsed JSON data: {st.session_state[f'{APP_ID}_json_data']}")
        except json.JSONDecodeError as e:
            logging.error(f"JSON parsing error: {e}")
            logging.error(f"Attempted to parse JSON data: {json_data}")
            st.error(f"Unable to parse travel information data. Please try rephrasing your question. Error: {e}")
            st.session_state[f'{APP_ID}_json_data'] = None
        text_response = text_response[:json_start].strip()
    else:
        logging.warning("'json_tag' not found")
        st.session_state[f'{APP_ID}_json_data'] = None
    return text_response

# Add chat interface in col1
with col1:
    st.markdown(colored_title("Chat with Your AI Travel Advisor", title_colors["main_title"]), unsafe_allow_html=True)

    chat_container = st.container()
    
    # File upload
    uploaded_files = st.file_uploader("Upload images, videos, PDFs or TXT files", type=['jpg', 'jpeg', 'png', 'mp4', 'pdf', 'txt'], accept_multiple_files=True, key=f"file_uploader_{st.session_state[f'{APP_ID}_file_key']}")
    if uploaded_files:
        process_uploaded_files(uploaded_files)
    
    # Display currently uploaded files
    if st.session_state[f'{APP_ID}_current_files']:
        for file_data in st.session_state[f'{APP_ID}_current_files']:
            if 'image' in file_data['mime_type']:
                st.image(file_data['raw_data'], caption='Uploaded Image', use_column_width=True)
            elif 'video' in file_data['mime_type']:
                st.video(file_data['raw_data'], start_time=0)
            elif file_data['mime_type'] in ['application/pdf', 'text/plain']:
                st.text_area("File Content Preview", file_data.get('extracted_text', 'Unable to extract text content'), height=200, key=f"preview_{file_data['id']}")
            else:
                st.warning("Uploaded file type not supported for preview.")
    
    # Chat input
    user_input = st.chat_input("Input your message")
    
    # Display chat history and new messages in the container
    with chat_container:
        for msg in st.session_state[f'{APP_ID}_messages']:
            st.chat_message(msg["role"]).write(msg["content"])
            if "files" in msg:
                for file_data in msg["files"]:
                    if 'image' in file_data['mime_type']:
                        st.image(file_data['raw_data'])
                    elif 'video' in file_data['mime_type']:
                        st.video(file_data['raw_data'])
                    elif file_data['mime_type'] in ['application/pdf', 'text/plain']:
                        st.text_area("File Content Preview", file_data['extracted_text'], height=200)
    
        # Handle new user input
        if user_input:
            user_message = {"role": "user", "content": user_input}
            if st.session_state[f'{APP_ID}_current_files']:
                user_message["files"] = []
                for file_data in st.session_state[f'{APP_ID}_current_files']:
                    user_message["files"].append({
                        "id": file_data['id'],
                        "mime_type": file_data['mime_type'],
                        "extracted_text": file_data.get('extracted_text', ''),
                        "preview": file_data['extracted_text'] if file_data['mime_type'] in ['application/pdf', 'text/plain'] else None,
                        "raw_data": file_data['raw_data'] if 'image' in file_data['mime_type'] or 'video' in file_data['mime_type'] else None,
                        "data": file_data['data']
                    })
            st.session_state[f'{APP_ID}_messages'].append(user_message)
            st.chat_message("user").write(user_input)
        
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                message_placeholder.image("https://storage.googleapis.com/ghackathon/typing-dots-40.gif")
                try:
                    response = generate_text(user_input, st.session_state[f'{APP_ID}_chat'], st.session_state[f'{APP_ID}_messages'])
                    full_response = process_model_response(response)
                    message_placeholder.empty()
                    message_placeholder.write(full_response)
                except Exception as e:
                    logging.error(f"Error processing AI response: {e}")
                    message_placeholder.empty()
                    message_placeholder.error(f"Error processing response: {e}")
            
            st.session_state[f'{APP_ID}_messages'].append({"role": "assistant", "content": full_response})
            st.session_state[f'{APP_ID}_current_files'] = None
            
# Define block styles
block_styles = {
    "weather": {"bg_color": "#E6F3FF", "text_color": "#333333", "font": "Arial", "font_size": "16px"},
    "flight": {"bg_color": "#FFEBEE", "text_color": "#333333", "font": "Arial", "font_size": "16px"},
    "attractions": {"bg_color": "#E8F5E9", "text_color": "#333333", "font": "Arial", "font_size": "16px"},
    "shopping": {"bg_color": "#FFF3E0", "text_color": "#333333", "font": "Arial", "font_size": "16px"}
}

# Function of creating styled block
def create_styled_block(title, content, style):
    content_html = "<br>".join([f"{item}" for item in content.split('\n')]) if content.strip() else ""
    content_div = f'<div style="color: {style["text_color"]}; font-family: {style["font"]};">{content_html}</div>' if content_html else ""
    st.markdown(f"""
    <div style="background-color: {style['bg_color']}; padding: 10px; border-radius: 5px; margin-bottom: 10px; height: 400px; overflow-y: auto;">
        <h3 style="color: {style['text_color']}; font-family: {style['font']}; font-size: {style['font_size']}; text-align: center;">{title}</h3>
        {content_div}
    </div>
    """, unsafe_allow_html=True)

# Add functionality area in col2
with col2:
    location = st.session_state[f'{APP_ID}_json_data'].get("city", "") if st.session_state[f'{APP_ID}_json_data'] else ""
    st.markdown(colored_title(f"Travel Information - {location}" if location else "Travel Information", title_colors["travel_info"]), unsafe_allow_html=True)
    
    col2_left, col2_right = st.columns(2)
    
    with col2_left:
        # Weather information
        weather_data = st.session_state[f'{APP_ID}_json_data'].get("weather", {}) if st.session_state[f'{APP_ID}_json_data'] else {}
        weather_content = "\n".join([f"{date}: {weather}" for date, weather in weather_data.items()]) if isinstance(weather_data, dict) and weather_data else ""
        create_styled_block("Weather Information", weather_content, block_styles["weather"])
        
        # Main attractions
        attractions = st.session_state[f'{APP_ID}_json_data'].get("tourist attractions", []) if st.session_state[f'{APP_ID}_json_data'] else []
        attractions_content = "\n".join([f"- {attraction}" for attraction in attractions]) if attractions else ""
        create_styled_block("Main Attractions", attractions_content, block_styles["attractions"])
    
    with col2_right:
        # Flight information
        flight_info = st.session_state[f'{APP_ID}_json_data'].get("flight information", {}) if st.session_state[f'{APP_ID}_json_data'] else {}
        flight_content = "\n".join([f"{date}: {flight}" for date, flight in flight_info.items()]) if isinstance(flight_info, dict) and flight_info else ""
        if st.session_state[f'{APP_ID}_json_data'] and st.session_state[f'{APP_ID}_json_data'].get('flight price'):
            flight_content += f"\nPrice: {st.session_state[f'{APP_ID}_json_data'].get('flight price')}"
        create_styled_block("Flight Information", flight_content, block_styles["flight"])
        
        # Popular shopping sites
        shopping_sites = st.session_state[f'{APP_ID}_json_data'].get("Popular Shopping Sites", []) if st.session_state[f'{APP_ID}_json_data'] else []
        shopping_content = "\n".join([f"- {shop}" for shop in shopping_sites]) if shopping_sites else ""
        create_styled_block("Popular Shopping Sites", shopping_content, block_styles["shopping"])


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