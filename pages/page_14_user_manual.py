import streamlit as st

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

left_co, cent_co,last_co = st.columns([0.16,0.7,0.02])
with cent_co:
    st.title("GCP GenAI Demo用户手册")

left_co, cent_co,last_co = st.columns([0.37,0.5,0.13])
with cent_co:
    st.write("修改日期: 2024年12月10日")

st.text("")

# 创建目录
st.markdown("# 目录")

# 创建一个选择框作为导航
section = st.selectbox(
    "选择章节跳转",
    [
        "1. 介绍",
        "2. 文本生成",
        "3. 提示词生成器",
        "4. 视频理解",
        "5. 文本翻译",
        "6. 旅游顾问",
        "7. RAG搜索",
        "8. 媒体搜索",
        "9. 图片生成",
        "10. 聊天机器人",
        "11. 游戏客服平台 & 电商客服平台",
        "12. Claude 3.5聊天机器人 & Llama 3.1聊天机器人",
        "13. GCP翻译门户",
        "14. GCP控制台 - Gemini & GCP控制台 - RAG搜索",
        "15. 用户服务协议",
        "16. 用户隐私政策"
    ]
)

# 根据选择显示相应内容
if section == "1. 介绍":
    st.markdown("## 1. 介绍")
    st.markdown("""
    1. 本手册向你介绍应该如何使用GCP GenAI项目向GCP的客户演示Vertex AI相关的各种能力。  
    2. GCP GenAI web-based app虽然是一个演示性质的app，但是其中的板块，除了“RAG搜索”，“媒体搜索”，“游戏服务平台”和“电商客服平台”因囿于后端数据的局限，只有少量文档用于demo之外，其他板块，都是可以正常使用的板块。  
    3. 本应用仅作GCP Sales向客户demo用途，因此，只能使用特定邀请码登录，无法向客户开放使用。
    """)
elif section == "2. 文本生成":
    st.markdown("## 2. 文本生成")
    st.markdown("""
    1. **场景：**  
        帮助内容创作者，如编剧，网文作家，游戏剧本制作人等，根据故事大纲快速生成可用的剧本或小说。  
    2. **提示词示例：**  
        [这里](https://docs.google.com/document/d/15Nf4zkjA46wcFy_mr0miXU23w63FeauAzO5EVsVNJ80/edit?usp=sharing)  
    3. **注意事项：**  
        1. Gemini API最大output token限制是8,192个token，因此，使用文本生成功能不能生成超过8,192 token的内容。为了避免生成过长内容，上面的提示词示例中只要求生成两集剧本；  
        2. 如果要生成过长内容，请每次请求只生成一部分；  
        3. 为了保持内容一致性，可以利用Gemini的长上下文能力，将剧情大纲与之前生成的内容一起作为提示词输入，如[这篇文档](https://docs.google.com/document/d/15Nf4zkjA46wcFy_mr0miXU23w63FeauAzO5EVsVNJ80/edit?tab=t.0)中的第二段提示词。这里是提前生成好的剧本：[第1-2集](https://drive.google.com/file/d/108oUg90b9Zpfov5uH13l-TyiwAF9H8v7/view?usp=drive_link&resourcekey=0-NI1DyNOVztJ1f8AFlKOpWQ)，[第3-4集](https://drive.google.com/file/d/1l9j3tHjAQJwjCuHaQtb4E0fThvf8oM34/view?usp=drive_link&resourcekey=0-xbmijuCti5xejbs5QwkQ3w)。  
    4. **Roadmap：**  
        1. 未来版本，会接受PDF文档以及图片的上传功能。预计9月初改版（delayed with no ETA）。
    """)
elif section == "3. 提示词生成器":
    st.markdown("## 3. 提示词生成器")
    st.markdown("""
    1. **场景：**  
        如果你有一个复杂任务，需要比较复杂的提示词，可以利用提示词生成器，生成对LLM比较友好的提示词，以便让LLM更好的理解你的任务，帮助你更好的完成任务。  
    2. **提示词示例：**  
        1. 我希望利用Gemini帮我分析一个公司过去两年的财报，以便于我快速理解这个公司的业务和财务状况，从而决定是否投资这家公司。  
        2. 我想利用Gemini API和Python创建一个聊天机器人的web应用。  
    3. **注意事项：**  
        1. 复杂任务，也可以将任务描述保存在txt文件中。  
    4. **Roadmap：**  
        不定期更改系统指令，以生成更好的提示词。
    """)
elif section == "4. 视频理解":
    st.markdown("## 4. 视频理解")
    st.markdown("""
    1. **场景：**  
        与“文本生成”板块为同一条故事线：内容创作者难免有才思枯竭的时候，或者想复刻某一款流行的短剧，这时候，就可以利用Gemini的多模态能力，来根据某一个短剧，视频，或者图片，生成一个故事大纲。将生成的故事大纲，copy到“文本生成”板块中，就可以快速的制作一个新的剧本；  
    2. **提示词示例：**  
        1. 请根据[这张图片](https://drive.google.com/file/d/1bqxBUmbVNBVj81dOWro-4ieJpq-rXasW/view?usp=drive_link&resourcekey=0-PE7414xJXq7GRPPwn8hEVg)，用中文讲述一个1000字左右的故事。  
        2. 请根据[这段视频](https://drive.google.com/file/d/1BCxlmyO8mUkDDlJsi-O5CJbEVycUh6Fu/view?usp=drive_link&resourcekey=0-4azgwchGwPkZgNU0OjSURA)，用中文讲述一个1000字左右的故事。  
    3. **注意事项：**  
        1. 目前的应用是免费托管在第三方平台上，受制于第三方平台的功能及能力，文件上传时并不能成功，请尽量使用已经上传的图片和视频。  
        2. 上面的图片和视频已经上传到了存储桶中，可以直接将它们的gcs uri链接copy到GCS链接对话框中即可：  
            1. 图片：gs://lwk-rag-videos/galaxy banner with GCP logo.png  
            2. 视频：gs://lwk-rag-videos/Google \- One more day until GoogleIO.mp4  
        3. 可以在现场给客户展示一下这张图片和视频  
    4. **Roadmap：**  
        1. 未来版本，会将图片和视频上传功能改为本地解析，取消上传至GCS，这样，就可以使用你自己的图片和视频来做媒体理解的演示了。预计9月初改版（delay with no ETA）。""")
    

elif section == "5. 文本翻译":
    st.markdown("## 5. 文本翻译")
    st.markdown("""
    1. **场景：**  
        客户目前使用最多的就是翻译，无论是聊天翻译，还是内容翻译。文本翻译板块就是向客户演示Gemini的多语言能力。  
    2. **提示词示例：**  
        1. 文档：[以色列建国史](https://drive.google.com/file/d/10EziEY88MHfwJ5Vfw525jsEXcUjpzXoO/view?usp=drive_link&resourcekey=0-113NtXpeFPGpKl4bEedg8g)  
        2. 任何你自己找到的大段文字  
    3. **注意事项：**  
        1. “文本翻译”板块在代码中已经将前置提示词写好了，在提示词对话框中不需要输入任何类似“请将下面的文本翻译成英文”之类的文字。直接将需要翻译的文本copy到提示词对话框中，并在左边栏选择目标语言，点击“开始翻译”即可。  
        2. 目前版本开发的比较早，当时只做了txt文件上传。  
    4. **Roadmap：**  
        1. 未来版本，会接受PDF文档以及图片的上传，直接将PDF文档或者图片中的文字翻译成目标语言。预计9月初改版（delayed with no ETA）。  
        2. 目前很多客户的场景集中于聊天对话的翻译，未来会增加一个“聊天翻译”的板块，将利用Gemini Flash实现聊天对话的实时翻译。预计9月中旬左右上线（delayed with no ETA）。""")

elif section == "6. 旅游顾问":
    st.markdown("## 6. 旅游顾问")
    st.markdown("""
    1. **场景：**  
        帮助用户规划旅游线路。这个板块主要展示Gemini的两个主要能力  
        1. Google Search Grounding：旅游规划需要实时了解目的地的情况，包括天气，机票，以及热门景点等等，这需要LLM能够进行实时搜索。Gemini可以很好的grounding Google Search，从而提供实时信息给用户。  
        2. 生成json结构化数据的能力：板块中的“旅行信息”中的数据，都需要从Gemini生成的json格式的数据中抓取，需要格式准确。  
    2. **提示词示例：**  
        1. 我想在10月1日-7日从北京到美国加州旅游  
        2. 或者提供你自己希望的行程，请提供以下信息：日期，出发地，目的地  
    3. **注意事项：**  
        1. 虽然grouping Google Search，依然会有幻觉现象产生，所以出发地和目的地尽量选择航线枢纽城市，如北京，上海，纽约，伦敦之类的城市。  
        2. 目前版本虽然可以上传图片，文本或视频文件，初衷是希望通过图片或视频识别相关的城市或景点，从而生成旅行计划。但是因为Gemini Grounding Google Search只支持纯文本输入，不支持多模态输入，因此，暂时无法实现上述功能。  
    4. **Roadmap：**  
        1. 下一个版本，会将代码逻辑改变一下，以便在支持多模态输入的前提下，同时支持Google Search Grounding功能。预计10月初改版（delayed with no ETA）。""")

elif section == "7. RAG搜索":
    st.markdown("## 7. RAG搜索")
    st.markdown("""
    1. **场景：**  
        企业知识库搜索，企业内部文档搜索。这个板块利用了Vertex AI的Agent Builder \- Search的服务来实现。目前，Agent Builder \- Search支持三种数据集：结构化数据，非结构化数据，以及website（需要有域名所有权）。其中结构化数据不支持自然语言搜索。所以本应用采用了非结构化数据（主要是PDF文档）作为数据集。所希望实现的功能，或者满足客户的需求，是在企业内部建立一个内部文档（知识库）搜索引擎，利用自然语言搜索相关内容，并返回由Gemini总结的答案以及原文档链接。适用场景：短剧平台或编剧根据自然语言搜索某一个桥段所在的具体文档，网文作家搜索特定内容，等等。  
    2. **提示词示例：**  
        1. 有哪些对视力有益的运动？  
        2. 应该如何正确配眼镜？  
        3. 精绝古城是谁发现的？  
        4. 《恩⾥克的旅程》讲述了一个什么样的故事？  
        5. 以色列是如何建国的？  
    3. **注意事项：**  
        1. 由于只是demo环境，目前“RAG搜索”应用中的数据集里只有6份PDF文档：[以色列：一个国家的诞生](https://storage.googleapis.com/lwk-rag-search-demo/%E4%BB%A5%E8%89%B2%E5%88%97%EF%BC%9A%E4%B8%80%E4%B8%AA%E5%9B%BD%E5%AE%B6%E7%9A%84%E8%AF%9E%E7%94%9F.pdf)，[八卦微积分](https://storage.googleapis.com/lwk-rag-search-demo/%E5%85%AB%E5%8D%A6%E5%BE%AE%E7%A7%AF%E5%88%86.pdf)，[围观考古现场](https://storage.googleapis.com/lwk-rag-search-demo/%E5%9B%B4%E8%A7%82%E8%80%83%E5%8F%A4%E7%8E%B0%E5%9C%BA.pdf)，[近视怎么办](https://storage.googleapis.com/lwk-rag-search-demo/%E8%BF%91%E8%A7%86%E6%80%8E%E4%B9%88%E5%8A%9E.pdf)，[量子通信](https://storage.googleapis.com/lwk-rag-search-demo/%E9%87%8F%E5%AD%90%E9%80%9A%E4%BF%A1.pdf)。  
        2. 如果你想用自己的提示词，应当从这些文档中选择相关相关内容，而不是开放式的问题，以便有最好的RAG结果。  
    4. **Roadmap：**  
        暂无
    """)
elif section == "8. 媒体搜索":
    st.markdown("## 8. 媒体搜索")
    st.markdown("""
    1. **场景：**  
        视频平台，短剧平台，以及各种媒体平台，都需要面向最终用户提供搜索功能。这个板块同样利用了Vertex AI的Agent Builder \- Search的服务。与“RAG搜索”板块几乎完全一样。正常的媒体搜索，应当使用multimodal embedding \+ vector DB \+ Gemini来实现，但是这种方案远超我的开发能力。作为一个workaround，我将媒体的内容做成了非结构化的PDF文档，同样能够实现利用自然语言搜索媒体的功能。  
    2. **提示词示例：**  
        1. 有没有关于机器人的电影？  
        2. 请推荐一个关于冒险的电影  
        3. 我想看一部喜剧电影  
        4. 有没有关于春天的歌曲？  
        5. 有哈利波特的电影吗？  
    3. **注意事项：**  
        1. 由于只是demo环境，目前“媒体搜索”应用中的数据集里只有5个媒体数据：[哈利波特与魔法石](https://storage.googleapis.com/media-rag-search-videos/video_5.mp4), [飞屋环游记](https://storage.googleapis.com/media-rag-search-videos/video_1.mp4)，[机器人总动员](https://storage.googleapis.com/media-rag-search-videos/video_3.mp4)，[好想去你的世界爱你](https://storage.googleapis.com/media-rag-search-videos/video_2.mp4)，[春暖花开去见你](https://storage.googleapis.com/media-rag-search-videos/video_4.mp4)  
        2. 因为上述媒体内容均可以通过互联网浏览，出于版权考虑，上述内容并不是相关媒体的完整内容。  
    4. **Roadmap：**  
        暂无""")

elif section == "9. 图片生成":
    st.markdown("## 9. 图片生成")
    st.markdown("""
    1. **场景：**  
        1. 宣传海报制作  
        2. 游戏角色或场景生成  
        3. 小说配图  
        4. ……  
    2. **提示词示例：**  
        1. A beautiful ice princess with silver hair, fantasy concept art style  
        2. A tiny modern house reflecting, on a coastal cliff, 35mm lens, global illumination, natural light  
        3. In the surreal CG rendering of ancient China, there is YaoLin fairyland beside the ancient architectural town in the south of the Yangtze River. At night, the stars are bright, the smoke is charming, the maple leaves and milky leaves are trees, the snow scene, HD  
        4. A stack of books, viewed from above. The topmost book's cover has a watercolor illustration of a bird with the title: "Vertex AI".  
        5. character design  
        6. 落霞与孤鹜齐飞，秋水共长天一色  
    3. **注意事项：**  
        1. 本应用调用的是Imagen3 API，可以让客户查看细节  
        2. 每次生成的图片可以选择1-4张，图片生成以后，可以点击图片旁边的放大按钮放大图片  
    4. **Roadmap：**  
        1. 蒙版编辑：预计12月改版。  
        2. Veo：暂无时间，等待Veo GA。""")

elif section == "10. 聊天机器人":
    st.markdown("## 10. 聊天机器人")
    st.markdown("""
        1. **场景：**  
        客户内部作为生产力辅助工具，或者数字人应用，都需要聊天机器人的功能。这个板块是一个比较简单的数字人应用，虽然没有类似Character.ai那样的复杂功能，但是也是一个完整的聊天机器人，可以进行多轮对话，识别并理解图片，视频，PDF等内容。作为一个数字助手或生产力工具，帮助生成内容，理解内容，学习内容，写代码，理解代码，解释代码等等工作，都是胜任的。  
        \[9/14/24 update\]：增加了Grounding Google Search功能，目前可以使用Google Search来搜索最新的信息，例如询问：  
        * 小米SU-7的价格是多少？  
        * OpenAI的最新模型是什么？  
        * 目前美国总统大选的候选人都是谁？  
        * 或者任何世界上刚刚发生的最新的事情 😁  
        2. **提示词示例：**  
            请自由发挥  
        3. **注意事项：**  
            1. 左边栏有角色定义，预定义了两个角色，用户也可以自定义角色。  
            2. 由于本应用没有任何后端存储，包括数据库，对象存储，所有数据都是通过前端代码处理，所以本应用没有长期记忆。每次开启新的对话，此轮对话的内容是有记忆的，但是，当浏览器关闭，或者点击左边栏的“开始新的对话”按钮后，此轮对话内容便会清空，不会保留。  
        4. **Roadmap：**  
            暂时保密，敬请期待。""")
    
elif section == "11. 游戏客服平台 & 电商客服平台":
    st.markdown('## 11. 游戏客服平台 & 电商客服平台')
    st.markdown("""
        1. **场景：**  
        无论是游戏公司，还是电商平台，都会需要客服机器人。这个应用是通过Agent Builder \- Conversation 以及DialogFlow实现的。游戏客服平台，我下载了[暴雪在官网技术支持的所有文章](https://us.battle.net/support/en/help/games/services/category/808)。电商客服平台，我利用了Google Cloud的公共数据（gs://cloud-samples-data/dialogflow-cx/google-store/），是两年前Google Store的所有网页。通过这两个应用，可以向客户展示一个简单的客服机器人的方案，例如问答，提供产品信息，解决简单技术问题等等。当然，实际的客服机器人，或者DialogFlow能够实现的功能，远远超过本应用所能实现的功能。这个应用仅仅是向客户展示通过Vertex AI Agent Builder \+ DialogFlow，是完全可以实现企业级的客服机器人的。  
        2. **提示词示例：**  
        1. My battle.net agent is stuck when it was updating  
        2. I got error code BLZBNTAGT00000841, what’s that mean? How to fix it?  
        3. Does my iPad Pro 2 support Diablo Immortal’s ultra resolution?  
        4. My PC can’t play Diablo 3, why is that?  
        5. Can you give me some information about Pixel 7?  
        6. Do you have Pixel Watch?  
        3. **注意事项：**  
        1. 因为这两个应用使用的是同一个项目，而我使用的是直接集成DialogFlow应用的方式，而不是通过SDK方式开发的，所以如果在同一个页面上切换两个应用时，例如从“游戏客服平台”直接切换至“电商客服平台”（或者相反）时，聊天窗口内会保留前一个客服平台的对话记录，为了防止这种事情发生，我在代码中特意做了“在新浏览器标签页中打开”的逻辑，即，当用户从“游戏客服平台”切换至“电商客服平台”（或相反）时，会新打开一个浏览器标签页，这时需要重新用你的Google公司账号登录一次，才能进入。而从任何其他应用页面进入这两个应用其中之一时，则不会如此。  
        2. 目前这两个应用都接受中文对话，但是机器人返回的结果并不一定准确。  
        4. **Roadmap：**  
        暂无""")

elif section == "12. Claude 3.5聊天机器人 & Llama 3.1聊天机器人":
    st.markdown('## 12. Claude 3.5聊天机器人 & Llama 3.1聊天机器人')
    st.markdown("""
        1. **场景：**  
        这两个应用的场景与[聊天机器人](#bookmark=id.2jxsxqh)的场景完全一致，只不过改用了Vertex AI上的Claude 3.5 API和Llama 3.1 API，后端的大模型也就是相应的这两个大模型。其他没有什么特别之处。  
        2. **提示词示例：**  
        请自由发挥。  
        3. **注意事项：**  
        1. Claude 3.5 API目前是准多模态，只支持图片输入，不支持音频视频PDF等格式。Llama 3.1目前只是纯文本大模型，不是多模态大模型，所以我没有做任何多模态内容输入的功能。  
        4. **Raodmap：**  
        依赖于Anthropic和Meta的update，如果有新的模型发布，我会第一时间集成到应用中。""")

elif section == "13. GCP翻译门户":
    st.markdown('## 13. GCP翻译门户')
    st.markdown("""

        1. **场景：**  
        这是GCP官方做的一个翻译门户网站，可以直接给最终用户使用，但是其使用的是Google Translate的机器翻译，也就是Translate API，翻译质量肯定不如Gemini的翻译质量。其优势在于可以给它一份PDF，Word或者PPT文件，它会按照原格式输出翻译好的文件。但是这个服务比较贵，按照页数收费，每页$0.15-0.5，具体的收费标准可以参考[这里](https://pantheon.corp.google.com/translation/hub)。  
        2. **提示词示例：**  
        无  
        3. **注意事项：**  
        无  
        4. **Roadmap：**  
        无""")

elif section == "14. GCP控制台 \- Gemini & GCP控制台 \- RAG搜索":
    st.markdown('## 14. GCP控制台 \- Gemini & GCP控制台 \- RAG搜索')
    st.markdown("""
        这是GCP的控制台界面入口，目的是为了给客户展示GCP控制台Gemini的界面，以及如何通过图形界面（no code）来搭建一个完整的RAG搜索。没有特别之处。自己熟悉一下就可以。""")

elif section == "15. 用户服务协议":
    st.markdown("""15. # [用户服务协议](https://gcp-genai-zh.streamlit.app/terms_of_service) """)

elif section == "16. 用户隐私政策":
    st.markdown("""16. # [用户隐私政策](https://gcp-genai-zh.streamlit.app/privacy_policy)""")

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