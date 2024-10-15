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
from auth import login, callback, logout

if "code" in st.query_params:
    callback()

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

# 初始化客户端
client = AnthropicVertex(region="europe-west1", project_id="lwk-genai-test", credentials=creds)

APP_ID = "claude_chat"

CURSOR_GIF_URL = "https://storage.googleapis.com/ghackathon/%E5%85%89%E6%A0%87-16.gif"

# 初始化会话状态
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

# 加载GIF图片
thinking_gif = load_gif("https://storage.googleapis.com/ghackathon/typing-dots-40.gif")

def reset_conversation():
    st.session_state[f'{APP_ID}_messages'] = []
    st.session_state[f'{APP_ID}_current_file'] = None
    st.session_state[f'{APP_ID}_file_uploaded'] = False
    st.session_state[f'{APP_ID}_file_key'] += 1

# Streamlit应用界面
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.42,0.36,0.22])
with cent_co:
    st.caption(":blue[_企业级聊天机器人_]")
st.image('https://storage.googleapis.com/ghackathon/page_18_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

#Sidebar界面
with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.28,0.5,0.22])
    with cent_co:
        st.title(":blue[GCP Gen]:rainbow[AI]")
    
    generic_chat = "你是一个乐于助人的人类助手，请用用户跟你对话的语言来进行与用户的对话"
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
            st.session_state[f"{APP_ID}_custom_role_description"] = system_instruction_option2
    
    if system_instruction_option1 == "友好的助手":
        system_instruction_option = generic_chat
    elif system_instruction_option1 == "Python专家":
        system_instruction_option = python_expert
    elif system_instruction_option1 == "自定义" and f"{APP_ID}_custom_role_description" in st.session_state:
        system_instruction_option = st.session_state[f"{APP_ID}_custom_role_description"]
    
    if system_instruction_option:
        if system_instruction_option != st.session_state[f"{APP_ID}_current_role"]:
            st.session_state[f"{APP_ID}_current_role"] = system_instruction_option
            st.session_state[f'{APP_ID}_messages'] = []
            st.experimental_rerun()
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
    st.markdown(
        """
    ## 关于
    这是由:blue[Google Cloud Vertex AI]驱动的生成式AI平台以及企业级RAG搜索引擎
        """
    )
    st.page_link("https://cloud.google.com/vertex-ai?hl=en", label="Google Cloud Vertex AI", icon="☁️")
    left_co, cent_co,last_co = st.columns([0.41,0.31,0.28])
    with cent_co:
        st.write('© LWK')
    left_co, cent_co,last_co = st.columns([0.09,0.83,0.08])
    with cent_co:
        st.markdown(
        f'<p style="text-align: center;">'
        f'<span style="color: grey;">Designed & Developed by</span> '
        f'<a href="{st.secrets["developer_profile_link"]}" '
        f'style="color: #185ABC; text-decoration: underline;" target="_blank">{st.secrets["developer_name"]}</a>'
        f'</p>',
        unsafe_allow_html=True
    )
    left_co, cent_co,last_co = st.columns([0.22,0.6,0.18])
    with cent_co:
        st.write(':grey[Powered by] **Vertex AI**')

    st.page_link("pages/terms_of_service.py", label="用户服务协议", icon="📄")
    st.page_link("pages/privacy_policy.py", label="用户隐私政策", icon="🔒")
        
# 处理上传的文件
def process_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        file_id = str(uuid.uuid4())
        # 读取文件内容
        file_content = uploaded_file.getvalue()
        # 获取MIME类型
        mime_type = uploaded_file.type
        # 将文件内容编码为base64
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
        st.error(f"生成文本时发生错误: {str(e)}")
        yield None

# 创建一个容器放置对话内容
chat_container = st.container()

# 在容器中显示聊天历史和新消息
with chat_container:
    for msg in st.session_state[f'{APP_ID}_messages']:
        st.chat_message(msg["role"]).write(msg["content"])
        if "file" in msg:
            file_data = msg["file"]
            if 'image' in file_data['mime_type']:
                st.image(file_data['raw_data'])

thinking_placeholder = st.empty()

# 定义图片预览函数
def image_preview():
    if st.session_state[f'{APP_ID}_current_file']:
        file_data = st.session_state[f'{APP_ID}_current_file']
        if 'image' in file_data['mime_type']:
            col1, col2, col3 = st.columns([1,2,1])
            with col2:
                st.image(file_data['raw_data'], caption='当前上传的图片', use_column_width=True)
        else:
            st.warning("上传的文件类型不支持预览。")
            
uploaded_file = st.file_uploader("上传图片文件", type=['jpg', 'jpeg', 'png'], key=f"file_uploader_{st.session_state[f'{APP_ID}_file_key']}")

# 创建一个用于预览的占位符
preview_placeholder = st.empty()

if uploaded_file is not None:
    process_uploaded_file(uploaded_file)
    with preview_placeholder:
        image_preview()
        
user_input = st.chat_input("输入您的消息")

if user_input:
    if not st.session_state[f"{APP_ID}_current_role"]:
        st.error("👈请定义一种角色：在菜单中选择或者自定义")
        st.stop()
    else:
        # 清除文件预览
        preview_placeholder.empty()
        
        user_message = {"role": "user", "content": user_input}
        if st.session_state[f'{APP_ID}_current_file'] and st.session_state[f'{APP_ID}_file_uploaded']:
            user_message["file"] = st.session_state[f'{APP_ID}_current_file']
        
        st.session_state[f'{APP_ID}_messages'].append(user_message)
        
        # 更新聊天历史
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
            f'<img src="{thinking_gif}" alt="思考中" style="width:30px;">'
            f'</div>',
            unsafe_allow_html=True
        )
        
        # 处理API调用和响应
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

# 使页面滚动到底部
st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)
