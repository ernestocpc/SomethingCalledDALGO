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


# Function to return max of two numbers
def Max(a, b):
	
	if a > b:
		return a
	else:
		return b

# Function to return longest alternating
# subsequence length
def zzis(arr, n):

	"""las[i][0] = Length of the longest
		alternating subsequence ending at
		index i and last element is greater
		than its previous element
	las[i][1] = Length of the longest
		alternating subsequence ending
		at index i and last element is
		smaller than its previous element"""
	las = [[0 for i in range(2)]
			for j in range(n)]

	# Initialize all values from 1
	for i in range(n):
		las[i][0], las[i][1] = 1, 1

	
	# Initialize result
	res = 1

	# Compute values in bottom up manner
	for i in range(1, n):
	
		# Consider all elements as
		# previous of arr[i]
		for j in range(0, i):
	
			# If arr[i] is greater, then
			# check with las[j][1]
			if (arr[j] < arr[i] and
			las[i][0] < las[j][1] + 1):
				las[i][0] = las[j][1] + 1

			# If arr[i] is smaller, then
			# check with las[j][0]
			if(arr[j] > arr[i] and
			las[i][1] < las[j][0] + 1):
				las[i][1] = las[j][0] + 1

		# Pick maximum of both values at index i
		if (res < max(las[i][0], las[i][1])):
			res = max(las[i][0], las[i][1])

	return las

# Driver Code
arr = [ 10, 22, 9, 33, 49, 50, 31, 60 ]
n = len(arr)

print("Length of Longest alternating subsequence is" ,
	zzis(arr, n))

# This code is contributed by divyesh072019
