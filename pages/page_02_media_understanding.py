import streamlit as st
import base64
from google.oauth2 import service_account
import google.auth.transport.requests
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
from google.cloud import storage
import os
import tempfile
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
model = GenerativeModel("gemini-1.5-flash-001")
# Streamlit application interface
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.3,0.6,0.1])
with cent_co:
    st.caption(":blue[_Enterprise-ready Content Generation Platform_]")
st.image('https://storage.googleapis.com/ghackathon/page_2.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

# Continue streamlit sidebar interface
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
        Top-P changes how the model selects tokens for output. Tokens are selected from most probable to least until the sum of their probabilities equals the top-P value. For example, if tokens A, B, and C have probabilities 0.3, 0.2, and 0.1 and the top-P value is 0.5, the model will select either A or B using temperature and discard C as a candidate.

        Specifying a lower value will result in less random responses, while specifying a higher value will result in more random responses.
        """
    ))
    st.subheader('',divider='rainbow')

    uploaded_file = st.file_uploader("Upload file to Google Cloud Storage", type=("mp4", "wmv", "jpg", "png"))
    
    # Define globally available
    file_type = None
    
    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]
   
    # Define function to upload file to storage bucket
    def upload_to_gcs(uploaded_file, bucket_name, destination_blob_name, source_file_name):
        """Upload file to Google Cloud Storage"""
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(uploaded_file.read())
                temp_file_name = temp_file.name
        bucket_name = "lwk-rag-videos"
        source_file_name = uploaded_file.name
        destination_blob_name = uploaded_file.name
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        
        generation_match_precondition = 0
        
        blob.upload_from_filename(temp_file_name, if_generation_match=generation_match_precondition)               
            
        # Delete temporary file
        os.remove(temp_file_name)
    
        return f"gs://{bucket_name}/{destination_blob_name}"
          
    with st.form("mysidebarform"):
        left_co, cent_co,last_co = st.columns([0.33,0.4,0.27])
        with cent_co:
            submitted = st.form_submit_button("Upload")
        
        if submitted and not uploaded_file:
            st.markdown('<font size="2" color="#EA4335">Please select a file first</font>', unsafe_allow_html=True)
        
        if submitted and uploaded_file:
            with st.spinner('Uploading, please wait...'):
                gs_uri = upload_to_gcs(uploaded_file, "your-bucket-name", uploaded_file.name, uploaded_file.name)
                st.markdown('<font size="2" color="#1E8E3E">File has been successfully uploaded to:</font>', unsafe_allow_html=True)
                st.code(gs_uri)
         
    st.page_link("https://pantheon.corp.google.com/storage/browser/lwk-rag-videos;tab=objects?forceOnBucketsSortingFiltering=true&e=13803378&hl=en&mods=dm_deploy_from_gcs&project=lwk-genai-test&prefix=&forceOnObjectsSortingFiltering=false", label="Google Cloud Storage Bucket", icon="🌎")
    st.subheader('',divider='rainbow')
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

# Define function to generate text
def generate_text(prompt):
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

# Define function for video understanding
def generate_video_text(prompt):
    video_responses = model.generate_content(
        [media, prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    generated_video_text = ""
    for response in video_responses:
        generated_video_text += response.text

    return generated_video_text

# Define generation model parameters
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

# Continue streamlit interface
gcs_file = st.text_input("Please input the GCS link of your file", placeholder='gs://"Your bucket name"/"Your file name"')

# Define globally available
media_mime_type = None

file_extension = None

# If no file is uploaded, infer file type from GCS link
if gcs_file:
    file_extension = gcs_file.split(".")[-1].lower()
    if file_extension == "mp4":
        media_mime_type = "video/mp4"
    elif file_extension == "jpg":
        media_mime_type = "image/jpeg"
    elif file_extension == "png":
        media_mime_type = "image/png"
    elif file_extension == "gif":
        media_mime_type = "video/wmv"

# If a file is uploaded, use the file type of the uploaded file
elif file_type:
    if file_type == "mp4":
        media_mime_type = "video/mp4"
    elif file_type == "jpg":
        media_mime_type = "image/jpeg"
    elif file_type == "png":
        media_mime_type = "image/png"
    elif file_type == "wmv":
        media_mime_type = "video/wmv"


media = Part.from_uri(
    mime_type=media_mime_type,
    uri=gcs_file
)

prompt = st.text_area("Please input your prompt:", "")

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.42,0.29,0.29])
    with cent_co:
        submitted = st.form_submit_button("Generate Text")
    if gcs_file and submitted and not prompt:
        st.info("Please input a prompt")
    
    if not gcs_file and prompt and submitted:
        with st.spinner('Please wait :coffee: Coming right up...'):
            generated_text = generate_text(prompt)
            st.write(generated_text)
        
    if prompt and submitted and gcs_file:
        prompt_with_video = f"Document content: \n{media}\n\n Prompt: \n{prompt}\n\nAnswer:"
        with st.spinner('Please wait :coffee: Coming right up...'):
            generated_video_text_text = generate_video_text(prompt_with_video)
            
            if file_extension in ("jpg", "png"):
                # Extract bucket name and blob name from GCS link
                bucket_name = gcs_file.split("/")[2]
                blob_name = "/".join(gcs_file.split("/")[3:])
            
                # Get GCS client and bucket
                storage_client = storage.Client()
                bucket = storage_client.bucket(bucket_name)
                
                # Get blob object
                blob = bucket.blob(blob_name)
                
                # Use blob.public_url to get https:// link
                public_url = blob.public_url
            
                # Display image using https:// link
                st.image(public_url, caption=blob_name)
            
            st.write(generated_video_text_text)


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