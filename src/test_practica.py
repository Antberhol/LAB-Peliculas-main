from practicar_peliculas import *
from peliculas import *

def test_leer_peliculas():
    datos=leer_peliculas("./data/peliculas.csv")
    print("el primer registro es:", datos[0])
"""
def test_peliculas_por_actor():
    datos=leer_peliculas("./data/peliculas.csv")
    print("las peliculas por actor son:",peliculas_por_actor(datos, 2010, 2020))
    """
def test_pelis_mas_ganancias():
    datos=leer_peliculas("./data/peliculas.csv")
    print("las peliculas con mas ganancias son:", pelicula_mas_ganancias(datos, {"Drama"}))

def test_media_presupuesto_por_genero():
    datos=leer_peliculas("./data/peliculas.csv")
    print("la media de presupuesto por genero es:", media_presupuesto_genero(datos))
def test_peliculas_por_actor():
    datos=leer_peliculas("./data/peliculas.csv")
    print("las peliculas por actor son:",peliculas_por_actor(datos, 2010, 2020))

def test_actores_mas_frecuentes():
    datos=leer_peliculas("./data/peliculas.csv")
    print("los actores mas frecuentes son:", actores_mas_frecuentes(datos, 3, 2005, 2015))
def funcion_principal():
    #test_leer_peliculas()
    #test_peliculas_por_actor()
   # test_pelis_mas_ganancias()
    #test_media_presupuesto_por_genero()
    #test_peliculas_por_actor()
    test_actores_mas_frecuentes()      
if __name__=="__main__":
    funcion_principal()

    