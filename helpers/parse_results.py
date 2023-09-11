from bs4 import BeautifulSoup
import pandas as pd
import locale

# Defina a localização para o formato desejado (por exemplo, en_US para inglês nos EUA)
locale.setlocale(
    locale.LC_ALL, "en_US.UTF-8"
)  # Altere o valor da localização conforme necessário


def parse_results(results):
    """Faz o parse do resultado da busca no imdb.

    Solução baseada em:
    https://abdulrwahab.medium.com/how-to-build-a-python-web-scraper-to-capture-imdb-top-100-movies-908bf9b6bc19
    """
    # Parse the results object to movie_soup using the html parser.
    movie_soup = BeautifulSoup(results.text, "html.parser")

    # Extract these attributes (to a list) from the movie_soup.
    titles = []
    years = []
    runtimes = []
    imdb_ratings = []
    imdb_ids = []
    metascores = []
    imdb_votes = []
    box_offices = []
    genres = []
    plots = []
    posters = []

    # Create a movie_div object to find all div objects in movie_soup.
    movie_div = movie_soup.find_all("div", class_="lister-item mode-advanced")

    # Loop through each object in the movie_div.
    for container in movie_div:
        # Add each result from each attribute for each list.

        # name
        name_text = container.h3.a.text
        titles.append(name_text)

        # year
        year_text = container.h3.find("span", class_="lister-item-year").text
        years.append(year_text)

        # runtime
        runtime_text = (
            container.p.find("span", class_="runtime").text
            if container.p.find("span", class_="runtime").text
            else "-"
        )
        runtimes.append(runtime_text)

        # IMDB rating
        imdb = container.strong.text
        imdb_ratings.append(imdb)

        # IMDB id
        id = container.find("span", class_="userRatingValue")["data-tconst"]
        imdb_ids.append(id)

        # genre
        genre = container.p.find("span", class_="genre").text
        genres.append(genre)

        # plot
        plot = container.find_all("p", class_="text-muted")[1].text
        plots.append(plot)

        # poster
        poster = container.find("img", class_="loadlate")["loadlate"]
        posters.append(poster)

        # metascore
        m_score = (
            container.find("span", class_="metascore").text
            if container.find("span", class_="metascore")
            else "-"
        )
        metascores.append(m_score)

        # There are two NV containers, grab both of them as they hold both the
        # votes and the grosses
        nv = container.find_all("span", attrs={"name": "nv"})

        # filter nv for votes
        vote = nv[0].text
        imdb_votes.append(vote)

        # filter nv for gross
        grosses = nv[1].text if len(nv) > 1 else 0
        box_offices.append(grosses)

    # Build and store all of the attributes into the Pandas movie dataframe.
    movies = pd.DataFrame(
        {
            "title": titles,
            "year": years,
            "runtime": runtimes,
            "imdb_rating": imdb_ratings,
            "imdb_id": imdb_ids,
            "metascore": metascores,
            "imdb_votes": imdb_votes,
            "box_office": box_offices,
            "genre": genres,
            "plot": plots,
            "poster": posters,
        }
    )

    # Use Pandas str.extract to remove all String characters, and save the
    # value as type int for cleaning up the data with Pandas.
    movies["year"] = movies["year"].str.strip()
    movies["runtime"] = movies["runtime"].str.strip()
    movies["metascore"] = movies["metascore"].str.strip()

    movies["imdb_votes"] = movies["imdb_votes"].str.strip()
    movies["box_office"] = movies["box_office"].map(
        lambda x: x.lstrip("$").rstrip("M")
    )
    movies["box_office"] = pd.to_numeric(movies["box_office"], errors="coerce")
    # Aplicar a função de formatação à coluna 'box_office'
    movies["box_office"] = movies["box_office"].apply(format_box_office)

    movies["genre"] = movies["genre"].str.replace("\n", "").str.strip()
    movies["plot"] = movies["plot"].str.replace("\n", "")

    return movies


def format_box_office(value):
    """Função para formatar o valor do box_office."""
    if value == 0:
        return "0"

    # se for uma string
    if isinstance(value, str):
        return value

    return locale.currency(value * 1000000, grouping=True, symbol=False)
