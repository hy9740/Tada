import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Streamlit 앱 설정
st.title('이차함수 표준형 그래프 시뮬레이터 📈')
st.markdown('표준형: $y = a(x-h)^2 + k$')
st.markdown('슬라이더를 움직여 $a$, $h$, $k$ 값 변화에 따른 그래프의 변화를 관찰해 보세요.')

# --- 사이드바: 사용자 입력 위젯 ---
st.sidebar.header('계수 (Coefficient) 입력')

# a 계수 (그래프의 모양/방향 결정)
# a는 0이 아니어야 하므로 min_value와 max_value 사이에서 0을 제외하도록 설정
a = st.sidebar.slider(
    'a 값 (볼록성 및 폭)',
    min_value=-2.0, max_value=2.0, value=1.0, step=0.1
)
# a가 0이면 이차함수가 아니므로, 사용자에게 경고 메시지를 표시합니다.
if a == 0:
    st.sidebar.warning('🚨 a는 0이 될 수 없습니다 (일차 함수가 됩니다)!', icon="⚠️")

# h 계수 (꼭짓점의 x좌표, x축 평행이동)
h = st.sidebar.slider(
    'h 값 (꼭짓점 x좌표/x축 평행이동)',
    min_value=-5.0, max_value=5.0, value=0.0, step=0.1
)

# k 계수 (꼭짓점의 y좌표, y축 평행이동)
k = st.sidebar.slider(
    'k 값 (꼭짓점 y좌표/y축 평행이동)',
    min_value=-5.0, max_value=5.0, value=0.0, step=0.1
)

# --- 메인 영역: 함수 정보 표시 ---
# 선택된 계수를 사용한 함수식 표시
st.subheader('선택된 함수식')
st.latex(f'y = {a}(x - {h})^{{2}} + {k}')

# 꼭짓점 좌표 표시
st.subheader('그래프의 특징')
st.write(f'**꼭짓점 좌표:** $({h}, {k})$')

# 축의 방정식 표시
st.write(f'**축의 방정식:** $x = {h}$')

# --- 메인 영역: 그래프 생성 및 표시 ---
# x축 범위 설정
x_range = np.linspace(-10, 10, 400) # -10부터 10까지 400개의 점 생성

# 이차함수 표준형 계산: y = a(x-h)^2 + k
y_values = a * (x_range - h)**2 + k

# 그래프 생성을 위해 Pandas DataFrame 생성
df = pd.DataFrame({
    'x': x_range,
    'y': y_values
})

# Plotly를 사용하여 대화형 라인 그래프 생성
fig = px.line(
    df,
    x='x',
    y='y',
    title=f'이차함수 그래프: y = {a}(x - {h})^2 + {k}',
)

# 그래프 레이아웃 설정 (축 범위 고정으로 변화를 더 잘 관찰할 수 있게 함)
fig.update_layout(
    xaxis_title='x',
    yaxis_title='y',
    xaxis_range=[-10, 10], # x축 범위 고정
    yaxis_range=[-10, 10], # y축 범위 고정
    height=500 # 그래프 높이 설정
)

# 꼭짓점 (h, k)를 강조하기 위해 점 추가
fig.add_scatter(
    x=[h],
    y=[k],
    mode='markers',
    name='꼭짓점',
    marker=dict(size=10, color='red')
)

# 축의 방정식 (x=h)을 점선으로 추가
fig.add_vline(
    x=h,
    line_dash="dot",
    line_color="gray",
    name='축의 방정식'
)

# Streamlit에 그래프 표시
st.plotly_chart(fig, use_container_width=True)
