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

if not login():
    st.stop()

with st.sidebar:
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

credentials_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

creds = service_account.Credentials.from_service_account_info(
    credentials_info,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)

# 初始化会话状态
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

# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.45,0.36,0.29])
with cent_co:
    st.caption(":blue[_企业级聊天机器人_]")
st.image('https://storage.googleapis.com/ghackathon/page_18_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')
    
#idebar界面
with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.28,0.5,0.22])
    with cent_co:
        st.title(":blue[GCP Gen]:rainbow[AI]")
    temperature = st.slider("调整模型Temperature", min_value=0.0, max_value=2.0, value=1.0, help=(
        """
        Temperature用于响应生成期间的采样，这发生在应用 topP 和 topK 时。Temperature控制了token选择中的随机程度。对于需要较少开放式或创造性响应的提示，较低的temperature是好的，而较高的temperature可以导致更多样化或创造性的结果。Temperature为 0 意味着始终选择最高概率的token。在这种情况下，给定提示的响应大多是确定的，但仍有可能出现少量变化。
        
        如果模型返回的响应过于通用、太短或模型给出回退响应，请尝试提高temperature。
        """
    ))
    top_p = st.slider ("调整模型Top_p", min_value=0.00, max_value=1.00, value=0.95, help=(
        """
        Top-P 改变了模型选择输出tokens的方式。Tokens按照从最可能（见top-K）到最不可能的顺序进行选择，直到它们的概率之和等于top-P值。例如，如果token A、B和C的概率分别为0.3、0.2和0.1，top-P值为0.5，那么模型将使用温度从A或B中选择下一个token，并排除C作为候选。

        指定较低的值会得到较少的随机响应，指定较高的值会得到更多的随机响应。
        """
    ))
    
    generic_chat = "你是一个乐于助人的人类助手，请用用户跟你对话的语言来进行与用户的对话。如果用户询问关于目前或当前的信息，你需要随时使用Google Search来获取最新的信息,并提供Google Search的搜索链接给用户"
    python_expert = "你是一个python专家，可以帮助用户生成python代码，解释python代码，完善python代码"
    
    st.subheader('', divider='rainbow')
    
    system_instruction_option = ""
        
    system_instruction_option1 = st.radio(
        "请选择AI的角色：",
        ("友好的助手", "Python专家", "自定义"),
        index=None,
    )
    
    if system_instruction_option1 == "自定义":
        system_instruction_option2 = st.text_area ("请在此自由定义AI的角色：", "")
        submitted = st.button("提交")
        if submitted:
            st.session_state.custom_role_description = system_instruction_option2
    
    if system_instruction_option1 == "友好的助手":
        system_instruction_option = generic_chat
    elif system_instruction_option1 == "Python专家":
        system_instruction_option = python_expert
    elif system_instruction_option1 == "自定义" and "custom_role_description" in st.session_state:
        system_instruction_option = st.session_state.custom_role_description
    
    if system_instruction_option:
        st.write(f"您选择的AI角色描述为：{system_instruction_option}")
    else:
        st.error("请选择或定义AI角色")
   
    st.text("")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("开始新的对话", use_container_width=True):
            reset_conversation()
            st.experimental_rerun()
        
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

left_co, cent_co, last_co = st.columns([0.09, 0.83, 0.08])
with cent_co:
    st.markdown(
        f'<div class="footer">'
        f'<div class="footer-content">'
        f'<p style="text-align: center; margin: 0;">'
        f'<span style="color: black;">© LWK &nbsp;&nbsp;|&nbsp;&nbsp; </span> '
        f'<span style="color: grey;">Designed & Developed by</span> '
        f'<a href="{st.secrets["developer_profile_link"]}" '
        f'style="color: #185ABC; text-decoration: underline;" target="_blank">{st.secrets["developer_name"]}</a>'
        f'<span style="color: grey;"> &nbsp;&nbsp;|&nbsp;&nbsp; Powered by </span> '
        f'<span style="color: black; font-weight: bold;">Vertex AI</span> '
        f'</p>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )
        
# 处理上传的文件
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
                extracted_text = "此文件类型不支持文本提取。"
            
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

# 定义模型参数
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

# 初始化Streamlit应用
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

# 创建一个容器放置所有对话内容
chat_container = st.container()

# 在容器中显示聊天历史和新消息
with chat_container:
    # 显示聊天历史
    for idx, msg in enumerate(st.session_state.messages):
        st.chat_message(msg["role"]).write(msg["content"])
        if "files" in msg:
            for file_data in msg["files"]:
                if 'image' in file_data['mime_type']:
                    st.image(file_data['raw_data'])
                elif 'video' in file_data['mime_type']:
                    st.video(file_data['raw_data'])
                elif file_data['mime_type'] in ['application/pdf', 'text/plain']:
                    st.text_area("文件内容预览", file_data['preview'], height=200, key=f"history_{idx}_{file_data['id']}")

    # 处理新的API调用和响应
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
            
uploaded_files = st.file_uploader("上传图片、视频、PDF或TXT文件", type=['jpg', 'jpeg', 'png', 'mp4', 'pdf', 'txt'], accept_multiple_files=True, key=f"file_uploader_{st.session_state.file_key}")

if uploaded_files:
    process_uploaded_files(uploaded_files)

# 显示当前上传的文件
if st.session_state.current_files:
    for file_data in st.session_state.current_files:
        if 'image' in file_data['mime_type']:
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.image(file_data['raw_data'], caption='上传的图片', use_column_width=True)
        elif 'video' in file_data['mime_type']:
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.video(file_data['raw_data'], start_time=0)
        elif file_data['mime_type'] in ['application/pdf', 'text/plain']:
            st.text_area("文件内容预览", file_data.get('extracted_text', '无法提取文本内容'), height=200, key=f"preview_{file_data['id']}")
        else:
            st.warning("上传的文件类型不支持预览。")

# 聊天输入
user_input = st.chat_input("输入您的消息")

if user_input:
    if not st.session_state.current_role:
        st.error("👈请定义一种角色：在菜单中选择或者自定义")
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