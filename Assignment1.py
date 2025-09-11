import pandas as pd
df = pd.read_csv('rollercoasters.csv')
print(df.head())
print(df.columns)

most_common_speed = df['avg_speed'].mode()[0]
print(f"The most common average speed is: {most_common_speed}")
