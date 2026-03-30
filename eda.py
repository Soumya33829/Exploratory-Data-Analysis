import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/sales.csv")

print(df.head())

df.drop_duplicates(inplace=True)

print(df.describe())

print(df.groupby("Region")["Profit"].sum())

sns.barplot(x="Region", y="Profit", data=df)
plt.show()

sns.histplot(df["Sales"])
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

sns.boxplot(x="Category", y="Sales", data=df)
plt.show()