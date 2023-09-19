from sqlalchemy import (
    Column,
    String,
    Integer,
)
from models import Base


class Movie(Base):
    """Classe que representa a tabela de filmes."""

    # O name da tabela no banco de dados
    __tablename__ = "movie"

    imdbID = Column(String(12), primary_key=True)

    Title = Column(String(255), nullable=False)

    Year = Column(String(4))
    Released = Column(String(10))
    Runtime = Column(String(12))
    Genre = Column(String(255))
    Director = Column(String(255))
    Writer = Column(String(255))
    Actors = Column(String(255))
    Plot = Column(String(255))
    Language = Column(String(255))
    Country = Column(String(255))
    Awards = Column(String(255))
    Poster = Column(String(255))
    Rated = Column(String(8))
    Metascore = Column(String(3))
    imdbRating = Column(String(3))
    imdbVotes = Column(String(12))
    Type = Column(String(255))
    DVD = Column(String(255))
    BoxOffice = Column(Integer)
    Production = Column(String(255))
    Website = Column(String(255))

    def __init__(
        self,
        imdbID: str,
        Title: str,
        Year: int,
        Released: str,
        Runtime: int,
        Genre: str,
        Director: str,
        Writer: str,
        Actors: str,
        Plot: str,
        Language: str,
        Country: str,
        Awards: str,
        Poster: str,
        Rated: str,
        Metascore: int,
        imdbRating: int,
        imdbVotes: int,
        Type: str,
        DVD: str,
        BoxOffice: int,
        Production: str,
        Website: str,
    ):
        """Cria um filme para ser adicionado à base."""
        self.imdbID = imdbID

        self.Title = Title

        self.Year = Year
        self.Released = Released
        self.Runtime = Runtime
        self.Genre = Genre
        self.Director = Director
        self.Writer = Writer
        self.Actors = Actors
        self.Plot = Plot
        self.Language = Language
        self.Country = Country
        self.Awards = Awards
        self.Poster = Poster
        self.Rated = Rated
        self.Metascore = Metascore
        self.imdbRating = imdbRating
        self.imdbVotes = imdbVotes
        self.Type = Type
        self.DVD = DVD
        self.BoxOffice = BoxOffice
        self.Production = Production
        self.Website = Website

    def to_dict(self):
        """Transforma o filme em um dicionário."""
        return {
            "imdbID": self.imdbID,
            "Title": self.Title,
            "Year": self.Year,
            "Released": self.Released,
            "Runtime": self.Runtime,
            "Genre": self.Genre,
            "Director": self.Director,
            "Writer": self.Writer,
            "Actors": self.Actors,
            "Plot": self.Plot,
            "Language": self.Language,
            "Country": self.Country,
            "Awards": self.Awards,
            "Poster": self.Poster,
            "Rated": self.Rated,
            "Metascore": self.Metascore,
            "imdbRating": self.imdbRating,
            "imdbVotes": self.imdbVotes,
            "Type": self.Type,
            "DVD": self.DVD,
            "BoxOffice": self.BoxOffice,
            "Production": self.Production,
            "Website": self.Website,
        }
