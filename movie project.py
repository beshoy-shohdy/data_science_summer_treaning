import pandas as pd

#load data
companies = pd.read_csv('companies.csv')
countries = pd.read_csv('countries.csv')
genres = pd.read_csv('genres.csv')
langs = pd.read_csv('langs.csv')
movie = pd.read_csv('movie_details.csv')

# Merge dataframes
merged_df = pd.merge(genres, companies, on="movie_id")
merged_df = pd.merge(merged_df, countries, on="movie_id")
merged_df = pd.merge(merged_df, langs, on="movie_id")
merged_df = pd.merge(merged_df, movie, on="movie_id")

#sort
merged_df = merged_df.sort_values(by="movie_id")

#remove duplicates
merged_df = merged_df.drop_duplicates("movie_id")

# Save merged dataframe to CSV
merged_df.to_csv('merged_movie_data.csv', index=False)

print("file is ready")
