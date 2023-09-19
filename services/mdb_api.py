from concurrent.futures import ThreadPoolExecutor
import requests
import os


def is_docker():
    """Verifica se o container está rodando em um ambiente docker."""
    path = "/proc/self/cgroup"
    return (
        os.path.exists("/.dockerenv")
        or os.path.isfile(path)
        and any("docker" in line for line in open(path))
    )


class MDbApi:
    def get_movies_by_ids(self, imdb_id: list[str]):
        """Busca um filme na API do imdb."""
        host = "http://localhost"

        if is_docker():
            host = "http://host.docker.internal"

        urls = [f"{host}:5000/movies/{id}" for id in imdb_id]

        def get_url(url):
            """Faz uma requisição get na url passada."""
            return requests.get(url).json()

        # cria um pool de threads para fazer as requisições
        with ThreadPoolExecutor(max_workers=3) as pool:
            responses = list(pool.map(get_url, urls))

        for movie in responses:
            movie.pop("Response", None)
            movie.pop("Ratings", None)

        return responses
