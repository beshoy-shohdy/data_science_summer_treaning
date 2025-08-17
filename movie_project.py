import pandas as pd
import matplotlib.pyplot as plt

def file_ready():
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

    #cleaning
    merged_df = merged_df.drop(columns=["homepage"])
    merged_df = merged_df.drop(columns=["backdrop_path"])
    merged_df = merged_df.drop(columns=["poster_path"])
    merged_df = merged_df.drop(columns=["tagline"])
    merged_df = merged_df.dropna(subset=["company_country"])
    merged_df = merged_df.dropna(subset=["imdb_id"])
    merged_df = merged_df.dropna(subset=["overview"])
    merged_df = merged_df.dropna(subset=["release_date"])

    # Save merged dataframe to CSV
    merged_df.to_csv('merged_movie_data.csv', index=False)

    print("file is ready")


