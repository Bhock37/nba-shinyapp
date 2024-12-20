import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

def unique_cols(columns):
    seen = {}
    new_columns = []
    
    for col in columns:
        if col in seen:
            seen[col] += 1
            new_columns.append(f"{col}_{seen[col]}")  # Rename by adding a suffix
        else:
            seen[col] = 0
            new_columns.append(col)
    
    return new_columns    

# Year and table type
year = 2025
tables = ['totals', 'per_game', 'per_minute', 'per_poss', 'advanced', 'play-by-play', 'shooting', 'adj_shooting']

# Loop through each table
for table in tables:
    dfs_list = []
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_{table}.html"
    print(f"Scraping {table} for {year-1}-{year}")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page {url}. Status code: {response.status_code}")
        continue

    soup = BeautifulSoup(response.content, 'html.parser')

    table_html = soup.find('table')

    if table_html:
        # Extract headers, excluding 'over_header' ths
        headers = [th.text for th in table_html.find('thead').find_all('th') if th.parent.get('class') != ['over_header']][1:]  # Skip the rank column
        headers = unique_cols(headers)
        # Extract data rows, skipping header rows with class 'over_header'
        rows = table_html.find('tbody').find_all('tr', class_=lambda x: x != 'over_header')  # Skip header rows

        data = []

        for row in rows:
            stats = [td.text for td in row.find_all('td')]
            if stats:
                data.append(stats)
            
        df = pd.DataFrame(data, columns=headers)
        df['Year'] = f"{year-1}-{year}"
        dfs_list.append(df)
        time.sleep(1)

    full_df = pd.concat(dfs_list, ignore_index=True)
    script_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
    filename = os.path.join(parent_dir, "data/current_data", f"current_{table}.csv")
    full_df.to_csv(filename, index = False)
    print(f"Data for {table} saved to {filename}")
