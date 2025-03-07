#企业级LLM提示词生成器
import streamlit as st
import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason, SafetySetting
import vertexai.preview.generative_models as generative_models
from auth import login, logout
import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests

# 检查用户是否已登录
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

# Streamlit 应用界面
left_co, cent_co,last_co = st.columns([0.35,0.32,0.33])
with cent_co:
    st.title(":blue[GCP Gen]:rainbow[AI]")
left_co, cent_co,last_co = st.columns([0.38,0.32,0.3])
with cent_co:
    st.caption(":blue[_企业级LLM提示词生成器_]")
st.image('https://storage.googleapis.com/ghackathon/page_0.png')
left_co, cent_co,last_co = st.columns([0.24,0.51,0.25])
with cent_co:
    st.subheader('', divider='rainbow')
    
#继续streamlit sidebar界面
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
    st.text("")
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

#继续streamlit界面
task_or_prompt = st.text_area("请输入您的任务描述或现有提示词：", "")

uploaded_files = st.file_uploader("如果您需要处理文档，请在这里上传，可以同时选择多份文档上传：", type=("txt"), accept_multiple_files=True)

left_co, cent_co,last_co = st.columns([0.4,0.4,0.2])
with cent_co:
    selected_language = st.radio(
        "请选择生成的提示词语言：",
        options=["English", "中文"],
        index=None,
        horizontal=True
    )

if selected_language:
    st.write(f"您选择生成的提示词语言是：{selected_language}")

if uploaded_files:
    all_text = ""
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        text = bytes_data.decode()
        all_text += text + "\n\n"

with st.form("myform"):
    left_co, cent_co,last_co = st.columns([0.42,0.29,0.29])
    with cent_co:
        submitted = st.form_submit_button("生成提示词")
    if uploaded_files and submitted and not task_or_prompt:
        if not selected_language:
            st.error("请选择生成的提示词语言")
        else:
            with st.spinner('请稍等 :coffee: 正在优化提示词...'):
                generated_prompt = generate_prompt(task_or_prompt, selected_language)
                st.write(generated_prompt)

    if task_or_prompt and submitted and not uploaded_files:
        if not selected_language:
            st.error("请选择生成的提示词语言")
        else:
            with st.spinner('请稍等 :coffee: 正在优化提示词...'):
                generated_prompt = generate_prompt(task_or_prompt, selected_language)
                st.write(generated_prompt)
            
    if task_or_prompt and submitted and uploaded_files:
        if not selected_language:
            st.error("请选择生成的提示词语言")
        else:
            task_with_files = f'{task_or_prompt}\n\n 文档内容: \n{all_text}'
            with st.spinner('请稍等 :coffee: 正在优化提示词...'):
                generated_prompt = generate_prompt(task_with_files, selected_language)
                st.write(generated_prompt)

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