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
from auth import login, callback, logout

# 页面配置
st.set_page_config(layout="wide", page_title="GCP GenAI旅游助手")

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

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)

APP_ID = "travel_advisor"

# 初始化会话状态
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

# 重置对话函数
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
        
# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.45,0.35,0.2])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.47,0.4,0.13])
with cent_co:
    st.caption(":blue[_智能专业旅游顾问_]")
left_co, cent_co,last_co = st.columns([1,2,1])
with cent_co:
    st.image('https://storage.googleapis.com/ghackathon/travel_advisor.png')
left_co, cent_co,last_co = st.columns([0.01,0.98,0.01])
with cent_co:
    st.subheader('', divider='rainbow')

# 左侧栏
with st.sidebar:
    left_co, cent_co,last_co = st.columns([0.34,0.33,0.33])
    with cent_co:
        st.image('https://storage.googleapis.com/ghackathon/image2.gif')
    left_co, cent_co,last_co = st.columns([0.28,0.5,0.22])
    with cent_co:
        st.title(":blue[GCP Gen]:rainbow[AI]")
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
        
# 自定义CSS样式
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

# 定义标题颜色
title_colors = {
    "main_title": "#4285F4",  # 蓝色
    "travel_info": "#202124",  # 灰色
    "weather": "#FBBC04",     # 黄色
    "flight": "#EA4335",  # 红色
    "shopping": "#A142F4",    # 紫色
    "restaurant": "#24C1E0",  # 青色
    "attractions": "#F439A0", # 粉红色
}

# 创建带颜色的标题函数
def colored_title(text, color, class_name="title"):
    return f'<div class="{class_name}" style="color: {color};">{text}</div>'

# 主页面布局
col1, col2 = st.columns([1.7, 1.3])

# Travel Advisor系统指令
TRAVEL_ADVISOR_INSTRUCTION = """
你是一个专业的旅游顾问AI助手。你的任务是为用户提供全面、准确、友好的旅游建议和信息。你应该:
1. 回答用户关于旅游目的地、景点、文化、美食等方面的问题
2. 提供个性化的旅行建议，考虑用户的偏好和需求
3. 帮助用户规划行程，包括交通、住宿、活动安排等
4. 提供旅行安全提示和当地注意事项
5. 推荐符合用户预算和兴趣的旅游选项
6. 分享有趣的旅行小知识和文化背景信息
7. 你应当以如下示例形式回复：
  国家：法国（另起一行）
  城市：巴黎（另起一行）
  {关于巴黎的介绍，请保持在500字左右，介绍这座城市的历史，目前的主要景点，并给出用户在指定日期内的旅游规划：
   例如：第一天：凯旋门
        第二天：埃菲尔铁塔
        第三天：罗兰加洛斯
        ...}
8. 请务必在回复中包含以下JSON格式的信息，并在JSON数据前添加标记"json_tag"，在JSON数据后添加标记"end_json_tag"：
json_tag
{
  "city": "城市名称",
  "weather": {
    "日期1": "天气描述",
    "日期2": "天气描述"
  },
  "tourist attractions": ["景点1", "景点2", "景点3", "景点4", "景点5","景点6", "景点7", "景点8", "景点9","景点10"],
  "flight information": {
    "出发日期": "去程航班信息",
    "到达日期": "返程航班信息"
  },
  "flight price": "价格信息",
  "Popular Shopping Sites": ["购物地点1", "购物地点2", "购物地点3", "购物地点4", "购物地点5"],
  "Popular restaurant": ["餐厅1", "餐厅2", "餐厅3", "餐厅4", "餐厅5"]
}
end_json_tag
请确保JSON格式正确，且包含所有必要的信息。
9. 如果用户没有特定日期，请用Google Search搜索最近一周的具体、详细的天气情况和最便宜的真实的机票信息，如果用户有特定日期，请根据用户日期，用Google Search搜索具体、详细的天气情况及最便宜的真实的机票信息：
示例：天气情况：7月1日，晴，25-30°C，7月2日，中雨，26-29°C
示例：机票信息：7月1日CZ322 广州 -- 洛杉矶，2500，7月2日CZ323 洛杉矶 -- 广州，3000
10. 在json_tag中显示天气情况的时候，请用emoji表情替代文字，例如：
    晴：☀️
    雨：🌧️
    多云：☁️
    ...
10. 在搜索机票信息时，必须要考虑到时差因素，例如：
用户7月1日-7月7日从中国去美国，去程机票应当是7月1日出发的机票，回程机票应当是美国当地时间7月6日的航班，因为中国和美国有时差。
请始终保持友好、耐心和专业的态度，为用户提供最佳的旅游咨询体验。
"""

SAFETY_CONFIGS = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

# 初始化Gemini模型
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


# 初始化聊天
if f'{APP_ID}_chat' not in st.session_state:
    st.session_state[f'{APP_ID}_chat'] = model.start_chat()

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
        st.session_state[f'{APP_ID}_uploaded_files'].extend(new_files)
        st.session_state[f'{APP_ID}_current_files'] = new_files
        st.session_state[f'{APP_ID}_file_uploaded'] = True

# 生成文本函数
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
            logging.warning("AI 响应中未找到 JSON 数据")
            st.warning("AI 未能生成旅行信息数据，请尝试重新提问或换个方式描述您的需求。")
        
        return response
    except Exception as e:
        logging.error(f"生成文本时发生错误: {e}")
        st.error(f"生成回复时出错: {e}")
        return None

# 处理模型响应的函数
def process_model_response(response):
    text_response = response.text
    logging.debug(f"原始AI响应: {text_response}")
    
    json_start = text_response.find('json_tag')
    if json_start != -1:
        json_data = text_response[json_start + 8:].strip()
        logging.debug(f"提取的JSON数据: {json_data}")
        try:
            # 尝试移除可能的额外文本
            json_end = json_data.rfind('}')
            if json_end != -1:
                json_data = json_data[:json_end+1]
            st.session_state[f'{APP_ID}_json_data'] = json.loads(json_data)
            logging.info(f"成功解析JSON数据: {st.session_state[f'{APP_ID}_json_data']}")
        except json.JSONDecodeError as e:
            logging.error(f"JSON 解析错误: {e}")
            logging.error(f"尝试解析的JSON数据: {json_data}")
            st.error(f"无法解析旅行信息数据。请尝试重新提问。错误: {e}")
            st.session_state[f'{APP_ID}_json_data'] = None
        text_response = text_response[:json_start].strip()
    else:
        logging.warning("未找到 'json_tag'")
        st.session_state[f'{APP_ID}_json_data'] = None
    return text_response

# 在col1中添加聊天界面
with col1:
    st.markdown(colored_title("与您的AI旅游顾问对话", title_colors["main_title"]), unsafe_allow_html=True)

    # 创建一个容器来放置所有对话内容
    chat_container = st.container()
    
    # 文件上传
    # 修改文件上传器部分
    uploaded_files = st.file_uploader("上传图片、视频、PDF或TXT文件", type=['jpg', 'jpeg', 'png', 'mp4', 'pdf', 'txt'], accept_multiple_files=True, key=f"file_uploader_{st.session_state[f'{APP_ID}_file_key']}")
    if uploaded_files:
        process_uploaded_files(uploaded_files)
    
    # 显示当前上传的文件
    if st.session_state[f'{APP_ID}_current_files']:
        for file_data in st.session_state[f'{APP_ID}_current_files']:
            if 'image' in file_data['mime_type']:
                st.image(file_data['raw_data'], caption='上传的图片', use_column_width=True)
            elif 'video' in file_data['mime_type']:
                st.video(file_data['raw_data'], start_time=0)
            elif file_data['mime_type'] in ['application/pdf', 'text/plain']:
                st.text_area("文件内容预览", file_data.get('extracted_text', '无法提取文本内容'), height=200, key=f"preview_{file_data['id']}")
            else:
                st.warning("上传的文件类型不支持预览。")
    
    # 聊天输入
    user_input = st.chat_input("输入您的消息")
    
    # 在容器中显示聊天历史和新消息
    with chat_container:
        # 显示聊天历史
        for msg in st.session_state[f'{APP_ID}_messages']:
            st.chat_message(msg["role"]).write(msg["content"])
            if "files" in msg:
                for file_data in msg["files"]:
                    if 'image' in file_data['mime_type']:
                        st.image(file_data['raw_data'])
                    elif 'video' in file_data['mime_type']:
                        st.video(file_data['raw_data'])
                    elif file_data['mime_type'] in ['application/pdf', 'text/plain']:
                        st.text_area("文件内容预览", file_data['extracted_text'], height=200)
    
        # 处理新的用户输入
        # 处理新的用户输入
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
                    logging.error(f"处理 AI 响应时出错: {e}")
                    message_placeholder.empty()
                    message_placeholder.error(f"处理响应时出错: {e}")
            
            st.session_state[f'{APP_ID}_messages'].append({"role": "assistant", "content": full_response})
            st.session_state[f'{APP_ID}_current_files'] = None
            
# 定义板块样式
block_styles = {
    "weather": {"bg_color": "#E6F3FF", "text_color": "#333333", "font": "Arial", "font_size": "16px"},
    "flight": {"bg_color": "#FFEBEE", "text_color": "#333333", "font": "Arial", "font_size": "16px"},
    "attractions": {"bg_color": "#E8F5E9", "text_color": "#333333", "font": "Arial", "font_size": "16px"},
    "shopping": {"bg_color": "#FFF3E0", "text_color": "#333333", "font": "Arial", "font_size": "16px"}
}

# 创建带样式的板块函数
def create_styled_block(title, content, style):
    content_html = "<br>".join([f"{item}" for item in content.split('\n')]) if content.strip() else ""
    content_div = f'<div style="color: {style["text_color"]}; font-family: {style["font"]};">{content_html}</div>' if content_html else ""
    st.markdown(f"""
    <div style="background-color: {style['bg_color']}; padding: 10px; border-radius: 5px; margin-bottom: 10px; height: 400px; overflow-y: auto;">
        <h3 style="color: {style['text_color']}; font-family: {style['font']}; font-size: {style['font_size']}; text-align: center;">{title}</h3>
        {content_div}
    </div>
    """, unsafe_allow_html=True)

# 在col2中添加功能区
with col2:
    location = st.session_state[f'{APP_ID}_json_data'].get("city", "") if st.session_state[f'{APP_ID}_json_data'] else ""
    st.markdown(colored_title(f"旅行信息 - {location}" if location else "旅行信息", title_colors["travel_info"]), unsafe_allow_html=True)
    
    col2_left, col2_right = st.columns(2)
    
    with col2_left:
        # 天气信息
        weather_data = st.session_state[f'{APP_ID}_json_data'].get("weather", {}) if st.session_state[f'{APP_ID}_json_data'] else {}
        weather_content = "\n".join([f"{date}: {weather}" for date, weather in weather_data.items()]) if isinstance(weather_data, dict) and weather_data else ""
        create_styled_block("天气信息", weather_content, block_styles["weather"])
        
        # 主要景点
        attractions = st.session_state[f'{APP_ID}_json_data'].get("tourist attractions", []) if st.session_state[f'{APP_ID}_json_data'] else []
        attractions_content = "\n".join([f"- {attraction}" for attraction in attractions]) if attractions else ""
        create_styled_block("主要景点", attractions_content, block_styles["attractions"])
    
    with col2_right:
        # 机票信息
        flight_info = st.session_state[f'{APP_ID}_json_data'].get("flight information", {}) if st.session_state[f'{APP_ID}_json_data'] else {}
        flight_content = "\n".join([f"{date}: {flight}" for date, flight in flight_info.items()]) if isinstance(flight_info, dict) and flight_info else ""
        if st.session_state[f'{APP_ID}_json_data'] and st.session_state[f'{APP_ID}_json_data'].get('flight price'):
            flight_content += f"\n价格：{st.session_state[f'{APP_ID}_json_data'].get('flight price')}"
        create_styled_block("机票信息", flight_content, block_styles["flight"])
        
        # 热门购物地点
        shopping_sites = st.session_state[f'{APP_ID}_json_data'].get("Popular Shopping Sites", []) if st.session_state[f'{APP_ID}_json_data'] else []
        shopping_content = "\n".join([f"- {shop}" for shop in shopping_sites]) if shopping_sites else ""
        create_styled_block("热门购物地点", shopping_content, block_styles["shopping"])
