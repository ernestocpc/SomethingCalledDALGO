#Integrantes: 

#Maria Alejandra Estrada Garcia 202021060
#Ernesto Carlos Pérez Covo 202112530 
#Santiago Martínez Novoa 202112020 

import sys

def alienOrder(words):
    
    # Creacion del grafo con nodos unicos
    grafo={}
    for palabra in words:
        for nodo in palabra:
            grafo[nodo]=[]
    
  
    # Se buscan los nodos y se agregan en el grafo
    for indice in range(0,len(words)-1) :
        pPalabra=words[indice]
        sPalabara=words[indice+1]
        #print('FS',primeraPalabra, segundaPalabara)

        h=0
        while len(pPalabra)>h and h<(len(sPalabara)):
           # print(primeraPalabra[h],segundaPalabara[h])
            if pPalabra[h] != sPalabara[h]: 
                grafo[sPalabara[h]].append(pPalabra[h])
             
                break
            else: 
                if len(pPalabra) < len(pPalabra): 
                        return "ERROR"
            h+=1
        

    # Segundo recorrido para agregar los nodos, DFS. 
    visited = {} 
    res = []
    def dfs(nodo): 
    
        if nodo in visited:
            return visited[nodo] 
        visited[nodo] = False 
        for snodo in grafo[nodo]:
            result = dfs(snodo)
            if not result: 
                return False 
        visited[nodo] = True 
        res.append(nodo)
        return True

    newListi = []

    for nodo in grafo:
        newListi.append(dfs(nodo))
  
    if not all(newListi):
        return "ERROR"

    return "".join(res)

numero_casos = int(sys.stdin.readline())
for __ in range(numero_casos):
    case_list = list(map(str, sys.stdin.readline().split()))
    diccionario = {}
    alfabeto = []
    numeroPag = int(case_list[0])
    for i in range(int(case_list[0])):
        pagina = list(map(str, sys.stdin.readline().split()))

        diccionario[int(pagina[0])] = pagina[1:]
        numeroPag -=1

        if numeroPag == 0:
            for p in range(len(diccionario)):
                alfabeto.extend(diccionario[p])
            print(alienOrder(alfabeto))
            alfabeto = []