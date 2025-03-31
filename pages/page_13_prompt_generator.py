#Enterprise-level LLM Prompt Generator
import streamlit as st
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason, SafetySetting
import vertexai.preview.generative_models as generative_models
from auth import login, logout
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
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

auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)

# Streamlit application interface
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.3,0.6,0.1])
with cent_co:
    st.caption(":blue[_Enterprise-ready Content Generation Platform_]")
st.image('https://storage.googleapis.com/ghackathon/page_1.png')
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
    temperature = st.slider("Adjust Model Temperature", min_value=0.0, max_value=2.0, value=1.5, help=(
        """
        Temperature is used for sampling during response generation, which occurs when applying topP and topK. Temperature controls the degree of randomness in token selection. Lower temperatures are good for prompts that require less open-ended or creative responses, while higher temperatures can lead to more diverse or creative results. A temperature of 0 means always selecting the highest probability token. In this case, the response for a given prompt is mostly deterministic, but there may still be some minor variations.
        
        If the model returns responses that are too generic, too short, or the model gives fallback responses, try increasing the temperature.
        """
    ))
    top_p = st.slider ("Adjust Model Top_p", min_value=0.00, max_value=1.00, value=0.95, help=(
        """
        Top-P changes how the model selects output tokens. Tokens are chosen in order from most likely (see top-K) to least likely until their cumulative probability equals the top-P value. For example, if tokens A, B, and C have probabilities of 0.3, 0.2, and 0.1 respectively, and the top-P value is 0.5, the model will use temperature to choose the next token from either A or B, excluding C as a candidate.

        Specifying a lower value will result in less random responses, while specifying a higher value will result in more random responses.
        """
    ))
    st.subheader('',divider='rainbow')
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

# 定义生成文本的函数
def generate_prompt(task_or_prompt, selected_language):
  vertexai.init(project="lwk-genai-test", location="us-central1")

  system_instruction = f"""
    Given a task description or existing prompt, produce a detailed system prompt to guide a language model in completing the task effectively.

# Guidelines

- Understand the Task: Grasp the main objective, goals, requirements, constraints, and expected output.
- Minimal Changes: If an existing prompt is provided, improve it only if it's simple. For complex prompts, enhance clarity and add missing elements without altering the original structure.
- Reasoning Before Conclusions**: Encourage reasoning steps before any conclusions are reached. ATTENTION! If the user provides examples where the reasoning happens afterward, REVERSE the order! NEVER START EXAMPLES WITH CONCLUSIONS!
    - Reasoning Order: Call out reasoning portions of the prompt and conclusion parts (specific fields by name). For each, determine the ORDER in which this is done, and whether it needs to be reversed.
    - Conclusion, classifications, or results should ALWAYS appear last.
- Examples: Include high-quality examples if helpful, using placeholders [in brackets] for complex elements.
   - What kinds of examples may need to be included, how many, and whether they are complex enough to benefit from placeholders.
- Clarity and Conciseness: Use clear, specific language. Avoid unnecessary instructions or bland statements.
- Formatting: Use markdown features for readability. DO NOT USE ``` CODE BLOCKS UNLESS SPECIFICALLY REQUESTED.
- Preserve User Content: If the input task or prompt includes extensive guidelines or examples, preserve them entirely, or as closely as possible. If they are vague, consider breaking down into sub-steps. Keep any details, guidelines, examples, variables, or placeholders provided by the user.
- Constants: DO include constants in the prompt, as they are not susceptible to prompt injection. Such as guides, rubrics, and examples.
- Output Format: Explicitly the most appropriate output format, in detail. This should include length and syntax (e.g. short sentence, paragraph, JSON, etc.)
    - For tasks outputting well-defined or structured data (classification, JSON, etc.) bias toward outputting a JSON.
    - JSON should never be wrapped in code blocks (```) unless explicitly requested.
- If you need to mention LLM-related models, always use Gemini as an example.
- Please output in the language of {selected_language}.

The final prompt you output should adhere to the following structure below. Do not include any additional commentary, only output the completed system prompt. SPECIFICALLY, do not include any additional messages at the start or end of the prompt. (e.g. no "---")

[Concise instruction describing the task - this should be the first line in the prompt, no section header]

[Additional details as needed.]

[Optional sections with headings or bullet points for detailed steps.]

# Steps [optional]

[optional: a detailed breakdown of the steps necessary to accomplish the task]

# Output Format

[Specifically call out how the output should be formatted, be it response length, structure e.g. JSON, markdown, etc]

# Examples [optional]

[Optional: 1-3 well-defined examples with placeholders if necessary. Clearly mark where examples start and end, and what the input and output are. User placeholders as necessary.]
[If the examples are shorter than what a realistic example is expected to be, make a reference with () explaining how real examples should be longer / shorter / different. AND USE PLACEHOLDERS! ]

# Notes [optional]

[optional: edge cases, details, and an area to call or repeat out specific important considerations]
"""

  model = GenerativeModel(
      "gemini-1.5-pro-002",
      system_instruction=[system_instruction]
 )
  responses = model.generate_content(
      [f"Task, Goal, or Current Prompt:\n{task_or_prompt}"],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )

  generated_prompt = ""
  for response in responses:
    generated_prompt += response.text

  return generated_prompt

# 定义模型参数
generation_config = {
    "max_output_tokens": 8192,
    "temperature": temperature,
    "top_p": top_p,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

#Continue streamlit interface
task_or_prompt = st.text_area("Please enter your task description or existing prompt:", "")

uploaded_files = st.file_uploader("If you need to process documents, please upload them here. You can select multiple documents:", type=("txt"), accept_multiple_files=True)

left_co, cent_co,last_co = st.columns([0.3,0.5,0.2])
with cent_co:
    selected_language = st.radio(
        "Please select the language for the generated prompt:",
        options=["English", "中文"],
        index=None,
        horizontal=True
    )

if selected_language:
    st.write(f"Your selected prompt language is: {selected_language}")

if uploaded_files:
    all_text = ""
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        text = bytes_data.decode()
        all_text += text + "\n\n"

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.39,0.3,0.31])
    with cent_co:
        submitted = st.form_submit_button("Generate Prompt")
    if uploaded_files and submitted and not task_or_prompt:
        if not selected_language:
            st.error("Please select a language for the prompt")
        else:
            with st.spinner('Please wait :coffee: Optimizing prompt...'):
                generated_prompt = generate_prompt(task_or_prompt, selected_language)
                st.write(generated_prompt)

    if task_or_prompt and submitted and not uploaded_files:
        if not selected_language:
            st.error("Please select a language for the prompt")
        else:
            with st.spinner('Please wait :coffee: Optimizing prompt...'):
                generated_prompt = generate_prompt(task_or_prompt, selected_language)
                st.write(generated_prompt)
            
    if task_or_prompt and submitted and uploaded_files:
        if not selected_language:
            st.error("Please select a language for the prompt")
        else:
            task_with_files = f'{task_or_prompt}\n\n Document content: \n{all_text}'
            with st.spinner('Please wait :coffee: Optimizing prompt...'):
                generated_prompt = generate_prompt(task_with_files, selected_language)
                st.write(generated_prompt)


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