import csv
import pandas as pd

df=pd.read_csv("dwarf_stars.csv")

df=df[df['Star_name'].notna()]
df=df[df['Distance'].notna()]