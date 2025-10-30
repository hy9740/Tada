import streamlit as st
import random

def generate_lotto_numbers(num_sets):
    """
    지정된 횟수만큼 로또 번호 (1부터 45 중 중복 없이 6개)를 생성합니다.
    """
    lotto_results = []
    for _ in range(num_sets):
        # 1부터 45까지의 숫자 리스트에서 중복 없이 6개의 숫자를 무작위로 선택
        numbers = sorted(random.sample(range(1, 46), 6))
        lotto_results.append(numbers)
    return lotto_results

# Streamlit 앱의 제목 설정
st.title('로또 번호 생성기 🎰')
st.markdown('1부터 45 사이의 숫자 중 6개의 숫자를 무작위로 생성합니다.')

# 사용자로부터 몇 세트의 로또 번호를 생성할지 입력받음
num_sets = st.slider(
    '몇 세트의 로또 번호를 생성하시겠습니까?',
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

# 번호 생성 버튼
if st.button('번호 생성'):
    # 로또 번호 생성
    numbers = generate_lotto_numbers(num_sets)

    st.subheader(f'{num_sets} 세트의 로또 번호:')

    # 생성된 번호 출력
    for i, lotto_set in enumerate(numbers, 1):
        # 번호를 쉼표로 구분된 문자열로 변환
        numbers_str = ", ".join(map(str, lotto_set))
        st.success(f'**{i}번째 세트:** {numbers_str}')

    # 시각적인 재미를 위한 풍선 효과
    st.balloons()
