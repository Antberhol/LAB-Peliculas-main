from peliculas import *
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
            for espacio in reparto:
                espacio.strip()
            r=Pelicula(fecha_estreno, titulo,director,generos,duracion,presupuesto,recaudacion,reparto)
            lista.append(r)
    return lista

def test_leer_peliculas():
    datos=leer_peliculas("./data/peliculas.csv")
    print("el primer registro es:", datos[0])

def test_peliculas_por_actor():
    datos=leer_peliculas("./data/peliculas.csv")
    print("las peliculas por actor son:",peliculas_por_actor(datos, 2010, 2020))

def test_media_presupuesto():
    datos=leer_peliculas("./data/peliculas.csv")
    print("la media de preseupuesto es:",media_presupuesto_por_genero(datos))

def actores_mas_frecuentes_test():
    datos=leer_peliculas("./data/peliculas.csv")
    print("los actores mas frecuentes son:", actores_mas_frecuentes(datos, 3, 2005, 2015))

def test_incremento_recaudacion():
    datos=leer_peliculas("./data/peliculas.csv")
    print("el incremento de recaudacion es:", incrementos_recaudacion2(datos,{"Drama", "Acción"}))


def test_recaudacion_por_año():
    datos=leer_peliculas("./data/peliculas.csv")
    print("la recaudacion por año es:",recaudacion_total_por_año(datos, {"Drama", "Acción"}))
def funcion_principal():
    #test_leer_peliculas()
    test_media_presupuesto()
    #test_peliculas_por_actor()
    #actores_mas_frecuentes_test()
    #test_recaudacion_por_año()
    #test_incremento_recaudacion()
if __name__=="__main__":
    funcion_principal()