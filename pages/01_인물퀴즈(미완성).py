import streamlit as st
import random

# 아이돌 이름 리스트 (50명 예시)
idols = [
    "정국", "뷔", "지민", "RM", "진", "슈가", "제이홉", "지드래곤", "태양", "대성",
    "민현", "백현", "찬열", "디오", "카이", "세훈", "태연", "아이유", "슬기", "조이",
    "웬디", "아이린", "예리", "수호", "시우민", "보나", "은서", "사나", "나연", "쯔위",
    "모모", "정연", "채영", "다현", "유나", "리아", "예지", "채령", "윤아", "서현",
    "수지", "하니", "솔라", "화사", "문별", "휘인", "연우", "주이", "지수", "제니"
]

# 예시 이미지 딕셔너리 (실제 이미지 경로/URL로 대체 필요)
idol_images = {name: f"https://example.com/images/{name}.jpg" for name in idols}

# 발랄한 아이콘들
cute_icons = ["🎀", "🎧", "🌟", "💖", "🧸", "🍭", "🌈", "🎉", "✨", "💫"]

# 세션 상태 초기화
if "quiz_pool" not in st.session_state:
    st.session_state.quiz_pool = random.sample(idols, 10)
    st.session_state.score = 0
    st.session_state.question_num = 0
    st.session_state.finished = False
    st.session_state.answered = False
    st.session_state.correct = False

def next_question():
    st.session_state.answered = False
    st.session_state.correct = False
    if st.session_state.question_num < len(st.session_state.quiz_pool) - 1:
        st.session_state.question_num += 1
    else:
        st.session_state.finished = True

def reset_quiz():
    st.session_state.quiz_pool = random.sample(idols, 10)
    st.session_state.score = 0
    st.session_state.question_num = 0
    st.session_state.finished = False
    st.session_state.answered = False
    st.session_state.correct = False

# 🎵 타이틀
st.title("🌟 아이돌 인물 퀴즈 🌟")
st.write("사진을 보고 어떤 아이돌인지 맞혀보세요!")

# 퀴즈 종료 화면
if st.session_state.finished:
    st.success(f"🎉 퀴즈 완료! 총 점수: {st.session_state.score} / 10")
    if st.button("🔄 다시 시작하기"):
        reset_quiz()
else:
    answer = st.session_state.quiz_pool[st.session_state.question_num]
    choices = random.sample([i for i in idols if i != answer], 3)
    choices.append(answer)
    random.shuffle(choices)

    # 이미지 출력 (예시 이미지 사용 중)
    st.image(idol_images[answer], width=300, caption="이 아이돌은 누구일까요?")

    # 선택지에 발랄한 아이콘 랜덤 붙이기
    display_choices = [f"{random.choice(cute_icons)} {name}" for name in choices]
    icon_name_map = dict(zip(display_choices, choices))
    
    selected = st.radio("정답을 골라주세요!", display_choices, index=0)

    if st.button("제출") and not st.session_state.answered:
        chosen_name = icon_name_map[selected]
        st.session_state.answered = True
        if chosen_name == answer:
            st.success("정답입니다! 🎉")
            st.balloons()  # 폭죽 효과
            st.session_state.score += 1
            st.session_state.correct = True
        else:
            st.error(f"틀렸어요! 💣 정답은 {answer}입니다.")
            st.session_state.correct = False

    # 정답 확인 후 '다음' 버튼
    if st.session_state.answered:
        st.button("👉 다음 문제", on_click=next_question)
