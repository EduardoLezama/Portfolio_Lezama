import bs4
import requests

# creamos la url para obtener el numero de pagina
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista de libros de rating alto
rating_alto = []

# Iterar paginas
for pagina in range(1, 51):
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    libros = sopa.select('.product_pod')

    # Iterar libros
    for libro in libros:

        # Checar que sean amayor a 4
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Four')) != 0:

            titulo_libro = libro.select('a')[1]['title']

            rating_alto.append(titulo_libro)

# Ver libros
for t in rating_alto:
    print(t)


