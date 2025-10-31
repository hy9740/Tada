import streamlit as st

# 페이지 설정
st.set_page_config(layout="wide")

# 앱 제목
st.title('📐 유리식 (Rational Expression) 개념 정리 앱')

# ----------------------------------------------------
st.header('1. 유리식의 정의')

st.markdown("""
**유리식**은 두 **다항식** $A$ 와 $B$ ($B \neq 0$)에 대하여, $\\frac{A}{B}$ 와 같이 **분수 꼴**로 나타낸 식을 말합니다.
이때, 유리식은 크게 **다항식**과 **분수식**으로 나눌 수 있습니다.
""")

st.latex(r'\text{유리식} = \frac{A}{B} \quad (A, B \text{는 다항식}, B \neq 0)')

# 다항식과 분수식 구분
st.subheader('1.1. 다항식 (Polynomial)')
st.markdown("""
분모 $B$ 가 **상수(0이 아닌 수)**일 때의 유리식, 즉 분모에 문자가 없는 식입니다.
*예시: $x^2 + 2x - 1$, $5y + 3$*
""")

st.subheader('1.2. 분수식 (Fractional Expression)')
st.markdown("""
분모 $B$ 에 **문자**가 포함되어 있는 식입니다.
*예시: $\\frac{1}{x}$, $\\frac{x^2 - 1}{x + 3}$*
""")

# ----------------------------------------------------
st.markdown('---')
st.header('2. 유리식의 기본 성질 및 약분')

st.markdown("""
유리식의 분자와 분모에 0이 아닌 같은 식 $C$ 를 곱하거나 나누어도 그 값은 같습니다.
이 성질을 이용하여 유리식을 **통분**하거나 **약분**할 수 있습니다.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader('2.1. 약분')
    st.latex(r'\frac{A}{B} = \frac{A \div C}{B \div C} \quad (C \neq 0)')
    st.markdown('*분자와 분모를 공통인수로 나눕니다.*')
    
    st.info('**예제:** $\\frac{x^2 - 1}{x - 1}$ 을 약분하면?')
    st.latex(r'\frac{x^2 - 1}{x - 1} = \frac{(x-1)(x+1)}{x-1} = x + 1')

with col2:
    st.subheader('2.2. 통분')
    st.latex(r'\frac{A}{B} = \
