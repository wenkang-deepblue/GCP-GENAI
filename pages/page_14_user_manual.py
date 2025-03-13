import streamlit as st
from components import chinese_version_link, save_invite_code

st.set_page_config(
    page_title="GCP GenAI",
    page_icon="👋",
)

save_invite_code()

with st.sidebar:
    st.markdown(chinese_version_link(), unsafe_allow_html=True)
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

left_co, cent_co,last_co = st.columns([0.15,0.75,0.1])
with cent_co:
    st.title("GCP GenAI Demo Manual")

left_co, cent_co,last_co = st.columns([0.37,0.5,0.13])
with cent_co:
    st.write("Effective Date: December 10, 2024")

st.text("")

# Create table of contents
st.markdown("# Table of Contents")

# Create a selection box as navigation
section = st.selectbox(
    "Select section to navigate",
    [
        "1. Introduction",
        "2. Text Generation",
        "3. Prompt Generator",
        "4. Video Understanding",
        "5. Text Translation",
        "6. Travel Advisor",
        "7. RAG Search",
        "8. Media Search",
        "9. Image Generation",
        "10. Chatbot",
        "11. Gaming Service Platform & E-commerce Service Platform",
        "12. Claude 3.5 Chatbot & Llama 3.1 Chatbot",
        "13. GCP Translation Hub",
        "14. GCP Console - Gemini & GCP Console - RAG Search",
        "15. Terms of Service",
        "16. Privacy Policy"
    ]
)

# Display content based on selection
if section == "1. Introduction":
    st.markdown("## 1. Introduction")
    st.markdown("""
    1. This manual introduces how to use the GCP GenAI project to demonstrate various Vertex AI capabilities to GCP customers.  
    2. Although the GCP GenAI web-based app is a demonstration app, all sections except "RAG Search," "Media Search," "Gaming Service Platform," and "E-commerce Service Platform" (which are limited by backend data with only a few documents for demo purposes) are fully functional.  
    3. This application is only for GCP Sales demo purposes to customers, so it can only be accessed with specific invitation codes and cannot be made available for customer use.
    """)
elif section == "2. Text Generation":
    st.markdown("## 2. Text Generation")
    st.markdown("""
    1. **Scenario:**  
        Help content creators such as screenwriters, web fiction writers, game script creators, etc., to quickly generate usable scripts or novels based on story outlines.  
    2. **Prompt Examples:**  
        [Here](https://storage.googleapis.com/lwk-rag-videos/drama_prompt.txt)  
    3. **Notes:**  
        1. Gemini API has a maximum output token limit of 8,192 tokens, so the text generation feature cannot generate content exceeding 8,192 tokens. To avoid generating overly long content, the prompt examples above only request two episodes of script;  
        2. If you need to generate longer content, please request only one part at a time;  
        3. To maintain content consistency, you can leverage Gemini's long context capability by including both the plot outline and previously generated content as input prompts, as shown in the second paragraph of prompts in [this document](https://storage.googleapis.com/lwk-rag-videos/drama_prompt.txt). Here are pre-generated scripts: [Episodes 1-2](https://storage.googleapis.com/lwk-rag-videos/%E7%9F%AD%E5%89%A7%E5%89%A7%E6%9C%AC(1-2%E9%9B%86).txt), [Episodes 3-4](https://storage.googleapis.com/lwk-rag-videos/%E7%9F%AD%E5%89%A7%E5%89%A7%E6%9C%AC(3-4%E9%9B%86).txt).  
    4. **Roadmap:**  
        1. Future versions will accept PDF documents and image uploads. Expected in early September (delayed with no ETA).
    """)
elif section == "3. Prompt Generator":
    st.markdown("## 3. Prompt Generator")
    st.markdown("""
    1. **Scenario:**  
        If you have a complex task requiring sophisticated prompts, you can use the prompt generator to create LLM-friendly prompts that help the LLM better understand your task and assist you more effectively.  
    2. **Prompt Examples:**  
        1. I want to use Gemini to analyze a company's financial reports from the past two years to quickly understand the company's business and financial situation, helping me decide whether to invest in this company.  
        2. I want to create a chatbot web application using Gemini API and Python.  
    3. **Notes:**  
        1. For complex tasks, you can also save the task description in a txt file.  
    4. **Roadmap:**  
        Periodic updates to system instructions to generate better prompts.
    """)
elif section == "4. Video Understanding":
    st.markdown("## 4. Video Understanding")
    st.markdown("""
    1. **Scenario:**  
        This follows the same storyline as the "Text Generation" section: content creators inevitably face creative blocks or want to recreate popular short dramas. In these cases, they can leverage Gemini's multimodal capabilities to generate a story outline based on a short drama, video, or image. By copying the generated outline to the "Text Generation" section, they can quickly create a new script.  
    2. **Prompt Examples:**  
        1. Please create a story of about 1000 words in English based on [this image](https://storage.googleapis.com/lwk-rag-videos/galaxy%20banner%20with%20GCP%20logo.png).  
        2. Please create a story of about 1000 words in English based on [this video](https://storage.googleapis.com/lwk-rag-videos/Google%20-%20One%20more%20day%20until%20GoogleIO.mp4).  
    3. **Notes:**  
        1. The current application is freely hosted on a third-party platform, limited by the platform's functionality and capabilities. File uploads may not work successfully, so please try to use already uploaded images and videos.  
        2. The above images and videos have already been uploaded to the storage bucket, and you can directly copy their GCS URI links to the GCS link dialog box:  
            1. Image: gs://lwk-rag-videos/galaxy banner with GCP logo.png  
            2. Video: gs://lwk-rag-videos/Google \- One more day until GoogleIO.mp4  
        3. You can show these images and videos to customers on-site.  
    4. **Roadmap:**  
        1. Future versions will change the image and video upload functionality to local parsing, eliminating the need to upload to GCS. This will allow you to use your own images and videos for media understanding demonstrations. Expected in early September (delayed with no ETA).""")
    

elif section == "5. Text Translation":
    st.markdown("## 5. Text Translation")
    st.markdown("""
    1. **Scenario:**  
        Translation is currently one of the most used features by customers, whether for chat translation or content translation. The Text Translation section demonstrates Gemini's multilingual capabilities to customers.  
    2. **Prompt Examples:**  
        1. Texts:  
                        第⼀章 ⽤铅笔创造出来的国家  
        1915 年 12 ⽉ 16 ⽇，在伦敦唐宁街 10 号的⾸相官邸中，⼏个英国  
        ⼈⽤⼀根铅笔和⼀张地图对⼏千公⾥外的中东⼟地进⾏了分割。  
        此时，第⼀次世界⼤战已经爆发⼀年多，对阵的双⽅分别是以英  
        国、法国、俄国为⾸的协约国，以及由德国、奥匈帝国、奥斯曼帝国  
        组成的同盟国。这些英国⼈此次坐在⼀起，是为了讨论如何把奥斯曼  
        帝国作为未来的战利品在协约国之间进⾏切分。  
        其中⼀个叫做赛克斯（Sykes）的⼈提议说，不如⼤家从地图左边  
        的城市 Acre 的字⺟ e 开始，画⼀条直线到地图右边 Kirkuk 的最后⼀  
        个字⺟ k 上⾯；直线以上的区域为法国的势⼒范围，直线以下的区域  
        为英国的势⼒范围。在座的⼈都觉得这条直线既简单⼜清楚，于是这  
        个提议很快就得到了英国⾸相的同意。  
        在与法国进⾏商议后，法国⼈也同意了以这条直线来划分英法两国  
        在中东的势⼒范围。双⽅于次年的 5 ⽉ 16 ⽇签署了赛克斯-⽪克特秘  
        密协定（Sykes-Picot Agreement），将这条⽤铅笔画下的直线以条约的  
        形式确定了下来。协议中还规定，英法有权在各⾃势⼒范围内进⼀步  
        划定国家间的边界。  
        2. Any large text you can find yourself  
    3. **Notes:**  
        1. The "Text Translation" section already has pre-written prompts in the code, so you don't need to enter any text like "Please translate the following text into English" in the prompt dialog box. Simply copy the text you want to translate into the prompt dialog box, select the target language in the left sidebar, and click "Start Translation".  
        2. The current version was developed early on and only supports txt file uploads.  
    4. **Roadmap:**  
        1. Future versions will accept PDF documents and image uploads, directly translating text from PDF documents or images into the target language. Expected in early September (delayed with no ETA).  
        2. Currently, many customer scenarios focus on chat translation. In the future, a "Chat Translation" section will be added, using Gemini Flash to achieve real-time translation of chat conversations. Expected to launch around mid-September (delayed with no ETA).""")

elif section == "6. Travel Advisor":
    st.markdown("## 6. Travel Advisor")
    st.markdown("""
    1. **Scenario:**  
        Help users plan travel routes. This section mainly showcases two key capabilities of Gemini:  
        1. Google Search Grounding: Travel planning requires real-time understanding of the destination, including weather, flights, and popular attractions. This requires the LLM to perform real-time searches. Gemini can effectively ground Google Search to provide users with real-time information.  
        2. Ability to generate structured JSON data: The data in the "Travel Information" section needs to be extracted from JSON-formatted data generated by Gemini, requiring accurate formatting.  
    2. **Prompt Examples:**  
        1. I want to travel from Beijing to California, USA from October 1-7  
        2. Or provide your own desired itinerary with the following information: dates, departure location, destination  
    3. **Notes:**  
        1. Despite grounding Google Search, hallucinations may still occur, so it's best to choose airline hub cities as departure and destination points, such as Beijing, Shanghai, New York, London, etc.  
        2. Although the current version can upload images, text, or video files, the original intention was to recognize relevant cities or attractions through images or videos to generate travel plans. However, since Gemini Grounding Google Search only supports plain text input and not multimodal input, this functionality cannot be implemented at this time.  
    4. **Roadmap:**  
        1. The next version will change the code logic to support Google Search Grounding functionality while also supporting multimodal input. Expected in early October (delayed with no ETA).""")

elif section == "7. RAG Search":
    st.markdown("## 7. RAG Search")
    st.markdown("""
    1. **Scenario:**  
        Enterprise knowledge base search, internal document search. This section uses Vertex AI's Agent Builder - Search service. Currently, Agent Builder - Search supports three types of datasets: structured data, unstructured data, and websites (requiring domain ownership). Structured data does not support natural language search. Therefore, this application uses unstructured data (mainly PDF documents) as the dataset. The desired functionality, or to meet customer needs, is to establish an internal document (knowledge base) search engine within the enterprise, using natural language to search for relevant content and return answers summarized by Gemini along with links to the original documents. Applicable scenarios: short drama platforms or screenwriters searching for specific plot points in documents, web fiction writers searching for specific content, etc.  
    2. **Prompt Examples:**  
        1. What exercises are beneficial for eyesight?  
        2. How should I properly get fitted for glasses?  
        3. Who discovered the ancient city of Jingjue?  
        4. What kind of story does "Enrique's Journey" tell?  
        5. How was Israel established?  
    3. **Notes:**  
        1. As this is only a demo environment, the current "RAG Search" application dataset only contains 6 PDF documents: [Israel: The Birth of a Nation](https://storage.googleapis.com/lwk-rag-search-demo/%E4%BB%A5%E8%89%B2%E5%88%97%EF%BC%9A%E4%B8%80%E4%B8%AA%E5%9B%BD%E5%AE%B6%E7%9A%84%E8%AF%9E%E7%94%9F.pdf), [Gossip Calculus](https://storage.googleapis.com/lwk-rag-search-demo/%E5%85%AB%E5%8D%A6%E5%BE%AE%E7%A7%AF%E5%88%86.pdf), [Observing Archaeological Sites](https://storage.googleapis.com/lwk-rag-search-demo/%E5%9B%B4%E8%A7%82%E8%80%83%E5%8F%A4%E7%8E%B0%E5%9C%BA.pdf), [What to Do About Nearsightedness](https://storage.googleapis.com/lwk-rag-search-demo/%E8%BF%91%E8%A7%86%E6%80%8E%E4%B9%88%E5%8A%9E.pdf), [Quantum Communication](https://storage.googleapis.com/lwk-rag-search-demo/%E9%87%8F%E5%AD%90%E9%80%9A%E4%BF%A1.pdf).  
        2. If you want to use your own prompts, you should select relevant content from these documents rather than open-ended questions to get the best RAG results.  
    4. **Roadmap:**  
        None
    """)
elif section == "8. Media Search":
    st.markdown("## 8. Media Search")
    st.markdown("""
    1. **Scenario:**  
        Video platforms, short drama platforms, and various media platforms all need to provide search functionality to end users. This section also uses Vertex AI's Agent Builder - Search service. It is almost identical to the "RAG Search" section. Normally, media search should be implemented using multimodal embedding + vector DB + Gemini, but this solution far exceeds my development capabilities. As a workaround, I've converted media content into unstructured PDF documents, which still enables natural language search for media.  
    2. **Prompt Examples:**  
        1. Are there any movies about robots?  
        2. Please recommend a movie about adventure  
        3. I want to watch a comedy movie  
        4. Are there any songs about spring?  
        5. Are there any Harry Potter movies?  
    3. **Notes:**  
        1. As this is only a demo environment, the current "Media Search" application dataset only contains 5 media items: [Harry Potter and the Philosopher's Stone](https://storage.googleapis.com/media-rag-search-videos/video_5.mp4), [Up](https://storage.googleapis.com/media-rag-search-videos/video_1.mp4), [WALL-E](https://storage.googleapis.com/media-rag-search-videos/video_3.mp4), [I Want to Go to Your World to Love You](https://storage.googleapis.com/media-rag-search-videos/video_2.mp4), [Spring Flowers Bloom to See You](https://storage.googleapis.com/media-rag-search-videos/video_4.mp4)  
        2. Because the above media content can be browsed through the internet, for copyright considerations, the above content is not the complete content of the relevant media.  
    4. **Roadmap:**  
        None""")

elif section == "9. Image Generation":
    st.markdown("## 9. Image Generation")
    st.markdown("""
    1. **Scenario:**  
        1. Promotional poster creation  
        2. Game character or scene generation  
        3. Novel illustrations  
        4. ……  
    2. **Prompt Examples:**  
        1. A beautiful ice princess with silver hair, fantasy concept art style  
        2. A tiny modern house reflecting, on a coastal cliff, 35mm lens, global illumination, natural light  
        3. In the surreal CG rendering of ancient China, there is YaoLin fairyland beside the ancient architectural town in the south of the Yangtze River. At night, the stars are bright, the smoke is charming, the maple leaves and milky leaves are trees, the snow scene, HD  
        4. A stack of books, viewed from above. The topmost book's cover has a watercolor illustration of a bird with the title: "Vertex AI".  
        5. character design  
        6. Sunset and lonely birds flying together, autumn waters and sky sharing the same color  
    3. **Notes:**  
        1. This application calls the Imagen3 API, allowing customers to view details  
        2. You can choose to generate 1-4 images each time, and after the images are generated, you can click the zoom button next to the image to enlarge it  
    4. **Roadmap:**  
        1. Mask editing: Expected revision in December.  
        2. Veo: No timeline yet, waiting for Veo GA.""")

elif section == "10. Chatbot":
    st.markdown("## 10. Chatbot")
    st.markdown("""
        1. **Scenario:**  
        Customers need chatbot functionality for internal productivity assistance tools or digital human applications. This section is a relatively simple digital human application. Although it doesn't have complex features like Character.ai, it is a complete chatbot that can engage in multi-turn conversations, recognize and understand images, videos, PDFs, and other content. As a digital assistant or productivity tool, it is capable of helping generate content, understand content, learn content, write code, understand code, explain code, and other tasks.  
        \[9/14/24 update\]: Added Grounding Google Search functionality, now able to use Google Search to find the latest information, for example asking:  
        * What is the price of Xiaomi SU-7?  
        * What is OpenAI's latest model?  
        * Who are the current candidates in the US presidential election?  
        * Or any of the latest things happening in the world 😁  
        2. **Prompt Examples:**  
            Feel free to experiment  
        3. **Notes:**  
            1. The left sidebar has role definitions, with two predefined roles, and users can also customize roles.  
            2. Since this application has no backend storage, including databases or object storage, all data is processed through frontend code, so this application has no long-term memory. Each time a new conversation is started, the content of this round of conversation is remembered, but when the browser is closed or the "Start New Conversation" button in the left sidebar is clicked, the content of this round of conversation will be cleared and not retained.  
        4. **Roadmap:**  
            Temporarily confidential, stay tuned.""")
    
elif section == "11. Gaming Service Platform & E-commerce Service Platform":
    st.markdown('## 11. Gaming Service Platform & E-commerce Service Platform')
    st.markdown("""
        1. **Scenario:**  
        Both gaming companies and e-commerce platforms need customer service chatbots. This application is implemented through Agent Builder - Conversation and DialogFlow. For the Gaming Service Platform, I downloaded [all articles from Blizzard's official website technical support](https://us.battle.net/support/en/help/games/services/category/808). For the E-commerce Service Platform, I used Google Cloud's public data (gs://cloud-samples-data/dialogflow-cx/google-store/), which contains all web pages from Google Store two years ago. Through these two applications, I can show customers a simple customer service chatbot solution, such as Q&A, providing product information, solving simple technical problems, etc. Of course, the actual customer service chatbot, or the functions that DialogFlow can achieve, far exceed what this application can achieve. This application is merely to show customers that through Vertex AI Agent Builder + DialogFlow, it is entirely possible to implement an enterprise-grade customer service chatbot.  
        2. **Prompt Examples:**  
        1. My battle.net agent is stuck when it was updating  
        2. I got error code BLZBNTAGT00000841, what's that mean? How to fix it?  
        3. Does my iPad Pro 2 support Diablo Immortal's ultra resolution?  
        4. My PC can't play Diablo 3, why is that?  
        5. Can you give me some information about Pixel 7?  
        6. Do you have Pixel Watch?  
        3. **Notes:**  
        1. Because these two applications use the same project, and I'm using direct integration of DialogFlow applications rather than developing through the SDK, if you switch between the two applications on the same page, such as directly switching from "Gaming Service Platform" to "E-commerce Service Platform" (or vice versa), the chat window will retain the conversation history from the previous customer service platform. To prevent this, I've specifically implemented "open in a new browser tab" logic in the code. That is, when a user switches from "Gaming Service Platform" to "E-commerce Service Platform" (or vice versa), a new browser tab will open, requiring you to log in again with your Google company account to enter. This doesn't happen when entering either of these two applications from any other application page.  
        2. Currently, both applications accept Chinese conversations, but the results returned by the chatbot may not always be accurate.  
        4. **Roadmap:**  
        None""")

elif section == "12. Claude 3.5 Chatbot & Llama 3.1 Chatbot":
    st.markdown('## 12. Claude 3.5 Chatbot & Llama 3.1 Chatbot')
    st.markdown("""
        1. **Scenario:**  
        The scenarios for these two applications are identical to the [Chatbot](#bookmark=id.2jxsxqh) scenario, except they use the Claude 3.5 API and Llama 3.1 API on Vertex AI, with the backend large models being the respective models. There are no other special features.  
        2. **Prompt Examples:**  
        Feel free to experiment.  
        3. **Notes:**  
        1. The Claude 3.5 API is currently quasi-multimodal, supporting only image input, not audio, video, PDF, or other formats. Llama 3.1 is currently only a pure text large model, not a multimodal large model, so I haven't implemented any multimodal content input functionality.  
        4. **Roadmap:**  
        Dependent on updates from Anthropic and Meta. If new models are released, I will integrate them into the application immediately.""")

elif section == "13. GCP Translation Hub":
    st.markdown('## 13. GCP Translation Hub')
    st.markdown("""

        1. **Scenario:**  
        This is an official GCP translation portal website that can be used directly by end users, but it uses Google Translate's machine translation, i.e., the Translate API, so the translation quality is definitely not as good as Gemini's translation quality. Its advantage is that you can give it a PDF, Word, or PPT file, and it will output the translated file in the original format. However, this service is relatively expensive, charging by page, $0.15-0.5 per page. For specific pricing, please refer to [here](https://pantheon.corp.google.com/translation/hub).  
        2. **Prompt Examples:**  
        None  
        3. **Notes:**  
        None  
        4. **Roadmap:**  
        None""")

elif section == "14. GCP Console \- Gemini & GCP Console \- RAG Search":
    st.markdown('## 14. GCP Console \- Gemini & GCP Console \- RAG Search')
    st.markdown("""
        These are entry points to the GCP console interface, aimed at showing customers the GCP console Gemini interface and how to build a complete RAG search through a graphical interface (no code). There's nothing special about it. Just familiarize yourself with it.""")

elif section == "15. Terms of Service":
    st.markdown("""15. # [Terms of Service](https://gcp-genai-zh.streamlit.app/terms_of_service) """)

elif section == "16. Privacy Policy":
    st.markdown("""16. # [Privacy Policy](https://gcp-genai-zh.streamlit.app/privacy_policy)""")


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