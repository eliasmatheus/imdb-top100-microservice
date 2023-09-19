from pydantic import BaseModel
from typing import Optional, List

from models import Movie


class MovieResponseSchema(BaseModel):
    """Define como um filme será representado."""

    Title: str = "The Avengers"
    Year: int = "2012"
    Rated: str = "PG-13"
    Released: str = "04 May 2012"
    Runtime: str = "143 min"
    Genre: str = "Action, Adventure, Sci-Fi"
    Director: str = "Joss Whedon"
    Writer: str = (
        "Joss Whedon (screenplay), Zak Penn (story), Joss Whedon (story)"
    )
    Actors: str = "Robert Downey Jr., Chris Evans, Scarlett Johansson"
    Plot: str = (
        "Earth's mightiest heroes must come together and learn to"
        "fight as a team if they are going to stop the mischievous Loki and"
        "his alien army from enslaving humanity."
    )
    Language: str
    Country: str = "United States"
    Awards: str = "Nominated for 1 Oscar. 38 wins & 80 nominations total"
    Poster: str = (
        "https://m.media-amazon.com/images/M/"
        "MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmY"
        "jU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg"
    )
    Rated: str = "PG-13"
    Metascore: str = "69"
    imdbRating: str = "8.0"
    imdbVotes: str = "1,285,614"
    imdbID: str = "tt0848228"
    Type: str = "movie"
    DVD: str = "22 Jun 2014"
    BoxOffice: str = "$623,279,547"
    Production: str = "N/A"
    Website: str = "N/A"


class MoviesListResponseSchema(BaseModel):
    """Define como uma lista de filmes será representada."""

    movies: List[MovieResponseSchema]


def present_movies(movies: list[Movie]):
    """Retorna lista de filmes."""
    result = []

    for movie in movies:
        result.append(movie.to_dict())

    return {"movies": result}
