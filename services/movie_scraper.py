import requests
from concurrent.futures import ThreadPoolExecutor

from helpers import parse_results
from services import MDbApi

from logger import logger
from models import Movie
from sqlalchemy.orm import sessionmaker

api = MDbApi()


def get_movies(engine):
    """Faz um web scraping nos top 100 do site imdb.

    E salva os filmes encontrados na base.
    """
    # urls para fazer o web scraping. Segunda e primeira página dos top 100.
    urls = [
        "https://www.imdb.com/search/title/?groups=top_100&ref_=adv_prv",
        "https://www.imdb.com/search/title/?groups=top_100&start=51&ref_=adv_nxt",
    ]

    headers = {"Accept-Language": "en-US, en;q=0.5"}

    def get_url(url):
        """Faz uma requisição get na url passada."""
        return requests.get(url, headers=headers)

    # cria um pool de threads para fazer as requisições
    with ThreadPoolExecutor(max_workers=3) as pool:
        responses = list(pool.map(get_url, urls))

    movies = []

    for response in responses:
        # para cada resposta, faz o parse dos filmes
        result = parse_results(response)

        movies += result.to_dict("records")

    ids = [movie["imdbID"] for movie in movies]

    # busca os filmes na API do imdb
    movies = api.get_movies_by_ids(ids)

    # cria uma sessão para salvar os filmes na base
    Session = sessionmaker(bind=engine)
    session = Session()

    # salva os filmes na base
    for movie in movies:
        movie.pop("Response", None)
        movie.pop("Ratings", None)
        session.add(Movie(**movie))
        session.commit()

    logger.info(f"%d filmes salvos na base" % len(movies))
