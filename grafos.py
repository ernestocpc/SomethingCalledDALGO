from collections import deque


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
    # queue = []
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.popleft()
        print(s, end = " ")

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

def BellmanFord(graph, V, E, src):
 
    # Initialize distance of all vertices as infinite.
    dis = [maxsize] * V
 
    # initialize distance of source as 0
    dis[src] = 0
 
    # Relax all edges |V| - 1 times. A simple
    # shortest path from src to any other
    # vertex can have at-most |V| - 1 edges
    for i in range(V - 1):
        for j in range(E):
            if dis[graph[j][0]] + \
                   graph[j][2] < dis[graph[j][1]]:
                dis[graph[j][1]] = dis[graph[j][0]] + \
                                       graph[j][2]
 
    # check for negative-weight cycles.
    # The above step guarantees shortest
    # distances if graph doesn't contain
    # negative weight cycle. If we get a
    # shorter path, then there is a cycle.
    for i in range(E):
        x = graph[i][0]
        y = graph[i][1]
        weight = graph[i][2]
        if dis[x] != maxsize and dis[x] + \
                        weight < dis[y]:
            print("Graph contains negative weight cycle")

def main():
    bfs(graph, 'A')
main()