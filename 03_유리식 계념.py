import streamlit as st

# 페이지 설정
st.set_page_config(layout="centered")

# 앱 제목
st.title('📘 유리식 (Rational Expression)의 정의')

# ----------------------------------------------------
## 1. 유리식의 개념
st.header('1. 유리식의 정의')

st.markdown("""
**유리식**이란 두 다항식 $A$ 와 $B$ ($B \neq 0$)에 대하여, $\\frac{A}{B}$ 와 같이 **분수 꼴**로 나타낸 식을 말합니다.
""")

# 유리식의 수학적 표현
st.latex(r'\text{유리식} = \frac{A}{B} \quad (\text{단, } A, B \text{는 다항식이고 } B \neq 0)')

st.markdown('---')

## 2. 유리식의 분류
st.header('2. 유리식의 분류: 다항식과 분수식')

st.markdown('유리식은 분모에 문자가 포함되어 있는지에 따라 **다항식**과 **분수식**으로 나뉩니다.')

col1, col2 = st.columns(2)

with col1:
    st.subheader('2.1. 다항식 (Polynomial)')
    st.markdown("""
    분모 $B$ 에 **문자가 포함되어 있지 않은** 유리식입니다.
    (분모가 0이 아닌 상수일 때)
    """)
    st.info('**예시:** $x^2 + 5x$, $\\frac{3}{2}y - 1$')

with col2:
    st.subheader('2.2. 분수식 (Fractional Expression)')
    st.markdown("""
    분모 $B$ 에 **문자가 포함되어 있는** 유리식입니다.
    """)
    st.info('**예시:** $\\frac{1}{x}$, $\\frac{x^2 + 1}{x - 4}$')

st.markdown('---')

## 3. 정의 조건
st.header('3. 유리식이 성립할 조건')

st.warning(r'💡 **핵심**: 모든 유리식 $\frac{A}{B}$ 는 **분모 $B$ 가 0이 아닐 때**만 정의됩니다.')
