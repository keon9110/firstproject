import streamlit as st
import random

# 아이돌 이름 리스트 (예시 50명, 자유롭게 수정 가능)
idols = [
    "정국", "뷔", "지민", "RM", "진", "슈가", "제이홉", "지드래곤", "태양", "대성",
    "민현", "백현", "찬열", "디오", "카이", "세훈", "태연", "아이유", "슬기", "조이",
    "웬디", "아이린", "예리", "수호", "시우민", "보나", "은서", "사나", "나연", "쯔위",
    "모모", "정연", "채영", "다현", "유나", "리아", "예지", "채령", "윤아", "서현",
    "수지", "하니", "솔라", "화사", "문별", "휘인", "연우", "주이", "지수", "제니"
]

# 이미지 경로 매핑 (예시용, 실제 URL 또는 로컬 경로로 대체하세요)
idol_images = {name: f"https://example.com/images/{name}.jpg" for name in idols}

# 세션 상태 초기화
if "quiz_pool" not in st.session_state:
    st.session_state.quiz_pool = random.sample(idols, 10)
    st.session_state.score = 0
    st.session_state.question_num = 0
    st.session_state.finished = False

def next_question():
    if st.session_state.question_num < len(st.session_state.quiz_pool) - 1:
        st.session_state.question_num += 1
    else:
        st.session_state.finished = True

def reset_quiz():
    st.session_state.quiz_pool = random.sample(idols, 10)
    st.session_state.score = 0
    st.session_state.question_num = 0
    st.session_state.finished = False

st.title("🎤 아이돌 얼굴 퀴즈")
st.write("다음 사진의 아이돌 이름은 무엇일까요?")

if st.session_state.finished:
    st.success(f"퀴즈 완료! 총 점수: {st.session_state.score} / 10")
    if st.button("다시 시작하기"):
        reset_quiz()
else:
    answer = st.session_state.quiz_pool[st.session_state.question_num]
    # 보기 4개 중 정답 포함되게 랜덤 생성
    choices = random.sample([i for i in idols if i != answer], 3)
    choices.append(answer)
    random.shuffle(choices)

    # 이미지 표시
    st.image(idol_images[answer], width=300, caption="누굴까요? (랜덤 이미지 필요)")

    # 선택지
    selected = st.radio("정답을 선택하세요", choices)

    if st.button("제출"):
        if selected == answer:
            st.success("정답입니다!")
            st.session_state.score += 1
        else:
            st.error(f"틀렸어요! 정답은 {answer}입니다.")
        st.button("다음 문제", on_click=next_question)
