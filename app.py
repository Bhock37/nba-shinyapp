import streamlit as st
import pandas as pd
import os
import numpy as np

st.title("NBA Data Explorer")


path_prefix = "data/combined_data/combined_"
per_game = pd.read_csv(f"{path_prefix}per_game.csv")
per_game = per_game.drop(columns = ['Awards'])
seasons = per_game['Year'].unique()
seasons = np.sort(seasons)[::-1]
season = st.sidebar.selectbox(
    "Season",
    seasons
)

seasons_per_game = per_game[per_game['Year'] == season]

player = st.sidebar.selectbox(
    "Player",
    seasons_per_game['Player'].unique()
)

player_data = seasons_per_game[seasons_per_game['Player'] == player]

print(player_data.columns)

st.subheader(f"{player}'s stats for {season}")
player_data = player_data.drop(columns = ['Year'])
st.dataframe(player_data, use_container_width=True, hide_index=True)
