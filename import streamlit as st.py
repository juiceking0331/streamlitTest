import streamlit as st

st.title('웹어플만들기')

st.header('🤖 사용자 입력')

text = st.text_input('여기에 텍스트를 입력하세요') # 텍스트 입력은 입력된 값을 반환
st.write(f'입력된 텍스트: {text}')

number = st.number_input('여기에 숫자를 입력하세요') # 숫자 입력은 입력된 값을 반환
st.write(f'입력된 숫자: {number}')

check = st.checkbox('여기를 체크하세요') # 체크박스는 True/False 값을 반환
if check:
    st.write('체크되었습니다.')

radio = st.radio('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3']) # 라디오 버튼은 선택된 값을 반환
st.write(radio+'가 선택되었습니다.')

select = st.selectbox('여기에서 선택하세요', ['선택 1', '선택 2', '선택 3']) # 셀렉트박스는 선택된 값을 반환
st.write(select+'가 선택되었습니다.')

slider = st.slider('여기에서 값을 선택하세요', 0, 100, 50) # 슬라이더는 선택된 값을 반환
st.write(f'현재의 값은 {slider} 입니다.')

multi = st.multiselect('여기에서 여러 값을 선택하세요', ['선택 1', '선택 2', '선택 3']) # 멀티셀렉트박스는 선택된 값을 리스트로 반환
st.write(f'{type(multi) = }, {multi}가 선택되었습니다.')

button = st.button('여기를 클릭하세요') # 버튼은 클릭 여부를 반환
if button:
    st.write('버튼이 클릭되었습니다.(일반 텍스트: st.write()')
    st.success('버튼이 클릭되었습니다.(메시지: st.success())')  # 성공 메시지 출력
    st.balloons() # 풍선 애니메이션 출력
