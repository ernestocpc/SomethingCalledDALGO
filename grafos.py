from collections import deque
from typing import List


graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'F'],
  'C' : ['G'],
  'D' : [],
  'E' : [],
  'F' : ['H'],
  'G' : ['I'],
  'H' : [],
  'I' : []
}
def bfs(graph, node):
    visited =[]
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.popleft()
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return visited

def floyd_Warshall(graph):
    """
    Graph es la matriz de adyacencia
    """
    V = len(graph)
    # dist = [[0 for columnas in range(V)] for filas in range(V)]
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min (dist[i][j], dist[i][k] + dist[k][j])
    return dist

def searchBipartite(graph):

    queue = deque()
    colores = ['white'] * len(graph)
    set_R = [] #Rojo
    set_A= [] #Azul

    
    colores[0] = 'red'
    for i in range(0,len(graph)):
        #Revisar si el nodo es blanco o ya fue visitado (a.k.a tiene color)
        if graph[i] not in set_R and graph[i] not in set_A:
            set_R.append(list(graph[i])) #Si no ah sido visitado se pone en Rojo 
            queue.append(list(graph[i]))

            while queue:
                nodoOrigen = queue.popleft()

                for n in range(0,len(graph[nodoOrigen])): #Recorrer vertices vecinos
                    nodoVecino = graph[nodoOrigen][n]

                    if nodoVecino not in set_R and nodoVecino not in set_A: #El vertice todavia no tiene color

                        if nodoOrigen in set_R: #El origen es rojo, los vecinos deben ser azules
                            set_A.append(nodoVecino)

                        elif nodoOrigen in set_A: #El origen es azul y el vecino debe ser rojo
                            set_R.append(nodoVecino)

                    elif (nodoVecino and nodoOrigen) in set_R or (nodoVecino and nodoOrigen) in set_A: #Como tiene color, revisar que no sea el mismo 
                        return False
    return True          


def main():
    searchBipartite(graph)
    bfs(graph, 'A')
# main()