import pandas as pd

stats = ["shooting","passing","gca","possession","defense"]
dfs = []
for stat in stats:
    url = fr"https://fbref.com/en/comps/Big5/{stat}/players/Big-5-European-Leagues-Stats"
    dfs.append(pd.read_html(url)[0])

merged_df: pd.DataFrame = pd.concat(dfs, axis=1)
players = merged_df.iloc[:,0:9]
duplicate_columns = set()
for i in range(len(merged_df.columns)):
    col1 = merged_df.iloc[:, i]
    for j in range(i + 1, len(merged_df.columns)):
        col2 = merged_df.iloc[:, j]
        if col1.equals(col2):
            duplicate_columns.add(merged_df.columns[j])

merged_df = merged_df[merged_df.iloc[:, 0] != "Rk"]
players = players[players.iloc[:,0] != "Rk"]

# Drop duplicate columns
merged_df = merged_df.drop(columns=duplicate_columns)
merged_df = pd.concat([players, merged_df], axis = 1)
merged_df.columns = ['{}--{}'.format(col[0], col[1]) for col in merged_df.columns]
cols = list(merged_df.columns)
for i,col in enumerate(cols):
    if "Unnamed" in col:
        cols[i] = col.split("--")[1]
merged_df.columns = cols
merged_df.to_csv("Big5.csv", index=False)
players.to_csv("Players.csv")
print("done")