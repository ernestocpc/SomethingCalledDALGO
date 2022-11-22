# Maria Alejandra Estrada
# Santiago Martinez
# Ernesto Perez -202112530

# palabras debe ser la lista [] con todas las palabras ordenadas por pagina 
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
    print(listaAdj)

    pass

E1 = ['h', 'hjh', 'hjmh', 'hm', 'j', 'jjm', 'm', 'm','mmhj'] # hjm
E2 = ['xx', 'xp', 'pj', 'jjj', 'jjw'] # xpjw
E3 = ['ab', 'ac', 'cb'] # ERROR
E4 = ['ab', 'ah', 'an', 'mn', 'mk'] # abmhnk
E5 = ['wrt','wrf','er','ett','rftt'] #wertf
pandora(E1)
pandora(E2)
pandora(E3)
pandora(E4)
