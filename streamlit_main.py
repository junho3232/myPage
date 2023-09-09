import streamlit as st

st.set_page_config(
    page_title= '준호홈',
    page_icon = '😁'
)

menu = st.sidebar.selectbox('MENU', ['자기소개','학교소개','동아리소개','관심분야'])
if menu == '자기소개':
    st.subheader('자기소개🤑')
    st.title('이준호')
    st.subheader('생일')
    st.subheader('2006년02월23년')
    st.subheader('취미')
    st.subheader('운동을 좋아함')
    col3, col4 = st.columns(2)
    with col3:
        image2 = ('basketball.jgp')
        st.image(image2)
    with col4:
        image3 =('축구.jgp')
        st.image(image3)


elif menu == '학교소개':
    st.subheader('학교소개')

    col1, col2 = st.columns(2)
    with col1:
        st.write('강북고등학교')
    with col2:
        image = ('schools1.jpg')
        st.image(image, width=200)
        st.subheader('일반계 고등학교')
        st.subheader('사립')
        st.subheader('교장:박종창')




elif menu == '동아리소개':
    st.subheader('동아리소개😳')

elif menu == '관심분야':
    st.subheader('관심분야')
    st.title('앱 개발자')
    st.image('1234.png')
    st.image('111.jpg')

    st.caption('https://namu.wiki/w/%EA%B0%9C%EB%B0%9C%EC%9E%90')
    st.video('https://www.youtube.com/watch?v=MvD6_eor0Kg')





