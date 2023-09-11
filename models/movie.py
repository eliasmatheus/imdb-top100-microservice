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

    imdb_id = Column(String(12), primary_key=True)
    title = Column(String(255), nullable=False)
    year = Column(String(4), nullable=False)
    runtime = Column(String(10))
    imdb_rating = Column(String(3))
    metascore = Column(String(3))
    imdb_votes = Column(String(12))
    box_office = Column(Integer)
    genre = Column(String(255))
    plot = Column(String(255))
    poster = Column(String(255))

    def __init__(
        self,
        imdb_id: str,
        title: str,
        year: int,
        runtime: int,
        imdb_rating: int,
        metascore: int,
        imdb_votes: int,
        box_office: int,
        genre: str,
        plot: str,
        poster: str,
    ):
        """Cria um filme para ser adicionado à base.

        Arguments:
            imdb_id: id do filme no imdb.
            title: nome do filme.
            year: ano de lançamento do filme.
            runtime: duração do filme em minutos.
            imdb_rating: nota do filme no imdb.
            metascore: nota do filme no metascore.
            imdb_votes: número de votos do filme no imdb.
            box_office: arrecadação do filme em milhões de dólares.
            genre: gênero do filme.
            plot: sinopse do filme.
            poster: url do poster do filme.
            created_at: data de criação do filme.
        """
        self.imdb_id = imdb_id
        self.title = title
        self.year = year
        self.runtime = runtime
        self.imdb_rating = imdb_rating
        self.metascore = metascore
        self.imdb_votes = imdb_votes
        self.box_office = box_office
        self.genre = genre
        self.plot = plot
        self.poster = poster
