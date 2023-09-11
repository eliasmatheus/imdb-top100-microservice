import requests
from concurrent.futures import ThreadPoolExecutor

from helpers import parse_results


def get_movies(engine):
    """Faz um web scraping nos top 100 do site imdb.

    E salva os filmes encontrados na base.
    """
    # urls para fazer o web scraping. Segunda e primeira página dos top 100.
    urls = [
        "https://www.imdb.com/search/title/?groups=top_100&start=51&ref_=adv_nxt",
        "https://www.imdb.com/search/title/?groups=top_100&ref_=adv_prv",
    ]

    headers = {"Accept-Language": "en-US, en;q=0.5"}

    def get_url(url):
        """Faz uma requisição get na url passada."""
        return requests.get(url, headers=headers)

    # cria um pool de threads para fazer as requisições
    with ThreadPoolExecutor(max_workers=3) as pool:
        responses = list(pool.map(get_url, urls))

    for response in responses:
        # para cada resposta, faz o parse dos filmes
        result = parse_results(response)

        # salva os filmes na base
        result.to_sql(
            name="movie", con=engine, if_exists="replace", index=False
        )
