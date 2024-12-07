import pandas
import  matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import ast

#download dataset
url = "movies_metadata.csv"
movies_df = pd.read_csv(url)

#output info about database
# movies_df.info()
# print(movies_df.head())
# print(movies_df.describe())

def extract_genres(genres_str):
    try:
        genres = ast.literal_eval(genres_str)
        return [genre['name'] for genre in genres]
    except ValueError:
        return []

# print(movies_df['genres'])
movies_df['genres'] = movies_df['genres'].apply(extract_genres)
# print(movies_df['genres'])

#-----------------------------------------------------------------------------------------------------------------------

movies_df['budget'] = pd.to_numeric(movies_df['budget'], errors='coerce')
movies_df['revenue'] = pd.to_numeric(movies_df['revenue'], errors='coerce')


movies_df.dropna(subset=['budget', 'revenue'], inplace=True)

# print(movies_df['budget'])
# print(movies_df['revenue'])

#-----------------------------------------------------------------------------------------------------------------------
movies_df['release_year'] = pd.to_datetime(movies_df['release_date'], errors='coerce').dt.year
print(movies_df['release_year'])

#-----------------------------------------------------------------------------------------------------------------------

genres_exploded = movies_df[['title', 'release_year', 'budget', 'revenue', 'genres']].explode('genres')
print(genres_exploded)

genre_count = genres_exploded['genres'].value_counts()
print(genre_count)

# Visualization of genres
plt.figure(figsize=(10,6))
sns.barplot(x=genre_count.index, y=genre_count.values)
plt.title("Amount of films by genres")
plt.xlabel("Genr")
plt.ylabel("Amount of films")
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()


#-----------------------------------------------------------------------------------------------------------------------

movies_df['popularity'] = pd.to_numeric(movies_df['popularity'], errors='coerce')
popularity_trend = movies_df.groupby('release_year')['popularity'].mean()

# Visualization of popularity trends

plt.figure(figsize=(12,6))
popularity_trend.plot()
plt.title("Average popularity of films by year")
plt.xlabel("Year")
plt.ylabel("Popularity")
# plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()

#-----------------------------------------------------------------------------------------------------------------------
movies_df['profit'] = movies_df['revenue'] - movies_df['budget']

plt.figure(figsize=(10,6))
sns.scatterplot(data = movies_df, x="budget" , y="profit", alpha=0.3)
plt.title("Budget vs profit")
plt.xlabel("Budget")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

cleaned_file_path = 'cleaned_movies_metadata.csv'
movies_df.to_csv(cleaned_file_path, index = False)

