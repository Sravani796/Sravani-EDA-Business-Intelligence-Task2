import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv('cleaned_housing_data.csv')

print("Dataset Shape:", df.shape)
print("\nSummary Statistics:\n", df.describe())
print("\nCorrelation Matrix:\n", df.corr(numeric_only=True))

# Histogram for price
df['price'].hist(bins=50)
plt.title('House Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: area vs price
plt.scatter(df['area'], df['price'])
plt.title('Area vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
# Bar chart: furnishing status count
df['furnishingstatus'].value_counts().plot(kind='bar')
plt.title('Furnishing Status Distribution')
plt.xlabel('Furnishing Status')
plt.ylabel('Count')
plt.show()

# Top insights
avg_price = df['price'].mean()
max_price = df['price'].max()
min_price = df['price'].min()

print(f"\nAverage House Price: {avg_price}")
print(f"Highest House Price: {max_price}")
print(f"Lowest House Price: {min_price}")