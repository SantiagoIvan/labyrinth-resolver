my_map_2d = [
    ["W", "L", "W", "W", "L", "W", "W", "W"],
    ["W", "L", "L", "L", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "L", "S"],
    ["L", "L", "W", "W", "L", "W", "L", "W"],
    ["W", "L", "W", "W", "L", "W", "L", "W"],
    ["L", "L", "L", "L", "L", "L", "L", "W"],
    ["W", "L", "W", "L", "W", "L", "W", "W"],
    ["W", "W", "W", "W", "W", "W", "L", "W"],
]
# ----ENUNCIADO----
# Mapa: matriz m*n
# Voy a hacerlo con 2 tipos de mapas: uno donde pueda tener una sola entrada y una salida
# y otro donde tenga varias entradas y varias salidas

# La entrada es cualquier L en la periferia
# La salida es una S
# Las W representan Walls, paredes
# Las L representan tierra libre

# -----------------

# En este caso me conviene aplicar depthfirst, ya que me va a convenir tomar un camino e ir hasta el fondo
# para encontrar la salida mas rapido. Si aplicase breadthfirst, haria un pasito por cada alternativa posible,
# y tardaria mas. Pero si hubiera varias salidas posibles, breadthfirst retornaria el mas corto, depthfirst no te asegura eso
# Como solo hay 1 salida, aplique depthfirst


# Cuando encuentre la salida, solo en ese caso voy a retornar un array con elementos, en los demas
# retornare None. Por lo tanto, cuando suceda eso, burbujeare el resultado a las funciones
# de arriba en la recursion, si el valor que reciben es algo distinto de None, se une su
# coordenada actual con el vector recibido. Asi se forma el camino encontrado
def depthfirst(map_2d, coords, visits):
    (row, column) = coords

    row_is_correct = row >= 0 and row < len(map_2d)
    column_is_correct = column >= 0 and column < len(map_2d[0])

    if (
        (not row_is_correct)
        or (not column_is_correct)
        or (map_2d[row][column] == "W")
        or (coords in visits)
    ):
        return

    visits.append(coords)
    if map_2d[row][column] == "S":
        return [coords]

    path = depthfirst(map_2d, (row - 1, column), visits)
    if path:
        return path + [coords]
    path = depthfirst(map_2d, (row, column - 1), visits)
    if path:
        return path + [coords]
    path = depthfirst(map_2d, (row + 1, column), visits)
    if path:
        return path + [coords]
    path = depthfirst(map_2d, (row, column + 1), visits)
    if path:
        return path + [coords]
    return


# Dando un punto de entrada
def labyrinth_resolver(map_2d, start):

    path = depthfirst(map_2d, start, [])
    path and path.reverse()
    return path


# Sin dar puntos de entrada, retorna todos los caminos desde distintos puntos de entrada
def labyrinth_resolver_v2(map_2d):
    # Primero busco entradas
    entrances = set([])
    pathsFound = []

    # reviso la periferia. Como puede no ser una matriz cuadrada, lo hago de esta forma.
    max_col = len(map_2d[0])
    max_row = len(map_2d)
    for i in range(max_row):
        if map_2d[i][0] == "L":
            entrances.add((i, 0))
        if map_2d[i][max_col - 1] == "L":
            entrances.add((i, max_col - 1))
    for i in range(max_col):
        if map_2d[0][i] == "L":
            entrances.add((0, i))
        if map_2d[max_row - 1][i] == "L":
            entrances.add((max_row - 1, i))

    for entrance in entrances:
        path = depthfirst(map_2d, entrance, [])
        path and path.reverse()
        path and pathsFound.append(path)

    return pathsFound


def shortest_labyrinth_path(paths):
    print("Caminos encontrados: ", len(paths))
    min = []
    for path in paths:
        print(path)
        if not min or len(min) > len(path):
            min = path
    # de todos los caminos, retorna el mas corto desde todas las entradas, retorna el mas corto
    return min


entrada = (3, 0)
print("Ingresando punto de entrada ", entrada)
print(labyrinth_resolver(my_map_2d, entrada))
print(" --- \n")

print("Buscando todos los puntos de entrada posibles...")
paths = labyrinth_resolver_v2(my_map_2d)
print("The shortest path is", shortest_labyrinth_path(paths))
