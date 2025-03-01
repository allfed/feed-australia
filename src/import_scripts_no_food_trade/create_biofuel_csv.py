import pandas as pd
import git
from pathlib import Path

repo_root = git.Repo(".", search_parent_directories=True).working_dir

print("importing biofuels data...")

NO_TRADE_XLS = (
    Path(repo_root)
    / "data"
    / "no_food_trade"
    / "raw_data"
    / "Integrated Model With No Food Trade.xlsx"
)

xls = pd.ExcelFile(NO_TRADE_XLS)

df_biofuel = pd.read_excel(xls, "Biofuel")[
    [
        "ISO3 Country Code",
        "Country",
        "Biofuel/other caloric consumption in 2020 (million dry caloric tons)",
        "Biofuel/other fat consumption in 2020 (tonnes)",
        "Biofuel/other protein consumption in 2020 (tonnes)",
    ]
]

# Rename columns
df_biofuel.columns = [
    "iso3",
    "country",
    "biofuel_kcals",
    "biofuel_fat",
    "biofuel_protein",
]


df_biofuel["biofuel_kcals"] = df_biofuel["biofuel_kcals"] * 1e6
df_biofuel["biofuel_fat"] = df_biofuel["biofuel_fat"] * 1e6
df_biofuel["biofuel_protein"] = df_biofuel["biofuel_protein"] * 1e6
df_biofuel = df_biofuel.iloc[
    0:138,
]

df_biofuel.to_csv(
    Path(repo_root) / "data" / "no_food_trade" / "processed_data" / "biofuel_csv.csv",
    sep=",",
    index=False,
)
