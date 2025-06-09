import streamlit as st

st.set_page_config(page_title="MBTI 과학 여행 추천기 🌍", page_icon="🧳", layout="centered")

st.title("🌌 MBTI 맞춤 과학 감성 여행지 추천기 🧳")
st.markdown("당신의 성격에 맞는 **과학·수학 테마 여행지**를 추천해드릴게요! 🧠🌍\nMBTI를 선택해 주세요! 👇")

# MBTI 드롭다운 메뉴
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox("🔬 MBTI를 선택하세요", options=mbti_types)

# MBTI별 여행지 추천 데이터
mbti_destinations = {
    "INTJ": ("CERN, 스위스 🇨🇭", "세계 최대 입자가속기! 과학과 전략을 사랑하는 INTJ에게 완벽한 목적지 💥"),
    "INTP": ("MIT 박물관, 미국 🇺🇸", "호기심 천국! 기계, AI, 수학을 좋아하는 당신을 위한 지식의 성지 🤖"),
    "ENTJ": ("실리콘밸리, 미국 🇺🇸", "혁신과 기술, 리더십이 살아 숨 쉬는 장소 💼✨"),
    "ENTP": ("도쿄 미래과학관, 일본 🇯🇵", "상상력과 호기심이 폭발하는 과학 놀이동산 🎢🔭"),
    "INFJ": ("노르웨이 오로라 존 🇳🇴", "우주의 조용한 아름다움에 감성 충만… 별빛 아래의 명상 여행 🌌"),
    "INFP": ("아이슬란드 지열지대 🇮🇸", "감성과 자연과학이 만나는 힐링의 땅 🌋🧡"),
    "ENFJ": ("케이프타운 천문대, 남아공 🇿🇦", "우주와 인간, 그리고 연결의 이야기 ✨"),
    "ENFP": ("NASA 우주센터, 미국 🇺🇸", "열정 넘치는 우주 체험! 타오르는 호기심에 불을 붙여요 🚀"),
    "ISTJ": ("영국 그리니치 천문대 🇬🇧", "정확함과 전통을 중시하는 당신에게, 시간과 우주의 고향 ⏰🌠"),
    "ISFJ": ("덴마크 자연사 박물관 🇩🇰", "조용하고 따뜻한 지식 여행지. 생명과 자연을 사랑하는 당신에게 🍃"),
    "ESTJ": ("스미소니언 항공우주 박물관, 미국 🇺🇸", "논리적이고 체계적인 당신의 뇌를 자극하는 과학의 성지 🛩️"),
    "ESFJ": ("시드니 아쿠아리움, 호주 🇦🇺", "다정한 마음으로 과학과 생명을 만나는 힐링 여행지 🐠💙"),
    "ISTP": ("하와이 화산 국립공원 🇺🇸", "탐험과 분석, 그리고 현장의 과학! 🌋🧪"),
    "ISFP": ("갈릴레오 박물관, 이탈리아 🇮🇹", "예술과 과학이 조화를 이루는 당신만의 감성 여행지 🎨🔭"),
    "ESTP": ("두바이 미래 박물관 🇦🇪", "속도감 있고 첨단 기술이 넘치는 화려한 체험의 세계 🚀🌆"),
    "ESFP": ("유니버설 스튜디오 과학 어트랙션 🎢", "과학도 재밌게! 놀이와 지식의 환상 콜라보 🌈✨")
}

# 선택 후 추천 결과 출력
if selected_mbti:
    place, description = mbti_destinations[selected_mbti]
    st.success(f"🗺️ 추천 여행지: **{place}**")
    st.markdown(f"💡 이유: {description}")
    st.balloons()

st.markdown("---")
st.markdown("✈️ *추천 여행지는 MBTI 특성과 과학 감성을 반영해 엄선했어요!* 🌠")
