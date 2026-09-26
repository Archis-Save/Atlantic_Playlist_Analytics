# Atlantic_Playlist_Analytics

# Historical Playlist Analytics — Atlantic United States

## 📊 Project Overview

This project analyzes historical daily Top 50 playlist data for Atlantic Recording Corporation to understand how songs, artists, rankings, and popularity changed over time.

The analysis focuses on historical patterns rather than prediction or recommendation.

### Key questions

* Which songs remained on the chart for the longest periods?
* Which songs maintained strong rankings?
* How volatile were song rankings?
* Which artists had repeated appearances?
* How does popularity relate to chart position?
* Does explicit content show differences in chart performance?
* How do song duration and album type relate to popularity?

---

## 📁 Dataset

The dataset contains daily playlist observations with the following fields:

* `date`
* `position`
* `song`
* `artist`
* `popularity`
* `duration_ms`
* `album_type`
* `total_tracks`
* `is_explicit`
* `album_cover_url`

### Dataset coverage

* Period: May 2024 – November 2025
* Original observations: 27,800
* Cleaned observations: 27,752
* Unique songs: 943
* Unique artists: 297
* Playlist positions: 1–50

A duplicate-date/song/artist anomaly was identified during data validation and handled during preprocessing.

---

## 🔧 Data Preparation

The following preprocessing steps were performed:

1. Converted dates into a standard date format.
2. Checked missing values and invalid records.
3. Identified duplicate date/song/artist observations.
4. Removed duplicate observations created by the anomalous duplicate playlist entry.
5. Converted song duration from milliseconds to minutes.
6. Created song-level and artist-level analytical metrics.

---

## 📐 Key Metrics

### Days on Chart

Number of distinct dates on which a song appeared.

### Average Rank

Average playlist position of a song.

Lower values represent stronger average positions.

### Best Rank

Highest position achieved by a song.

### Rank Volatility Index

Standard deviation of a song's playlist position.

Higher values indicate greater movement in ranking.

### Popularity Trend

Popularity attributes supplied with the dataset were analyzed across the historical observations.

### Artist Dominance

Artist contribution was evaluated using:

* Number of unique songs
* Total chart appearances
* Average ranking
* Average popularity
* Share of playlist observations

### Explicit Content Share

Percentage of observations classified as explicit.

---

## 📈 Key Findings

### Song longevity

**"Something in the Orange" by Zach Bryan** had the longest observed chart presence, appearing on the playlist for approximately **536 days**.

### Artist presence

Taylor Swift had approximately **2,015 playlist appearances across 96 unique songs** in the cleaned dataset.

### Popularity and ranking

The relationship between row-level popularity and playlist position was weakly negative, with a correlation of approximately **-0.094**.

This indicates that higher supplied popularity values were generally associated with somewhat better rankings, but the relationship was not strong.

### Longevity and popularity

Song-level average popularity showed a positive association with days on chart, with a correlation of approximately **0.350**.

This suggests that songs with stronger average supplied popularity tended to remain visible on the playlist for longer periods in this dataset.

### Explicit content

Explicit and non-explicit songs showed broadly similar average ranking patterns in the historical observations.

### Album type

Single releases showed higher average supplied popularity than album-track observations in this dataset.

These findings describe historical associations and should not be interpreted as causal relationships.

---

## 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit dashboard.

### Dashboard features

* Date range filtering
* Artist filtering
* Song filtering
* Rank range filtering
* Album type filtering
* Explicit/non-explicit filtering
* Playlist timeline exploration
* Song ranking trends
* Song longevity analysis
* Artist leaderboard
* Popularity vs ranking analysis
* Explicit-content analysis
* Duration vs popularity analysis
* Album-type comparison

---

## 🚀 Running the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run streamlit_app.py
```

The dashboard will open in your browser.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* Python-docx
* Jupyter/Python-based data analysis

---

## 📄 Project Deliverables

The repository contains:

* Research paper
* Executive summary
* Cleaned dataset
* Streamlit dashboard
* Requirements file
* Project documentation

---

## ⚠️ Limitations

The dataset represents playlist observations and supplied popularity attributes. It does not provide direct daily streaming counts.

Therefore:

* Playlist position should not be interpreted as exact stream volume.
* Popularity should not be interpreted as daily streams.
* Correlation does not establish causation.
* Historical patterns do not guarantee future performance.

---

## 🎯 Conclusion

This project provides a historical view of playlist performance across songs and artists.

The analysis demonstrates how ranking persistence, popularity, artist presence, content attributes, and song characteristics can be combined to understand playlist dynamics over time.

The Streamlit dashboard allows users to interactively explore these historical patterns through filters and visualizations.
