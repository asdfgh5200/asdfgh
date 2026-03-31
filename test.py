import streamlit as st

st.set_page_config(
    page_title="吴帅大帅哥",
    page_icon="🎧",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help':'https://www.baidu.com',
        'Report a bug':'https://www.bilibili.com/video/BV12P411u7en/?spm_id_from=333.337.search-card.all.click&vd_source=b936e27d9df7c8827fd2b08f8fa9d54d',
        'About':"爱你哦~",
    }
)

st.title("合照墙-----ws and lry")

st.audio("./resourses/周杰伦 - 晴天.mp3",start_time=0,autoplay=True,loop=1)
st.image("./resourses/01.jpg",width=500)
st.image("./resourses/02.jpg",width=500)
st.image("./resourses/03.jpg",width=500)
st.image("./resourses/04.jpg",width=500)
st.image("./resourses/05.jpg",width=500)
st.image("./resourses/06.jpg",width=500)
st.image("./resourses/07.jpg",width=500)
st.image("./resourses/08.jpg",width=500)
st.image("./resourses/09.jpg",width=500)
st.image("./resourses/10.jpg",width=500)
st.image("./resourses/11.jpg",width=500)
st.image("./resourses/12.jpg",width=500)
st.logo("./resourses/logo.png")
st.radio("请问您对本网站是否满意:",["满意","超级无敌雷霆满意"])
suggestion = st.text_input("输入评论....")
st.write("这个功能不会做嘻嘻:"+suggestion)