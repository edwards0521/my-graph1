import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="영화 데이터 그래프 도감 1 - 시간",
page_icon="🎬",
layout="wide"
)

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"

df = pd.read_csv(DATA_URL)

df["날짜"] = pd.to_datetime(
df["날짜"].astype(str),
format="%Y%m%d"
)

df["순위"] = pd.to_numeric(df["순위"], errors="coerce")
df["일관객"] = pd.to_numeric(df["일관객"], errors="coerce")
df["누적관객"] = pd.to_numeric(df["누적관객"], errors="coerce")
df["스크린수"] = pd.to_numeric(df["스크린수"], errors="coerce")
df["상영횟수"] = pd.to_numeric(df["상영횟수"], errors="coerce")

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")

st.write("1년 동안의 일별 박스오피스 데이터를 시간의 흐름에 따라 살펴봅니다.")

st.divider()

st.header("📋 데이터 살펴보기")

st.write(f"전체 데이터 수: {len(df):,}개")

st.dataframe(
df.head(20),
use_container_width=True
)

st.divider()

st.header("📈 그래프 1. 시간에 따른 영화별 일관객 변화")

st.write("드롭다운에서 영화를 선택하면 날짜별 일관객 변화를 확인할 수 있습니다.")

movie_list = sorted(df["영화명"].dropna().unique())

selected_movie = st.selectbox(
"🎥 영화를 선택하세요",
movie_list
)

movie_df = df[df["영화명"] == selected_movie].copy()

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
hovertemplate="<b>날짜</b>: %{x|%Y-%m-%d}<br><b>관객수</b>: %{y:,}명<extra></extra>"
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
"💡 이 그래프로 알 수 있는 것: 선택한 영화의 일별 관객 수가 시간에 따라 어떻게 변했는지 알 수 있습니다."
)

st.divider()

st.header("📊 그래프 2. 다음 그래프")

st.write("이곳에 앞으로 새로운 시간 관련 그래프를 추가합니다.")

st.info(
"💡 이 그래프로 알 수 있는 것: 앞으로 추가할 그래프에서 발견할 수 있는 내용을 한 문장으로 작성합니다."
)

st.divider()

st.header("📊 그래프 3. 다음 그래프")

st.write("이곳에 앞으로 새로운 시간 관련 그래프를 추가합니다.")

st.info(
"💡 이 그래프로 알 수 있는 것: 앞으로 추가할 그래프에서 발견할 수 있는 내용을 한 문장으로 작성합니다."
)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="영화 데이터 그래프 도감 1 - 시간",
page_icon="🎬",
layout="wide"
)

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"

df = pd.read_csv(DATA_URL)

df["날짜"] = pd.to_datetime(
df["날짜"].astype(str),
format="%Y%m%d"
)

df["순위"] = pd.to_numeric(df["순위"], errors="coerce")
df["일관객"] = pd.to_numeric(df["일관객"], errors="coerce")
df["누적관객"] = pd.to_numeric(df["누적관객"], errors="coerce")
df["스크린수"] = pd.to_numeric(df["스크린수"], errors="coerce")
df["상영횟수"] = pd.to_numeric(df["상영횟수"], errors="coerce")

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")

st.write("1년 동안의 일별 박스오피스 데이터를 시간의 흐름에 따라 살펴봅니다.")

st.divider()

st.header("📋 데이터 살펴보기")

st.write(f"전체 데이터 수: {len(df):,}개")

st.dataframe(
df.head(20),
use_container_width=True
)

# ==================================================

# 그래프 1

# ==================================================

st.divider()

st.header("📈 그래프 1. 시간에 따른 영화별 일관객 변화")

st.write("드롭다운에서 영화를 선택하면 날짜별 일관객 변화를 확인할 수 있습니다.")

movie_list = sorted(df["영화명"].dropna().unique())

selected_movie = st.selectbox(
"🎥 영화를 선택하세요",
movie_list
)

movie_df = df[df["영화명"] == selected_movie].copy()

movie_df = movie_df.sort_values("날짜")

fig1 = px.line(
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

fig1.update_traces(
hovertemplate="<b>날짜</b>: %{x|%Y-%m-%d}<br><b>관객수</b>: %{y:,}명<extra></extra>"
)

fig1.update_layout(
xaxis_title="날짜",
yaxis_title="일관객 수(명)"
)

st.plotly_chart(
fig1,
use_container_width=True
)

st.info(
"💡 이 그래프로 알 수 있는 것: 선택한 영화의 일별 관객 수가 시간에 따라 어떻게 변했는지 알 수 있습니다."
)

# ==================================================

# 그래프 2

# ==================================================

st.divider()

st.header("📊 그래프 2. 일관객 합계 상위 5편의 날짜별 변화")

st.write(
"이 기간 동안 일관객 합계가 가장 많은 영화 5편을 골라 날짜별 관객 수를 비교합니다."
)

# 영화별 일관객 합계 계산

top5_movies = (
df.groupby("영화명")["일관객"]
.sum()
.sort_values(ascending=False)
.head(5)
.index
.tolist()
)

# 상위 5편 데이터만 선택

top5_df = df[
df["영화명"].isin(top5_movies)
].copy()

# 날짜 순서대로 정렬

top5_df = top5_df.sort_values("날짜")

# 5편의 영화를 한 그래프에 표시

fig2 = px.line(
top5_df,
x="날짜",
y="일관객",
color="영화명",
markers=True,
title="일관객 합계 상위 5편의 날짜별 일관객 변화",
labels={
"날짜": "날짜",
"일관객": "일관객 수",
"영화명": "영화"
}
)

fig2.update_layout(
xaxis_title="날짜",
yaxis_title="일관객 수(명)",
legend_title="영화명",
hovermode="x unified"
)

fig2.update_traces(
hovertemplate="<b>%{fullData.name}</b><br>날짜: %{x|%Y-%m-%d}<br>관객수: %{y:,}명<extra></extra>"
)

st.plotly_chart(
fig2,
use_container_width=True
)

st.info(
"💡 이 그래프로 알 수 있는 것: 이 기간 동안 가장 많은 관객을 모은 5편의 영화가 각각 언제 관객 수가 높아졌고, 얼마나 오래 흥행했는지 비교할 수 있습니다."
)

# ==================================================

# 그래프 3

# ==================================================

st.divider()

st.header("📊 그래프 3. 다음 그래프")

st.write("이곳에 앞으로 새로운 시간 관련 그래프를 추가합니다.")

st.info(
"💡 이 그래프로 알 수 있는 것: 앞으로 추가할 그래프에서 발견할 수 있는 내용을 한 문장으로 작성합니다."
)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
page_title="영화 데이터 그래프 도감 1 - 시간",
page_icon="🎬",
layout="wide"
)

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"

df = pd.read_csv(DATA_URL)

df["날짜"] = pd.to_datetime(
df["날짜"].astype(str),
format="%Y%m%d"
)

df["순위"] = pd.to_numeric(df["순위"], errors="coerce")
df["일관객"] = pd.to_numeric(df["일관객"], errors="coerce")
df["누적관객"] = pd.to_numeric(df["누적관객"], errors="coerce")
df["스크린수"] = pd.to_numeric(df["스크린수"], errors="coerce")
df["상영횟수"] = pd.to_numeric(df["상영횟수"], errors="coerce")

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")

st.write("1년 동안의 일별 박스오피스 데이터를 시간의 흐름에 따라 살펴봅니다.")

st.divider()

st.header("📋 데이터 살펴보기")

st.write(f"전체 데이터 수: {len(df):,}개")

st.dataframe(
df.head(20),
use_container_width=True
)

# ==================================================

# 그래프 1

# ==================================================

st.divider()

st.header("📈 그래프 1. 시간에 따른 영화별 일관객 변화")

st.write("드롭다운에서 영화를 선택하면 날짜별 일관객 변화를 확인할 수 있습니다.")

movie_list = sorted(df["영화명"].dropna().unique())

selected_movie = st.selectbox(
"🎥 영화를 선택하세요",
movie_list
)

movie_df = df[df["영화명"] == selected_movie].copy()

movie_df = movie_df.sort_values("날짜")

fig1 = px.line(
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

fig1.update_traces(
hovertemplate="<b>날짜</b>: %{x|%Y-%m-%d}<br><b>관객수</b>: %{y:,}명<extra></extra>"
)

fig1.update_layout(
xaxis_title="날짜",
yaxis_title="일관객 수(명)"
)

st.plotly_chart(
fig1,
use_container_width=True
)

st.info(
"💡 이 그래프로 알 수 있는 것: 선택한 영화의 일별 관객 수가 시간에 따라 어떻게 변했는지 알 수 있습니다."
)

# ==================================================

# 그래프 2

# ==================================================

st.divider()

st.header("📊 그래프 2. 일관객 합계 상위 5편의 날짜별 변화")

st.write(
"이 기간 동안 일관객 합계가 가장 많은 영화 5편을 골라 날짜별 관객 수를 비교합니다."
)

top5_movies = (
df.groupby("영화명")["일관객"]
.sum()
.sort_values(ascending=False)
.head(5)
.index
.tolist()
)

top5_df = df[
df["영화명"].isin(top5_movies)
].copy()

top5_df = top5_df.sort_values("날짜")

fig2 = px.line(
top5_df,
x="날짜",
y="일관객",
color="영화명",
markers=True,
title="일관객 합계 상위 5편의 날짜별 일관객 변화",
labels={
"날짜": "날짜",
"일관객": "일관객 수",
"영화명": "영화"
}
)

fig2.update_layout(
xaxis_title="날짜",
yaxis_title="일관객 수(명)",
legend_title="영화명",
hovermode="x unified"
)

fig2.update_traces(
hovertemplate="<b>%{fullData.name}</b><br>날짜: %{x|%Y-%m-%d}<br>관객수: %{y:,}명<extra></extra>"
)

st.plotly_chart(
fig2,
use_container_width=True
)

st.info(
"💡 이 그래프로 알 수 있는 것: 이 기간 동안 가장 많은 관객을 모은 5편의 영화가 각각 언제 관객 수가 높아졌고, 얼마나 오래 흥행했는지 비교할 수 있습니다."
)

# ==================================================

# 그래프 3

# ==================================================

st.divider()

st.header("📊 그래프 3. 날짜별 박스오피스 TOP 10 전체 관객 수")

st.write(
"날짜별로 박스오피스 10위권 영화의 일관객 수를 모두 합쳐 전체 관객 수의 변화를 살펴봅니다."
)

# 날짜별 일관객 합계 계산

daily_total = (
df.groupby("날짜")["일관객"]
.sum()
.reset_index()
.sort_values("날짜")
)

# 일관객 합계가 가장 큰 날짜 3개

top3_days = (
daily_total.nlargest(3, "일관객")
.sort_values("날짜")
)

# 영역 그래프 만들기

fig3 = px.area(
daily_total,
x="날짜",
y="일관객",
title="날짜별 박스오피스 TOP 10 일관객 합계",
labels={
"날짜": "날짜",
"일관객": "TOP 10 일관객 합계"
}
)

# 그래프 위에 상위 3일 표시

fig3.add_scatter(
x=top3_days["날짜"],
y=top3_days["일관객"],
mode="markers+text",
text=top3_days["날짜"].dt.strftime("%Y-%m-%d"),
textposition="top center",
name="관객 합계 상위 3일",
hovertemplate=(
"<b>날짜</b>: %{x|%Y-%m-%d}<br>"
"<b>TOP 10 관객 합계</b>: %{y:,}명"
"<extra></extra>"
)
)

fig3.update_layout(
xaxis_title="날짜",
yaxis_title="TOP 10 일관객 합계(명)",
hovermode="x unified"
)

# 영역 부분 마우스 정보 설정

fig3.update_traces(
hovertemplate=(
"<b>날짜</b>: %{x|%Y-%m-%d}<br>"
"<b>TOP 10 관객 합계</b>: %{y:,}명"
"<extra></extra>"
),
selector=dict(type="scatter")
)

st.plotly_chart(
fig3,
use_container_width=True
)

st.info(
"💡 이 그래프로 알 수 있는 것: 1년 동안 박스오피스 TOP 10 영화 전체의 관객 수가 언제 가장 많았는지 확인하고, 특히 관객이 집중된 상위 3일을 찾아볼 수 있습니다."
)
# ==================================================

# 그래프 4

# ==================================================

st.divider()

st.header("🏆 그래프 4. 이 기간 관객 수 TOP 10 영화")

st.write(
"영화별로 이 기간 동안의 일관객을 모두 더해 관객 수가 가장 많은 영화 10편을 비교합니다."
)

# 영화별 일관객 합계와 10위권에 등장한 날 수 계산

movie_summary = (
df.groupby("영화명")
.agg(
일관객합계=("일관객", "sum"),
TOP10등장일수=("날짜", "nunique")
)
.reset_index()
)

# 일관객 합계가 많은 순서로 TOP 10 선정

top10_movies = (
movie_summary
.sort_values("일관객합계", ascending=False)
.head(10)
.sort_values("일관객합계", ascending=True)
)

# 가로 막대그래프 만들기

fig4 = px.bar(
top10_movies,
x="일관객합계",
y="영화명",
orientation="h",
title="이 기간 일관객 합계 TOP 10",
labels={
"일관객합계": "일관객 합계",
"영화명": "영화명"
},
hover_data={
"일관객합계": ":,",
"TOP10등장일수": True
}
)

# 마우스를 올렸을 때 표시할 내용

fig4.update_traces(
hovertemplate=(
"<b>%{y}</b><br>"
"일관객 합계: %{x:,}명<br>"
"10위권에 든 날: %{customdata[0]}일"
"<extra></extra>"
)
)

fig4.update_layout(
xaxis_title="이 기간 일관객 합계(명)",
yaxis_title="영화명",
showlegend=False
)

st.plotly_chart(
fig4,
use_container_width=True
)

st.info(
"💡 이 그래프로 알 수 있는 것: 이 기간 동안 가장 많은 관객을 모은 영화와, 각 영화가 박스오피스 TOP 10에 얼마나 오래 등장했는지를 함께 비교할 수 있습니다."
)



