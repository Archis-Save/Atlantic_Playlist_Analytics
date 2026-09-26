import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Atlantic Playlist Analytics", page_icon="🎵", layout="wide")
st.title("🎵 Atlantic United States — Historical Playlist Analytics")
st.caption("Descriptive historical analysis of daily Top 50 playlist snapshots. No prediction or recommendation.")

@st.cache_data
def load_data(uploaded=None):
    if uploaded is not None:
        d=pd.read_csv(uploaded)
    else:
        d=pd.read_csv("Atlantic_United_States_cleaned.csv")
    d["date"]=pd.to_datetime(d["date"],dayfirst=True,errors="coerce")
    d["duration_min"]=d["duration_ms"]/60000
    return d

uploaded=st.sidebar.file_uploader("Upload CSV (optional)", type=["csv"])
df=load_data(uploaded)

# Filters
st.sidebar.header("Filters")
min_d,max_d=df["date"].min().date(),df["date"].max().date()
dates=st.sidebar.date_input("Date range",[min_d,max_d],min_value=min_d,max_value=max_d)
if isinstance(dates,(list,tuple)) and len(dates)==2:
    d1,d2=dates
else:
    d1,d2=min_d,max_d
artists=["All"]+sorted(df["artist"].dropna().unique().tolist())
artist_sel=st.sidebar.selectbox("Artist",artists)
songs=["All"]+sorted(df["song"].dropna().unique().tolist())
song_sel=st.sidebar.selectbox("Song",songs)
rank_range=st.sidebar.slider("Rank range",1,50,(1,50))
album_sel=st.sidebar.multiselect("Album type",sorted(df["album_type"].dropna().unique()),default=sorted(df["album_type"].dropna().unique()))
explicit_sel=st.sidebar.multiselect("Explicit",["Explicit","Non-explicit"],default=["Explicit","Non-explicit"])

x=df[(df.date.dt.date>=d1)&(df.date.dt.date<=d2)&df.position.between(*rank_range)&df.album_type.isin(album_sel)].copy()
if artist_sel!="All": x=x[x.artist==artist_sel]
if song_sel!="All": x=x[x.song==song_sel]
if len(explicit_sel)==1:
    x=x[x.is_explicit==(explicit_sel[0]=="Explicit")]

c1,c2,c3,c4=st.columns(4)
c1.metric("Chart rows",f"{len(x):,}")
c2.metric("Unique songs",f"{x.song.nunique():,}")
c3.metric("Unique artists",f"{x.artist.nunique():,}")
c4.metric("Avg popularity",f"{x.popularity.mean():.1f}" if len(x) else "—")

if len(x):
    tab1,tab2,tab3,tab4=st.tabs(["Timeline","Songs","Artists","Attributes"])
    with tab1:
        daily=x.groupby("date").agg(avg_rank=("position","mean"),avg_popularity=("popularity","mean"),top10_popularity=("popularity",lambda s:s[x.loc[s.index,"position"]<=10].mean())).reset_index()
        fig=px.line(daily,x="date",y=["avg_popularity","top10_popularity"],markers=False,title="Daily Popularity Trend")
        st.plotly_chart(fig,use_container_width=True)
        fig2=px.line(x.sort_values("date"),x="date",y="position",color="song",hover_data=["artist"],title="Song Ranking Timeline")
        fig2.update_yaxes(autorange="reversed")
        st.plotly_chart(fig2,use_container_width=True)
    with tab2:
        sm=x.groupby(["song","artist"]).agg(days_on_chart=("date","nunique"),avg_rank=("position","mean"),best_rank=("position","min"),rank_volatility=("position","std"),avg_popularity=("popularity","mean")).reset_index()
        sm["rank_volatility"]=sm.rank_volatility.fillna(0)
        st.dataframe(sm.sort_values(["days_on_chart","avg_rank"],ascending=[False,True]).head(50),use_container_width=True)
        fig=px.scatter(sm,x="days_on_chart",y="avg_popularity",size="days_on_chart",hover_name="song",hover_data=["artist","avg_rank","best_rank"],title="Song Longevity vs Popularity")
        st.plotly_chart(fig,use_container_width=True)
    with tab3:
        am=x.groupby("artist").agg(unique_songs=("song","nunique"),chart_appearances=("song","size"),avg_rank=("position","mean"),avg_popularity=("popularity","mean")).reset_index()
        am["slot_share"]=am.chart_appearances/len(x)
        st.dataframe(am.sort_values("chart_appearances",ascending=False).head(50),use_container_width=True)
        fig=px.bar(am.sort_values("chart_appearances",ascending=False).head(15),x="chart_appearances",y="artist",orientation="h",title="Artist Chart Appearances")
        st.plotly_chart(fig,use_container_width=True)
    with tab4:
        fig=px.box(x,x="is_explicit",y="position",title="Rank Distribution: Explicit vs Non-explicit")
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig,use_container_width=True)
        fig2=px.scatter(x,x="duration_min",y="popularity",color="album_type",hover_data=["song","artist"],title="Duration vs Popularity")
        st.plotly_chart(fig2,use_container_width=True)
        fig3=px.box(x,x="album_type",y="popularity",title="Popularity by Album Type")
        st.plotly_chart(fig3,use_container_width=True)
else:
    st.warning("No rows match the selected filters.")
