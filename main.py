import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="영화 데이터 그래프 도감 1 - 시간",
page_icon="🎬",
layout="wide"
)

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"

# 데이터 불러오기

df = pd.read_csv(DATA_URL)

# 날짜를 진짜 날짜로 변환

df["날짜"] = pd.to_datetime(
df["날짜"].astype(str),
format="%Y%m%d"
)

# 숫자 데이터로 변환

df["순위"] = pd.to_numeric(df["순위"], errors="coerce")
df["일관객"] = pd.to_numeric(df["일관객"], errors="coerce")
df["누적관객"] = pd.to_numeric(df["누적관객"], errors="coerce")
df["스크린수"] = pd.to_numeric(df["스크린수"], errors="coerce")
df["상영횟수"] = pd.to_numeric(df["상영횟수"], errors="coerce")

# ==================================================

# 제목

# ==================================================

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")

st.write(
"1년 동안의 일별 박스오피스 데이터를 시간의 흐름에 따라 살펴봅니다."
)

# ==================================================

# 데이터 살펴보기

# ==================================================

st.divider()

st.header("📋 데이터 살펴보기")

st.write(f"전체 데이터 수: **{len(df):,}개**")

with st.expander("데이터 미리 보기"):
st.dataframe(df.head(20), use_container_width=True)

# ==================================================

# 그래프 1

# ==================================================

st.divider()

st.header("📈 그래프 1. 시간에 따른 영화별 일관객 변화")

st.write(
"드롭다운에서 영화를 선택하면 날짜별 일관객 변화를 확인할 수 있습니다."
)

movie_list = sorted(
df["영화명"].dropna().unique()
)

selected_movie = st.selectbox(
"🎥 영화를 선택하세요",
movie_list
)

movie_df = df[
df["영화명"] == selected_movie
].copy()

movie_df = movie_df.sort_values("날짜")

fig = px.line(
movie_df,
x="날짜",
y="일관객",
markers=True,
title=f"{selected_movie}의 날짜별 일관객 변화",
labels={
"날짜": "날짜",
"일관객": "일관객 수"
}
)

fig.update_traces(
hovertemplate=
"<b>날짜</b>: %{x|%Y-%m-%d}<br>"
"<b>관객수</b>: %{y:,}명"
"<extra></extra>"
)

fig.update_layout(
xaxis_title="날짜",
yaxis_title="일관객 수(명)"
)

st.plotly_chart(
fig,
use_container_width=True
)

st.info(
"💡 이 그래프로 알 수 있는 것: "
"선택한 영화의 일별 관객 수가 시간에 따라 어떻게 변했는지 알 수 있습니다."
)

# ==================================================

# 그래프 2

# ==================================================

st.divider()

st.header("📊 그래프 2. 다음 그래프")

st.write("이곳에 앞으로 새로운 그래프를 추가합니다.")

st.info(
"💡 이 그래프로 알 수 있는 것: "
"그래프를 추가한 뒤 이곳에 그래프에서 알 수 있는 내용을 작성합니다."
)

# ==================================================

# 그래프 3

# ==================================================

st.divider()

st.header("📊 그래프 3. 다음 그래프")

st.write("이곳에 앞으로 새로운 그래프를 추가합니다.")

st.info(
"💡 이 그래프로 알 수 있는 것: "
"그래프를 추가한 뒤 이곳에 그래프에서 알 수 있는 내용을 작성합니다."
)
