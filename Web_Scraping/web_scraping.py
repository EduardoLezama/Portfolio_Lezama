import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/courses')

# print(resultado.text)
# print(sopa.select('h1')[0].getText())

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

img_curso_1 = requests.get(imagenes)
f = open('mi_imagen.jpg', 'wb')
f.write(img_curso_1.content)
f.close()