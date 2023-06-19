# Write code here
import pandas as pd
df=pd.read_csv("ecdict.mini.csv")
print(df[["word","translation"]])