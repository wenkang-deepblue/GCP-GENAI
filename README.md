# GCP-GenAI Project README

### Introduction

The GCP GenAI project is a generative AI application built based on the Google Cloud Vertex AI platform. It aims to demonstrate the powerful capabilities of Vertex AI in areas such as content generation, media understanding, RAG (Retrieval Augmented Generation) search, image generation, chatbots, and customer service bots. This project utilizes various Vertex AI and third-party models and services, including Gemini 1.5 Pro/Flash multimodal models, Agent Builder - Vertex AI Search, Imagen, DialogFlow CX, Anthropic Claude 3.5 Sonnet - Vertex AI Model Garden, and Meta Llama 3.1 - Vertex AI Model Garden.

### Project Structure

-   `homepage.py`: Project homepage, providing an overview and navigation.
-   `auth.py`: Handles user invite code login authentication.
-   `components.py`: Contains reusable Streamlit components used across multiple pages.
-   `pages/`: Contains subpages for different functional modules.

### Functional Modules

#### 1. Text Generation - `pages/page_01_text_generation.py`
Provides a text content generation platform. Users can input prompts, upload text documents, and adjust model parameters (Temperature, Top-p) to generate various types of text content, such as stories, scripts, etc.

#### 2. Video Understanding - `pages/page_02_media_understanding.py`
Users can upload video (mp4, wmv) or image (jpg, png) files to GCS, or directly input a GCS link. Then, based on the media content and custom prompts, users can generate text descriptions, analyses, or summaries.

#### 3. Text Translation - `pages/page_03_translation.py`
Enterprise-grade text translation platform. Supports uploading text documents or directly inputting text, and selecting a target language (including Chinese, English, Japanese, Korean, French, German, and many others) for translation.

#### 4. Travel Advisor - `pages/page_04_travel_advisor.py`
An intelligent travel advisor chatbot. Utilizes Gemini 1.5 Pro and Google Search grounding to provide users with personalized travel advice, including destination introductions, weather, attractions, flight information (with prices, considering time differences), shopping, and dining recommendations, returning some information in a structured JSON format.

#### 5. RAG Search - `pages/page_05_rag_search.py`
Enterprise-grade RAG search engine. Users can ask natural language questions against a pre-set knowledge base (PDF documents), and the system will return AI-generated summaries with citations and links to relevant documents.

#### 6. Media Search - `pages/page_06_media_search.py`
Enterprise-grade media content search engine. Similar to RAG search but for media content (achieved through descriptive documents). Users can search for video or image content using natural language and get links to relevant media.

#### 7. Image Generation - `pages/page_07_image_generation.py`
Provides image generation functionality based on the Vertex AI Imagen 3 model. Users can input prompts, select the number of images to generate, and choose the aspect ratio to create high-quality images.

#### 8. Chatbot - `pages/page_08_chatbot.py`
A general-purpose enterprise-grade chatbot based on Gemini 1.5 Pro. Users can select the AI's role (e.g., friendly assistant, Python expert) or define a custom role. Supports file uploads (PDF, TXT) and Google Search grounding.

#### 9. Gaming Servicebot - `pages/page_09_gaming_servicebot.py`
Embeds a DialogFlow CX-based customer service bot for the gaming industry to demonstrate handling game-related user inquiries.

#### 10. E-commerce Servicebot - `pages/page_10_ecommerce_servicebot.py`
Embeds a DialogFlow CX-based customer service bot for the e-commerce industry to demonstrate handling e-commerce-related user inquiries.

#### 11. Claude 3.5 Chatbot - `pages/page_11_claude_chatbot.py`
A chatbot based on the Anthropic Claude 3.5 Sonnet model. Users can select AI roles, and it supports streaming output and image uploads for multimodal interaction.

#### 12. Llama 3.1 Chatbot - `pages/page_12_llama_chatbot.py`
A chatbot based on the Meta Llama 3.1 (405B instruct model), accessed via Vertex AI's OpenAI-compatible endpoint. Users can select AI roles and adjust model parameters.

#### 13. Prompt Generator - `pages/page_13_prompt_generator.py`
Enterprise-grade LLM prompt generator. Users can input task descriptions or existing prompts, select the output language (Chinese/English), and the system will use Gemini 1.5 Pro to generate a more optimized and structured system prompt.

#### 14. Vibtitle - [Vibtitle](https://vibtitle-en.deepblue.cc)
An powerful tool to automatically generate video subtitles and translate to specified language.

#### 15. User Manual - `pages/page_14_user_manual.py`
A detailed user manual introducing the use cases, prompt examples, precautions, and future roadmap for each functional module in the project.

### How to Run

1.  Ensure Python and Streamlit are installed.
2.  Clone the repository.
3.  Install dependencies with this command: `pip install -r requirements.txt`.
3.  Create a `.streamlit/secrets.toml` file in the root directory of the repository and configure the necessary credentials, such as `INVITE_CODES`, `GOOGLE_APPLICATION_CREDENTIALS` (GCP service account key as a JSON string). If needed, set up: `developer_profile_link`, `developer_name`, `developer_email`, `manual_link`.
4.  Run `streamlit run homepage.py` in your terminal.
5.  Access the application via your browser and log in using a valid invite code.

### Dependencies

Major dependencies include:
-   streamlit
-   google-cloud-aiplatform
-   google-auth
-   google-cloud-storage
-   requests
-   anthropic_vertex
-   openai
-   PyPDF2
-   Pillow

Please refer to the import statements in individual Python files for detailed dependencies.

---

### 简介

GCP GenAI 项目是一个基于 Google Cloud Vertex AI 平台搭建的生成式 AI 应用。它旨在演示 Vertex AI 在内容生成、媒体理解、RAG (Retrieval Augmented Generation) 搜索、图片生成、聊天机器人以及客服机器人等方面的强大能力。本项目使用了包括 Gemini 1.5 Pro/Flash 多模态模型, Agent Builder - Vertex AI Search, Imagen, DialogFlow CX, Vertex AI Model Garden 中的 Anthropic Claude 3.5 Sonnet, 和 Meta Llama 3.1 在内的多种 Vertex AI 及第三方模型和服务。

### 项目结构

-   `homepage.py`: 项目主页，提供项目概览和导航。
-   `auth.py`: 处理用户邀请码登录认证。
-   `components.py`: 包含一些在多个页面中复用的Streamlit组件。
-   `pages/`: 包含各个功能模块的子页面。

### 功能模块

#### 1. 文本生成 - `pages/page_01_text_generation.py`
提供一个文本内容生成平台。用户可以输入提示词，上传文本文档，调整模型参数（Temperature, Top-p），以生成各种类型的文本内容，如故事、剧本等。

#### 2. 视频理解 - `pages/page_02_media_understanding.py`
用户可以上传视频（mp4, wmv）或图片（jpg, png）文件到 GCS，或直接输入 GCS 链接。然后，用户可以基于媒体内容和自定义提示词，生成文本描述、分析或摘要。

#### 3. 文本翻译 - `pages/page_03_translation.py`
企业级文本翻译平台。支持上传文本文档或直接输入文本，并选择目标语言（包括中、英、日、韩、法、德等多种语言）进行翻译。

#### 4. 旅游顾问 - `pages/page_04_travel_advisor.py`
一个智能旅游顾问聊天机器人。利用 Gemini 1.5 Pro 和 Google Search grounding 功能，为用户提供个性化的旅行建议，包括目的地介绍、天气、景点、航班信息（含价格，考虑时差）、购物和餐饮推荐，并以结构化的 JSON 格式返回部分信息。

#### 5. RAG搜索 - `pages/page_05_rag_search.py`
企业级 RAG 搜索引擎。用户可以针对预设的知识库（PDF文档）进行自然语言提问，系统会返回由 AI 生成的摘要以及相关文档的引用和链接。

#### 6. 媒体搜索 - `pages/page_06_media_search.py`
企业级媒体内容搜索引擎。与 RAG 搜索类似，但针对媒体内容（通过描述性文档实现）。用户可以用自然语言搜索视频或图片内容，并获得相关媒体的链接。

#### 7. 图片生成 - `pages/page_07_image_generation.py`
基于 Vertex AI Imagen 3 模型，提供图片生成功能。用户可以输入提示词，选择生成图片的数量和宽高比，生成高质量图片。

#### 8. 聊天机器人 - `pages/page_08_chatbot.py`
一个通用的企业级聊天机器人，基于 Gemini 1.5 Pro。用户可以选择 AI 的角色（如友好助手、Python专家）或自定义角色。支持文件上传（PDF, TXT）和 Google Search grounding 功能。

#### 9. 游戏客服平台 - `pages/page_09_gaming_servicebot.py`
嵌入了一个基于 DialogFlow CX 的游戏行业客服机器人，用于演示如何处理游戏相关的用户咨询。

#### 10. 电商客服平台 - `pages/page_10_ecommerce_servicebot.py`
嵌入了一个基于 DialogFlow CX 的电商行业客服机器人，用于演示如何处理电商相关的用户咨询。

#### 11. Claude3.5聊天机器人 - `pages/page_11_claude_chatbot.py`
一个基于 Anthropic Claude 3.5 Sonnet 模型的聊天机器人。用户可以选择 AI 角色，支持流式输出和图片上传进行多模态交互。

#### 12. Llama3.1聊天机器人 - `pages/page_12_llama_chatbot.py`
一个基于 Meta Llama 3.1 (405B 指令模型) 的聊天机器人，通过 Vertex AI 的 OpenAI 兼容端点访问。用户可以选择 AI 角色并调整模型参数。

#### 13. 提示词生成器 - `pages/page_13_prompt_generator.py`
企业级 LLM 提示词生成器。用户可以输入任务描述或现有提示词，并选择输出语言（中/英），系统会利用 Gemini 1.5 Pro 生成一个更优化的、结构化的系统提示词。

#### 14. Vibtitle - [Vibtitle](https://vibtitle.deepblue.cc)
一个自动生成并翻译视频字幕的强大工具。

#### 14. 用户手册 - `pages/page_14_user_manual.py`
详细的用户手册，介绍了项目中各个功能模块的使用场景、提示词示例、注意事项和未来规划。

### 如何运行

1.  确保已安装 Python 和 Streamlit。
2.  克隆代码库。
3.  使用以下命令安装所有依赖：`pip install -r requirements.txt`。
4.  在代码库根目录创建 `.streamlit/secrets.toml` 文件，并配置必要的凭据，例如 `INVITE_CODES`, `GOOGLE_APPLICATION_CREDENTIALS` (JSON 字符串形式的服务账号密钥), 如有需要，请配置：`developer_profile_link`, `developer_name`, `developer_email`, `manual_link`。
5.  在终端中运行 `streamlit run homepage.py`。
6.  通过浏览器访问应用，并使用有效的邀请码登录。

### 依赖

主要依赖项包括:
-   streamlit
-   google-cloud-aiplatform
-   google-auth
-   google-cloud-storage
-   requests
-   anthropic_vertex
-   openai
-   PyPDF2
-   Pillow

详细依赖请查看各个 Python 文件中的导入语句。