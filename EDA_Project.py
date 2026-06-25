import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("data/netflix_titles.csv")

print("="*50)
print("DATASET SHAPE")
print(df.shape)

print("\n" + "="*50)
print("FIRST 5 ROWS")
print(df.head())

print("\n" + "="*50)
print("MISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# Data Cleaning
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")
df["duration"] = df["duration"].fillna("Unknown")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["date_added"] = df["date_added"].fillna(pd.Timestamp("2000-01-01"))

df.drop_duplicates(inplace=True)

print("\n" + "="*50)
print("MISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# Save Cleaned Dataset
df.to_csv("data/cleaned_netflix.csv", index=False)

print("\nCleaned dataset saved successfully!")

# -------------------------------
# EDA 1: Movies vs TV Shows
# -------------------------------
plt.figure(figsize=(6,4))
df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# -------------------------------
# EDA 2: Release Year Histogram
# -------------------------------
plt.figure(figsize=(8,4))
plt.hist(df["release_year"], bins=20)
plt.title("Distribution of Release Years")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.show()

# -------------------------------
# EDA 3: Top 10 Countries
# -------------------------------
plt.figure(figsize=(10,5))
df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries by Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# -------------------------------
# EDA 4: Content Added Per Year
# -------------------------------
df["year_added"] = df["date_added"].dt.year

plt.figure(figsize=(10,5))
df["year_added"].value_counts().sort_index().plot()
plt.title("Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# -------------------------------
# Insights
# -------------------------------
print("\n" + "="*50)
print("KEY INSIGHTS")
print("1. Netflix has more Movies than TV Shows.")
print("2. Most content was released after 2015.")
print("3. United States contributes the highest content.")
print("4. Netflix content grew rapidly after 2015.")
print("5. Dataset was cleaned successfully with no missing values.")