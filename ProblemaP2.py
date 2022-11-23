# María Alejandra Estrada G 202021060 
# Santiago Martínez Novoa 202112020 
# Ernesto Carlos Pérez Covo 202112530 
import sys

# palabras debe ser la lista [] con todas las palabras ordenadas por pagina 
def dfs(listaAdj, c, visitado, stack):
    visitado[c] = True
    for v in listaAdj[c]:
        if visitado[v] == False:
            dfs(listaAdj, v, visitado, stack)
    stack.insert(0,c)

def pandora(palabras) -> str :
    listaAdj = {c:[] for w in palabras for c in w} #Todas las letras en orden de aparicion 
    
    for i in range (len(palabras) -1 ): #iterar todas las palabras 
        p1 = palabras[i]
        p2 = palabras[i+1]
        for letra in range(min(len(p1),len(p2))):
            if p1[letra] != p2[letra]: #La letra de p1 va antes que la de p2
                if p2[letra] not in listaAdj[p1[letra]]:
                    listaAdj[p1[letra]].append(p2[letra])
                    break
    """
    Ya esta el caso normal
    Falta pensar excepciones
    Siguiente paso: Hacer el dfs 
    """
    
    visitado = {c:False for c in listaAdj}
    stack = []
    for c in listaAdj:
        if visitado[c] == False:
            dfs(listaAdj, c, visitado, stack)

    return "".join(stack)   




#  Main - Funciona para leer y formatear datos
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
            print(pandora(alfabeto))
            alfabeto = []

    
    
"""
4
3 3
2 m mh mmhj
0 h hjh hjmh
1 hm j jjm
1 5
0 xx xp pj jjj jjw
1 4
0 ab ac cc cb
1 8
0 ab ah an mb mm mh nan nak
"""
E1 = ['h', 'hjh', 'hjmh', 'hm', 'j', 'jjm', 'm', 'm','mmhj'] # hjm
E2 = ['xx', 'xp', 'pj', 'jjj', 'jjw'] # xpjw
E3 = ['ab', 'ac', 'cb'] # ERROR
E4 = ['ab', 'ah', 'an', 'mn', 'mk'] # abmhnk
E5 = ['wrt','wrf','er','ett','rftt'] #wertf
# pandora(E1)
# pandora(E2)
# pandora(E3)
# pandora(E4)