from typing import NamedTuple
import csv
from collections import defaultdict
from datetime import datetime, date
from peliculas import Pelicula
def leer_peliculas(registros:str)->list[Pelicula]:
    lista=[]
    with open(registros, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        for fecha_estreno,titulo,director,generos,duracion,presupuesto,recaudacion,reparto in lector:
            fecha_estreno=datetime.strptime(fecha_estreno, "%d/%m/%Y").date()
            generos=generos.split(',')
            for cadena in generos:
                cadena.strip()
            duracion=int(duracion)
            presupuesto=int(presupuesto)
            recaudacion=int(recaudacion)
            reparto=reparto.split(',')
            reparto=[r.strip() for r in reparto]
            r=Pelicula(fecha_estreno, titulo,director,generos,duracion,presupuesto,recaudacion,reparto)
            lista.append(r)
    return lista


"""
recibe una lista de tuplas de tipo `Pelicula` y una cadena de texto `genero`, con valor por defecto `None`, 
y devuelve el título y las ganancias de la película con mayores ganancias, de entre aquellas películas que tienen entre
 sus géneros el `genero` indicado. Si el parámetro `genero` es `None`, se busca la película con mayores ganancias,
 sin importar sus géneros. Las ganancias de una película se calculan como la diferencia entre la recaudación y el presupuesto.



"""
def peliculas_mas_ganancias(registros:list[Pelicula], genero:str|None)->tuple[str,int]:
    lista_ganancias=[]
    for r in registros:
        if genero ==None:
            lista_ganancias.append((r.titulo, r.recaudacion - r.presupuesto))
        else:
            if r.generos == genero:
                lista_ganancias.append((r.titulo, r.recaudacion - r.presupuesto))
    return max(lista_ganancias, key=lambda x: x[1])






"""
media_presupuesto_por_genero`: recibe una lista de tuplas de tipo `Pelicula` y devuelve un diccionario
 en el que las claves son los distintos géneros y los valores son la media de presupuesto de las 
 películas de cada género.


"""
def media_presupuesto_genero(registros:list[Pelicula])->dict[str,float]:
    diccionario=dict()
    for r  in registros:
        for genero in r.generos:
            if genero not in diccionario:
                diccionario[genero]=[0,0]
            diccionario[genero][0] += r.presupuesto
            diccionario[genero][1] += 1
    for  genero in diccionario:
        diccionario[genero]=diccionario[genero][0] / diccionario[genero][1]

    return diccionario

"""
recibe una lista de tuplas de tipo `Pelicula` y dos enteros `año_inicial` y `año_final`, con valor 
por defecto `None`, y devuelve un diccionario en el que las claves son los nombres de los actores y 
actrices, y los valores son el número de películas, estrenadas entre `año_inicial` y `año_final`
 (ambos incluidos), en que ha participado cada actor o actriz. Si `año_inicial` o `año_final` 
 son `None`, se contarán las películas sin filtrar por año inicial o final, respectivamente.

"""
def peliculas_por_actor(registros:list[Pelicula],año_incial:int|None, año_final:int|None)->dict[str,int]:
    diccionario=dict()
    for r in registros:
        if año_incial==None or r.fecha_estreno.year>=año_incial and (año_final==None or r.fecha_estreno.year<=año_final):
            for actor in r.reparto:
                if actor not in diccionario:
                    diccionario[actor]=1
                else:
                    diccionario[actor]+=1
    return diccionario

"""
recibe una lista de tuplas de tipo `Pelicula`, un entero `n` y dos enteros `año_inicial` y `año_final`, con valor por defecto 
`None`, y devuelve una lista con los `n` actores o actrices que han participado en más películas estrenadas entre `año_inicial` y 
`año_final` (ambos incluidos). La lista de actores o actrices debe estar ordenada alfabéticamente. Si `año_inicial` o `año_final` son `None`, 
se contarán las películas sin filtrar por año inicial o final, respectivamente.
 Haga uso de la función `peliculas_por_actor` para implementar esta función.

"""
def actores_mas_frecuentes(registros:list[Pelicula], n:int, año_inicial:int|None, año_final:int|None)->list[str]:
    diccionario_peliculas=peliculas_por_actor(registros, año_inicial,año_final)
    lista_ordenada=sorted(diccionario_peliculas.items(), key=lambda x:x[1], reverse=True)[:n]
    lista_actores=[actor[0] for actor in lista_ordenada]
    return lista_actores
        
