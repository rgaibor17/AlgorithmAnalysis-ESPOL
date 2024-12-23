def agrupar_por_sala(peliculas):
    """
    Agrupa las películas por su sala en un diccionario.
    
    :param peliculas: Lista de películas, cada una contiene:
                      - 'start': Hora de inicio de la película
                      - 'end': Hora de finalización de la película
                      - 'room': Número de sala
                      - Se puede incluir información adicional
    :return: Un diccionario con los números de sala como claves y listas de películas como valores
    """
    agrupadas = {}
    for pelicula in peliculas:
        sala = pelicula['room']
        if sala not in agrupadas:
            agrupadas[sala] = []
        agrupadas[sala].append(pelicula)
    return agrupadas


def maximizar_peliculas(peliculas):
    """
    Maximiza el número de películas que se pueden ver sin que hayan conflictos de tiempo.
    
    :param peliculas: Lista de peliculas, cada una contiene:
                      - 'start': Hora de inicio de la película
                      - 'end': Hora de finalización de la película
                      - 'room': Número de sala
                      - Se puede incluir información adicional
    :return: Lista de películas seleccionadas
    """
    # Paso 1: Agrupar las películas por salas
    peliculas_por_sala = agrupar_por_sala(peliculas)

    # Paso 2: Ordenar las películas dentro de cada sala por la hora de finalización
    for sala in peliculas_por_sala:
        peliculas_por_sala[sala].sort(key=lambda x: x['end'])

    # Paso 3: Usar un algoritmo voraz para encontrar la máxima cantidad de películas por sala
    peliculas_seleccionadas = []
    for sala, peliculas_sala in peliculas_por_sala.items():
        ultimo_fin = 0
        for pelicula in peliculas_sala:
            if pelicula['start'] >= ultimo_fin:
                peliculas_seleccionadas.append(pelicula)
                ultimo_fin = pelicula['end']

    # Paso 4: Devolver el horario final
    return peliculas_seleccionadas


# Ejemplo de uso
peliculas = [
    {'title': 'Película A', 'start': 1, 'end': 4, 'room': 1},
    {'title': 'Película B', 'start': 3, 'end': 5, 'room': 1},
    {'title': 'Película C', 'start': 0, 'end': 6, 'room': 1},
    {'title': 'Película D', 'start': 5, 'end': 7, 'room': 1},
    {'title': 'Película E', 'start': 1, 'end': 2, 'room': 2},
    {'title': 'Película F', 'start': 2, 'end': 4, 'room': 2},
    {'title': 'Película G', 'start': 3, 'end': 5, 'room': 2}
]

print(f"Lista de películas: ")
for pelicula in peliculas:
    print(f"Título: {pelicula['title']}, Inicio: {pelicula['start']}, Fin: {pelicula['end']}, Sala: {pelicula['room']}")

resultado = maximizar_peliculas(peliculas)

# Mostrar los resultados
print(f"\nHorario resultante: ")
for pelicula in resultado:
    print(f"Título: {pelicula['title']}, Inicio: {pelicula['start']}, Fin: {pelicula['end']}, Sala: {pelicula['room']}")
