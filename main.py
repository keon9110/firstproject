import streamlit as st
import random

# 게임 리스트
games = [
    ("몸으로 말해요 🎭", "제시어를 몸짓으로만 설명하는 게임! 말은 금지! 🤫"),
    ("빙고 게임 🎯", "팀별로 숫자를 맞추며 즐기는 운빨 게임! 🧩"),
    ("제기차기 토너먼트 🥎", "전통놀이로 승부한다! 누가 제일 오래 찰까? 🇰🇷"),
    ("수건 돌리기 게임 🌀", "옛날 교실 감성 충만! 수건 돌리고 도망가자! 🏃‍♂️💨"),
    ("돌림판 퀴즈쇼 🎡", "돌림판에 맞는 퀴즈를 맞혀라! 뿅~🧠"),
    ("눈치 게임 👀", "다 같이 숫자 외치기! 겹치면 탈락~ 🔢"),
    ("손병호 게임 ✋", "기억력과 순발력의 대결! 손가락 접어~ 🎲"),
    ("무궁화 꽃이 피었습니다 🌸", "움직이면 탈락! 조심조심~ 🚦"),
    ("이구동성 📣", "같은 단어를 동시에 외쳐서 맞추기! 마음을 모아봐~ 💞"),
    ("과자 따먹기 🍭", "줄에 매달린 과자를 입으로 따먹기! 손 쓰면 반칙~ 🙊"),
    ("OX 퀴즈 🅾️❌", "지식과 감으로 풀어가는 OX 퀴즈! 📘"),
    ("풍선 터뜨리기 🎈", "의자에 앉아 풍선을 터뜨려라! 빠르게! 💥"),
    ("협동 줄넘기 🪢", "여럿이서 함께 줄넘기! 마음을 맞춰봐요 🤝"),
    ("종이컵 탑 쌓기 🏗️", "제한 시간 내에 가장 높이 쌓아라! ⏱️"),
    ("생일자 찾기 게임 🎂", "단서를 통해 생일자를 찾아라! 탐정 놀이 시작~ 🕵️"),
]

# 페이지 기본 설정
st.set_page_config(page_title="수련회 랜덤 게임 선택기 🎲", page_icon="🎈", layout="centered")

# 타이틀
st.markdown("<h1 style='text-align: center;'>🎉 수련회 랜덤 게임 선택기 🎉</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>👇 귀여운 버튼을 눌러서 오늘의 예능 게임을 뽑아보세요! 👇</p>", unsafe_allow_html=True)

# 버튼 (아이콘 포함)
if st.button("🎁 게임 뽑기!"):
    game = random.choice(games)
    st.balloons()  # 풍선 효과 🎈🎈🎈
    st.success(f"🥳 오늘의 게임은... **{game[0]}**!")
    st.info(f"📌 {game[1]}")
else:
    st.image("https://cdn-icons-png.flaticon.com/512/3468/3468372.png", width=150)  # 발랄한 클릭 유도 아이콘

# 하단 꾸미기
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>Made with ❤️ for 즐거운 수련회</p>", unsafe_allow_html=True)
