from typing import NamedTuple
import csv
from datetime import date, datetime
from collections import defaultdict

Pelicula = NamedTuple("Pelicula",[("fecha_estreno", date), ("titulo", str), ("director", str), ("generos", list[str]),("duracion", int),
    ("presupuesto", int), ("recaudacion", int), ("reparto", list[str])])    
def parsea_generos(generos:str)->list[str]:
    lista_generos=[]
    for r in generos:
        lista_generos=r.split(',')
    return lista_generos

def parsea_repartos(reparto:str)->list[str]:
    lista_reparto=[]
    for r in reparto:
        lista_reparto=r.split(',')
    return lista_reparto
"""
recibe una lista de tuplas de tipo `Pelicula` y una cadena de texto `genero`, con valor por defecto `None`, 
y devuelve el título y las ganancias de la película con mayores ganancias, de entre aquellas películas que tienen entre
 sus géneros el `genero` indicado. Si el parámetro `genero` es `None`, se busca la película con mayores ganancias,
 sin importar sus géneros. Las ganancias de una película se calculan como la diferencia entre la recaudación y el presupuesto.

"""
def peliculas_mas_ganancias(registros:list[Pelicula], genero:str | None)->tuple[str,int]:
    lista_ganancias=[]
    if genero!=None:
        for r in registros:
            if r.generos==genero:
                ganancias=r.recaudacion-r.presupuesto
                lista_ganancias.append((r.titulo,ganancias))
            
    else:
        for r in registros:
            ganancias=r.recaudacion-r.presupuesto
            lista_ganancias.append((r.titulo, ganancias))
    maximo= max(lista_ganancias, key=lambda x:x[1])
    return maximo
"""
`media_presupuesto_por_genero`: recibe una lista de tuplas de tipo `Pelicula` y devuelve un diccionario en el que 
las claves son los distintos géneros y los valores son la media de presupuesto de las películas de cada género.

"""
def media_presupuesto_por_genero(registros:list[Pelicula])->dict[str,float]:
    diccionario=dict()

    for r in registros:
        for genero in r.generos:
            if genero not in diccionario:
                diccionario[genero] = [0, 0]  # [suma, cantidad]
            diccionario[genero][0] += r.presupuesto
            diccionario[genero][1] += 1

    for genero in diccionario:
        diccionario[genero] = diccionario[genero][0] / diccionario[genero][1]

    return diccionario

"""
recibe una lista de tuplas de tipo `Pelicula` y dos enteros `año_inicial` y `año_final`, con valor por defecto `None`, 
y devuelve un diccionario en el que las claves son los nombres de los actores y actrices, y los valores son el número de películas, 
estrenadas entre `año_inicial` y `año_final` (ambos incluidos), en que ha participado cada actor o actriz. 
Si `año_inicial` o `año_final` son `None`, se contarán las películas sin filtrar por año inicial o final, respectivamente.

"""
def peliculas_por_actor(registros:list[Pelicula], año_inicial:int|None=None, año_final:int|None=None)->dict[str,int]:
    diccionario=defaultdict(int)
    for r in registros:
        if(año_inicial is None or r.fecha_estreno.year>=año_inicial) and (año_final is None or r.fecha_estreno.year<=año_final):
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

"""
`recaudacion_total_por_año`: recibe una lista de tuplas de tipo `Pelicula` y un conjunto de cadenas de texto `generos`, 
con valor por defecto `None`, y devuelve un diccionario en el que las claves son los años en los que se han estrenado películas,
 y los valores son la recaudación total de las películas estrenadas en cada año que son de alguno de los géneros contenidos en el 
 parámetro `generos`. Si `generos` es None, se calcularán las recaudaciones totales de todas las películas de cada año,
   independientemente de su género.
 NOTA: Puede usar operaciones entre conjuntos para ver si existe alguna coincidencia entre los géneros de cada película y 
 los géneros especificados por el parámetro.

"""     
def recaudacion_total_por_año(registros: list[Pelicula], generos: set[str] | None) -> dict[int, float]:
    diccionario=defaultdict(float)
    for r in registros:
        if generos==None:
            diccionario[r.fecha_estreno.year]+=r.recaudacion
        else:
            for genero in r.generos:
                if genero in generos:
                    diccionario[r.fecha_estreno.year]+=r.recaudacion
                    break
    return diccionario

"""
incrementos_recaudacion_por_año`: recibe una lista de tuplas de tipo `Pelicula`
 y un conjunto de cadenas de texto `generos`, con valor por defecto `None`, y devuelve una 
 lista de enteros con las diferencias de recaudación total de cada año con respecto al anterior
   registrado, de películas de alguno de los géneros indicados por el parámetro `generos`.
     Si `generos` es None, se usarán para el cálculo las recaudaciones totales de todas las películas 
     de cada año, independientemente de su género. Haga uso de la función `recaudacion_total_por_año` 
     para implementar esta función. 


"""
def incrementos_recaudacion_por_año(registros:list[Pelicula],generos:set[str]|None)->list[int]:
    diccionario_recaudacion_año=recaudacion_total_por_año(registros, generos)
    lista_incremento=[]
    for r in registros:
        if generos==None:
            lista_incremento.append(diccionario_recaudacion_año[r.fecha_estreno.year]-diccionario_recaudacion_año[r.fecha_estreno.year-1])
        else:
            for genero in r.generos:
                if genero in generos:
                    lista_incremento.append(diccionario_recaudacion_año[r.fecha_estreno.year]-diccionario_recaudacion_año[r.fecha_estreno.year-1])
                    break
    return lista_incremento

def incrementos_recaudacion2(registros:list[Pelicula],generos:set[str]|None)->list[int]:
    diccionario_recaudacion_año=recaudacion_total_por_año(registros, generos)
    lista_incremento=[]
    años_ordenados=sorted(diccionario_recaudacion_año.keys())
    for r in range(1,len(años_ordenados)):
        lista_incremento.append(diccionario_recaudacion_año[años_ordenados[r]]-diccionario_recaudacion_año[años_ordenados[r-1]])
    return lista_incremento
