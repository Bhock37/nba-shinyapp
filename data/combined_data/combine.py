import pandas as pd
import os

script_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
path_to_curr = os.path.join(parent_dir, "current_data")
path_to_hist = os.path.join(parent_dir, "historic_data")

tables = ['totals', 'per_game', 'per_minute', 'per_poss', 'advanced', 'play-by-play', 'shooting', 'adj_shooting']

for table in tables:
    curr_path = os.path.join(path_to_curr, f"current_{table}.csv")
    hist_path = os.path.join(path_to_hist, f"historic_{table}.csv")
    current = pd.read_csv(curr_path)
    historic = pd.read_csv(hist_path, dtype={30:'str'})
    combined = pd.concat([current, historic], ignore_index=True)
    filename = os.path.join(parent_dir, "combined_data", f"combined_{table}.csv")
    combined.to_csv(filename, index = False)
    print(f"{table} data combined")
