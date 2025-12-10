import pandas as pd

df = pd.read_csv("MGSD_Expanded_sentiment_regard.csv")

# Show the first 5 rows
print(df.head())

# Show column names and types
print(df.info())

# Quick stats on numeric columns
print(df.describe())

df_sample = df.sample(1000, random_state=42)
df_sample.to_csv("MGSD_sentiment_sample.csv", index=False)

print(df['Sentiment'].value_counts())
print(df['Regard'].value_counts())

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x='stereotype_type', hue='Sentiment')
plt.title("Sentiment Distribution by Stereotype Type")
plt.show()

sns.countplot(data=df, x='stereotype_type', hue='Regard')
plt.title("Regard Distribution by Stereotype Type")
plt.show()
