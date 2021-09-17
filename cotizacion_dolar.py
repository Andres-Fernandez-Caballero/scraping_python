import requests  # Esta libreria trae la pagina web
from bs4 import BeautifulSoup  # Esta libreria facilita el manejo, filtrado de etiquetas html, y css

URL = "https://dolarhoy.com/cotizaciondolarblue"  # pagina web a analizar
page = requests.get(URL) # obtengo el codigo html de la pagina

soup = BeautifulSoup(page.content, "html.parser")  # inicio el objeto BeautifulSoup (siempre de esta manera)

# filtro la pagina y solo me quedo con el contenedor de dolares
contenedor_dolares = soup.find("div", class_="tile is-parent is-8")
# print(contenedor_dolares.prettify())  # muestro el contenedor

#vuelvo a filtrar dentro del contenedor buscando todos las las etiquetas div
# que tengan la clase is-child find_all DEVUELVE UNA LISTA DE OBJETOS (IMPORTANTE)
# <div class="is-child>
#   contenido de la etiqueta
# </div>
contenedores = contenedor_dolares.find_all("div", class_="is-child")
# print(contenedores)  # muetro el contenido

for contenedor_dolaresenedor in contenedores:
    # recorro la lista y busco los div con la clase topic y value
    # que representan la accion de compra venta y la cotizacion
    accion = contenedor_dolaresenedor.find("div", class_="topic")
    cotizacion = contenedor_dolaresenedor.find("div", class_="value")

    if('Venta' in accion):  # si la accion es venta muestro por pantalla
        print(str("Accion: " + accion.string + " Contizacion: " + cotizacion.string))
