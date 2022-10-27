# Subsecuencia alternante

# Subsecuencia bitonica
def LIS(arr):
    l= len(arr)
    solution = [1] * l
    for i in range (1,l):
        for j in range(0,i):
            if arr[j] < arr[i]:
                solution[i] = max (solution[i], solution[j]+1)
    return solution
def LDS(arr):
    l= len(arr)
    solution = [1] * l
    for i in range (1,l):
        for j in range(0,i):
            if arr[j] > arr[i]:
                solution[i] = max (solution[i], solution[j]+1)
    return solution
def BitonicSubsecuence(arr):
    increasing  = LIS(arr)
    decreasing = LDS(arr[::-1])
    sublist= [1] * len(arr)
    for i in range(len(arr)):
        sublist[i] = increasing[i] + decreasing[i] -1         
    # Para sacar la subsecuencia con mayo incremento toca coger el array y cada vez que incremente se coge la letra
    # de esa posicion hasta que se llegue al maximo (que ya se deberia conocer.)
    # Para la de menor incremento se coje desde e
    print (arr, arr[::-1])
    print(increasing,decreasing)

print(BitonicSubsecuence([2,-1,4,3,5,-1,3,2])) #2,3,5,3,2 = 5 
# Subsecuencia palindromica
def subsecuenciaPalindromica(string):
    l= len(string)
    matrix = [[0 for columna in range(l)] for fila in range(l)]

    
    pass
# print(subsecuenciaPalindromica("Hola"))