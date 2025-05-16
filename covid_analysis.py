import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv('owid-covid-data.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("File not found. Please check the path.")

# Display first few rows
print(df.head())

# Explore the structure
print(df.info())
print(df.describe())

# Clean missing data
df_cleaned = df.dropna()

# Grouping example: Average by country (change based on your actual data)
if 'Country Name' in df.columns and 'Indicator Value' in df.columns:
    country_avg = df.groupby('Country Name')['Indicator Value'].mean()
    print(country_avg.head())

# ----- Data Visualizations -----

# 1. Line Chart: Trend of a country over time
plt.figure(figsize=(10, 5))
sample_country = df[df['Country Name'] == 'South Africa']
plt.plot(sample_country['Year'], sample_country['Indicator Value'])
plt.title('South Africa - Indicator Trend Over Time')
plt.xlabel('Year')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# 2. Bar Chart: Average per Country
country_avg.sort_values(ascending=False).head(10).plot(kind='bar', title='Top 10 Countries by Avg Indicator')
plt.ylabel('Average Value')
plt.show()

# 3. Histogram
plt.hist(df_cleaned['Indicator Value'], bins=30, color='skyblue')
plt.title('Distribution of Indicator Values')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot: Example of two variables if available
if 'Indicator Value' in df.columns and 'Year' in df.columns:
    sns.scatterplot(data=df, x='Year', y='Indicator Value')
    plt.title('Scatter of Value vs Year')
    plt.show()
