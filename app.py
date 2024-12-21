import streamlit as st
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from plots import bio

st.title("NBA Player Profile")


path_prefix = "data/combined_data/combined_"
per_game = pd.read_csv(f"{path_prefix}per_game.csv")
per_game = per_game.drop(columns = ['Awards'])
seasons = per_game['Year'].unique()
seasons = np.sort(seasons)[::-1]

col1, col2, col3 = st.columns(3)
with col1:
    season = st.selectbox(
        "Season:",
        seasons
    )

    seasons_per_game = per_game[per_game['Year'] == season]

with col2:
    teams = seasons_per_game['Team'].dropna().unique()
    teams = np.sort(teams)
    team = st.selectbox(
        "Team:",
        teams    
    )
    teams_per_game = seasons_per_game[seasons_per_game['Team'] == team]

with col3:
    player = st.selectbox(
        "Player:",
        teams_per_game['Player'].unique()
    )

    player_data = teams_per_game[teams_per_game['Player'] == player]

st.subheader(f"{player} - {season}")

player_data = player_data.drop(columns = ['Year'])
st.dataframe(player_data, use_container_width=True, hide_index=True)

fig, ax = plt.subplots(figsize=(10, 4))
bio(per_game, player, season, ax)
st.pyplot(fig)

print("App Running/Updated")


