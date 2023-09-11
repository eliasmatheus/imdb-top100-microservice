from pydantic import BaseModel
from typing import Optional, List

from models import Movie


class MovieResponseSchema(BaseModel):
    """Define como um filme será representado."""

    imdbID: str = "tt0848228"
    Title: str = "The Avengers"
    Year: str = "2012"
    Runtime: str = "143 min"
    imdbRating: str = "8.0"
    Metascore: Optional[str] = "69"
    imdbVotes: str = "1,285,614"
    BoxOffice: Optional[str] = "$623,279,547"
    Genre: str = "Action, Adventure, Sci-Fi"
    Plot: str = (
        "Earth's mightiest heroes must come together and learn to"
        "fight as a team if they are going to stop the mischievous Loki and"
        "his alien army from enslaving humanity."
    )
    Poster: str = (
        "https://m.media-amazon.com/images/M/"
        "MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmY"
        "jU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg"
    )


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
                "imdbRating": movie.imdb_rating,
                "Metascore": movie.metascore,
                "imdbVotes": movie.imdb_votes,
                "BoxOffice": movie.box_office,
                "Genre": movie.genre,
                "Plot": movie.plot,
                "Poster": movie.poster,
            }
        )

    return {"movies": result}
