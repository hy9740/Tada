import streamlit as st

# 페이지 설정
st.set_page_config(layout="wide")

# 앱 제목
st.title('📐 유리식 (Rational Expression) 개념 및 성질 학습 앱')

# ----------------------------------------------------
## 1. 유리식의 정의
st.header('1. 유리식의 정의')

st.markdown("""
**유리식**은 두 **다항식** $A$ 와 $B$ ($B \neq 0$)에 대하여, $\\frac{A}{B}$ 와 같이 **분수 꼴**로 나타낸 식을 말합니다.
""")

st.latex(r'\text{유리식} = \frac{A}{B} \quad (A, B \text{는 다항식}, B \neq 0)')

st.subheader('1.1. 다항식 (Polynomial)')
st.markdown("""
분모 $B$ 에 **문자**가 포함되어 있지 않은 유리식입니다.
*예시: $x^2 + 2x - 1$, $5y + 3$*
""")

st.subheader('1.2. 분수식 (Fractional Expression)')
st.markdown("""
분모 $B$ 에 **문자**가 포함되어 있는 유리식입니다.
*예시: $\\frac{1}{x}$, $\\frac{x^2 - 1}{x + 3}$*
""")

st.markdown('---')

# ----------------------------------------------------
## 2. 유리식의 기본 성질 (약분/통분)
st.header('2. 유리식의 기본 성질 (약분 및 통분)')

st.markdown("""
유리식의 분자와 분모에 0이 아닌 같은 식 $C$ 를 곱하거나 나누어도 그 값은 같습니다.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader('2.1. 약분 (Simplification)')
    st.markdown('분자와 분모를 **공통인수**로 나누어 간단히 만듭니다.')
    st.latex(r'\frac{A}{B} = \frac{A \div C}{B \div C} \quad (C \neq 0)')
    
    st.info('**예제:**')
    st.latex(r'\frac{x^2 - 4}{x + 2} = \frac{(x-2)(x+2)}{x+2} = x - 2')

with col2:
    st.subheader('2.2. 통분 (Finding a Common Denominator)')
    st.markdown('덧셈이나 뺄셈을 위해 분모를 **최소공배수**로 같게 만듭니다.')
    st.latex(r'\frac{A}{B} = \frac{A \times C}{B \times C} \quad (C \neq 0)')
    
    st.info('**예제:**')
    st.latex(r'\frac{1}{x} \text{와} \frac{1}{x^2} \text{의 공통분모:} \quad x^2')
    st.latex(r'\frac{1}{x} \to \frac{x}{x^2}')

st.markdown('---')

# ----------------------------------------------------
## 3. 유리식이 정의될 조건
st.header('3. 유리식이 정의될 조건')

st.markdown("""
수학에서 **분모는 절대 0이 될 수 없다**는 조건은 유리식에서도 가장 중요하게 적용됩니다.
""")

st.warning(r'❗ **핵심 조건**: 유리식 $\frac{A}{B}$ 가 정의되기 위해서는 **분모 $B$ 가 0이 아니어야 합니다 ($\mathbf{B \neq 0}$)**.')

st.info('**예제:** 유리식 $\\frac{x+1}{x-3}$ 이 정의되기 위한 조건')
st.markdown(r'분모 $x-3$ 이 0이 아니어야 하므로, $x-3 \neq 0$, 즉 **$x \neq 3$** 입니다.')
