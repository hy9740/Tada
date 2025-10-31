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
    st.latex(r'\frac{A}{B} = \frac{A \times C}{B \times C} \quad (C \neq 0)')
    st.markdown('*분모를 최소공배수로 맞추기 위해 곱합니다.*')
    
    st.info('**예제:** $\\frac{1}{x-1}$ 와 $\\frac{1}{x+1}$ 를 통분하면?')
    st.latex(r'\frac{1}{x-1} \to \frac{x+1}{(x-1)(x+1)}, \quad \frac{1}{x+1} \to \frac{x-1}{(x-1)(x+1)}')

# ----------------------------------------------------
st.markdown('---')
st.header('3. 사칙연산 (덧셈, 뺄셈, 곱셈, 나눗셈)')

st.markdown('유리식의 사칙연산은 일반적인 분수의 사칙연산과 동일한 방법으로 계산합니다.')

# 덧셈/뺄셈
st.subheader('3.1. 덧셈과 뺄셈')
st.markdown('분모를 **통분**한 후, 분자끼리 더하거나 뺍니다.')
st.latex(r'\frac{A}{C} \pm \frac{B}{C} = \frac{A \pm B}{C}')

# 곱셈/나눗셈
st.subheader('3.2. 곱셈과 나눗셈')
st.markdown('곱셈은 분자는 분자끼리, 분모는 분모끼리 곱합니다. 나눗셈은 나누는 식을 역수로 바꾸어 곱합니다.')
st.latex(r'\frac{A}{B} \times \frac{C}{D} = \frac{A \times C}{B \times D}')
st.latex(r'\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \times \frac{D}{C} = \frac{A \times D}{B \times C}')

# ----------------------------------------------------
st.markdown('---')
st.header('4. 유리식의 계산에서 중요한 조건')

st.markdown("""
유리식을 계산할 때는 분모가 0이 되지 않도록 항상 주의해야 합니다.
**분모가 0이 되는 $x$ 값**에서는 함수가 정의되지 않습니다.
""")

st.warning(r'❗ **주의**: 유리식 $\frac{A}{B}$ 가 정의되기 위한 조건은 **$B \neq 0$** 입니다.')

st.info('**학습 팁**')
st.markdown("""
1.  **약분/통분 전:** 분자와 분모를 **인수분해**하는 연습을 하세요.
2.  **나눗셈:** 역수를 취하는 과정에서 실수가 없도록 주의하세요.
3.  **부분분수 변형:** 복잡한 유리식의 합을 계산할 때 유용하며, 나중에 학습합니다.
""")
