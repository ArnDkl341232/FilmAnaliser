# Films Data Analysis

This project performs the analysis of dataset(movies_metadata.csv) from the information about films.

Goal:   identify key trends,popular genres, 
the relationship between budget and profit,
and also examine changes in the popularity of films over the years.

## Data

Used data set have 45,466 notes and 24 columns.

Main columns:
- `title` : Film name.
- `budget` : Budget.
- `revenue` : Film revenue.
- `release_date` : Release date.
- `genres` : Genres in JSON.
- `popularity` : Popularity.
- `vote_average` : Vote average.


### Data clearing

1. Deleted notations without dates, with incorrect budget or income.
2. JSON format genres are divided into separate lines.
3. Added new columns: `release_year`.
4. 

