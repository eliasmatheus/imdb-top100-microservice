from pydantic import BaseModel
from typing import Optional, List

from models import Movie


class MovieResponseSchema(BaseModel):
    """Define como um filme será representado."""

    imdbID: str = "tt0848228"
    Title: str = "The Avengers"
    Year: str = "2012"
    Runtime: str = "143 min"
    Poster: str = (
        "https://m.media-amazon.com/images/M/"
        "MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmY"
        "jU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg"
    )
    Type: str = "movie"


class MoviesListResponseSchema(BaseModel):
    """Define como uma lista de filmes será representada."""

    movies: List[MovieResponseSchema]


def present_movies(movies: Movie):
    """Retorna lista de filmes."""
    result = []

    for movie in movies:
        result.append(
            {
                "imdbID": movie.imdb_id,
                "Title": movie.title,
                "Year": movie.year,
                "Runtime": movie.runtime,
                "Poster": movie.poster,
                "Type": "movie",
            }
        )

    return {"movies": result}
