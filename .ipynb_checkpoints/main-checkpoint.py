import pandas as pd

dtFrame = pd.read_csv("./dataset_tugas1_preprocessing.csv")
dtFrame.head()
dtFrame.isnull().sum()
dtFrame["Umur"].dropna(axis=0)

dtFrame["Nilai_Akhir"].fillna(dtFrame["Nilai_Akhir"].mean())
print(dtFrame)