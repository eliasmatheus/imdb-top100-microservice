from flask_openapi3 import Tag, APIBlueprint

from schemas import *
from schemas import ErrorSchema

from logger import logger
from models import Session, Movie
from sqlalchemy.exc import IntegrityError


movie_tag = Tag(
    name="Movie",
    description="Busca os top 100 filmes mais populares no imdb salvos na base",
)

movie_bp = APIBlueprint("movie", __name__)


@movie_bp.get(
    "/movies",
    tags=[movie_tag],
    responses={
        "200": MoviesListResponseSchema,
        "404": ErrorSchema,
    },
)
def get_movies():
    """Faz a busca dos filmes salvos na base."""
    logger.info(f"Buscando filmes ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    movies = session.query(Movie).all()

    if not movies:
        # se não há filmes cadastrados
        return {"filmes": []}, 200
    else:
        logger.info(f"%d filmes encontrados" % len(movies))
        # retorna a representação de produto
        return present_movies(movies), 200
