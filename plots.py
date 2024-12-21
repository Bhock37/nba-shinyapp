import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def bio(data : pd.DataFrame, player_name: str, season: str, ax : plt.Axes):
    player_filtered = data[data["Player"] == player_name]
    player_data = player_filtered[player_filtered["Year"] == season]
    name = player_data["Player"].iloc[0]
    season = player_data["Year"].iloc[0]
    games_played = player_data["G"].iloc[0]
    age = player_data["Age"].iloc[0]
    team = player_data["Team"].iloc[0]
    position = player_data["Pos"].iloc[0]
    ax.text(0.5, 1, f'{name}', va='top', ha='center', fontsize=56)
    ax.text(0.5, 0.65, f'{team}, Age: {int(age)}, {position}', va='top', ha='center', fontsize=30)
    ax.text(0.5, 0.5, f"Games Played: {games_played}", va = 'top', ha = 'center', fontsize = 30)
    ax.text(0.5, 0.40, f'Season Summary', va='top', ha='center', fontsize=40)
    ax.text(0.5, 0.15, f'{season}', va='top', ha='center', fontsize=30, fontstyle='italic')

    ax.axis('off')

def summary(data : pd.DataFrame, player_name: str, season: str, stats : list, ax : plt.Axes):
    print(1)

path_prefix = "data/combined_data/combined_"
per_game = pd.read_csv(f"{path_prefix}per_game.csv")

plt.figure()
bio(per_game, "Jayson Tatum", "2024-2025", plt.subplots(figsize=(10, 4))[1])
plt.savefig('test')