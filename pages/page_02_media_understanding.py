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

vertexai.init(project="lwk-genai-test", location="us-central1", credentials=creds)
model = GenerativeModel("gemini-1.5-flash-001")
# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.35,0.35,0.3])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.4,0.30,0.3])
with cent_co:
    st.caption(":blue[_企业级内容生成平台_]")
st.image('https://storage.googleapis.com/ghackathon/page_1_zh.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')

#继续streamlit sidebar界面
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
    st.subheader('',divider='rainbow')

    uploaded_file = st.file_uploader("上传文件到 Google Cloud Storage", type=("mp4", "wmv", "jpg", "png"))
    
    #定义全局可用
    file_type = None
    
    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]
   
    #定义上传文件到存储桶的函数
    def upload_to_gcs(uploaded_file, bucket_name, destination_blob_name, source_file_name):
        """将文件上传到 Google Cloud Storage"""
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
            
        #删除临时文件
        os.remove(temp_file_name)
    
        return f"gs://{bucket_name}/{destination_blob_name}"
          
    with st.form("mysidebarform"):
        left_co, cent_co,last_co = st.columns([0.35,0.33,0.33])
        with cent_co:
            submitted = st.form_submit_button("上传")
        
        if submitted and not uploaded_file:
            st.markdown('<font size="2" color="#EA4335">请先选择文件</font>', unsafe_allow_html=True)
        
        if submitted and uploaded_file:
            with st.spinner('正在上传，请稍等...'):
                gs_uri = upload_to_gcs(uploaded_file, "your-bucket-name", uploaded_file.name, uploaded_file.name)
                st.markdown('<font size="2" color="#1E8E3E">文件已经成功上传至：</font>', unsafe_allow_html=True)
                st.code(gs_uri)
         
    st.page_link("https://pantheon.corp.google.com/storage/browser/lwk-rag-videos;tab=objects?forceOnBucketsSortingFiltering=true&e=13803378&hl=en&mods=dm_deploy_from_gcs&project=lwk-genai-test&prefix=&forceOnObjectsSortingFiltering=false", label="Google Cloud存储桶", icon="🌎")
    st.subheader('',divider='rainbow')
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
    这是由Google Cloud Vertex AI驱动的生成式AI平台以及企业级RAG搜索引擎
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

# 定义生成文本的函数
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

#定义视频理解的函数
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

# 定义生成模型参数
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

#继续streamlit界面
gcs_file = st.text_input("请输入您的文件的GCS链接", placeholder='gs://"您的存储桶名字"/"您的文件名"')

#定义全局可用
media_mime_type = None

file_extension = None

# 如果没有上传文件，则根据 GCS 链接推断文件类型
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

# 如果上传了文件，则使用上传文件的文件类型
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

prompt = st.text_area("请输入您的提示词：", "")

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.42,0.29,0.29])
    with cent_co:
        submitted = st.form_submit_button("生成文本")
    if gcs_file and submitted and not prompt:
        st.info("请输入提示词")
    
    if not gcs_file and prompt and submitted:
        with st.spinner('请稍等 :coffee: 马上就来...'):
            generated_text = generate_text(prompt)
            st.write(generated_text)
        
    if prompt and submitted and gcs_file:
        prompt_with_video = f"文档内容: \n{media}\n\n 提示词: \n{prompt}\n\n回答："
        with st.spinner('请稍等 :coffee: 马上就来...'):
            generated_video_text_text = generate_video_text(prompt_with_video)
            
            if file_extension in ("jpg", "png"):
                # 从 GCS 链接中提取存储桶名称和 blob 名称
                bucket_name = gcs_file.split("/")[2]
                blob_name = "/".join(gcs_file.split("/")[3:])
            
                # 获取 GCS 客户端和存储桶
                storage_client = storage.Client()
                bucket = storage_client.bucket(bucket_name)
                
                # 获取 blob 对象
                blob = bucket.blob(blob_name)
                
                # 使用 blob.public_url 获取 https:// 链接
                public_url = blob.public_url
            
                # 使用 https:// 链接显示图片
                st.image(public_url, caption=blob_name)
            
            st.write(generated_video_text_text)
