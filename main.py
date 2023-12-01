import streamlit as st 

# Title
st.image('./logo.png')
st.header('내 물건 팔기')

st.file_uploader('File uploader')

st.subheader("제목")
prod_name = st.text_input(label='', value="제목")

st.subheader("거래 방식")
st.radio('거래 방식:', ['판매하기','나눔하기'])
price = st.number_input('￦ 가격을 입력해 주세요.')
st.checkbox('가격 제안 받기')

# Text Area
st.subheader("자세한 설명")
message = st.text_area(label='', value="도곡동에 올릴 게시글 내용을 작성해주세요 (판매 금지 물품은 게시가 제한될 수 있어요)\n신뢰 할 수 있는 거래를 위해서 자세히 적어주세요. \n과학기술정보통신부, 한국인터넷진흥원과 함께 해요.")


# Text Input
st.subheader("거래희망장소")
place_to_meet = st.text_input(label='', value="Type Here ...")

if st.button('작성완료', key='complete'):
   st.write(prod_name.title()+ "\n" + message.title())
   st.toast('가격을 제안해 드려요!')
   st.toast('적정가격은...')
