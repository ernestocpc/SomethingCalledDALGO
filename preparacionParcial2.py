# Subsecuencia alternante =======================================================
from operator import sub


def subsecuenciaAlternante(nums):
    l = len(nums)
    matrix = [[0 for columna in range(l)] for fila in range(l)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 1
            elif i>j:#abajo izquierda
                if nums[j] < nums[j-1]:
                    matrix[i][j] = matrix[i-1][j] + 1
                else:
                    matrix[i][j] = matrix[i-1][j]
            elif i<j: #arriba derecha
                if nums[j] > nums[j-1]:
                    matrix[i][j] = matrix[i][j-1] + 1
                else:
                    matrix[i][j] = matrix[i][j-1]

    for i in matrix:
        print(i)

# Subsecuencia bitonica =======================================================
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

# print(BitonicSubsecuence([2,-1,4,3,5,-1,3,2])) #2,3,5,3,2 = 5 


# Subsecuencia palindromica =======================================================
def subsecuenciaPalindromica(s):
    l= len(s)
    matrix = [[0 for columna in range(l)] for fila in range(l)]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i==j:
                matrix[i][j] = s[i]


    for long in range(2,l+1): #Se comienza con long = 2 y se va incrementando hasta la longitud de el String. long es el tamaño de los caracteres que comparamos 
        for i in range (0,l-long+1):
            j= i + long -1      # Asi recorremos matriz por sus diagonales (hacia la derecha)
            if long==2 and s[i] == s[j]: #Caso especial para la primera diagonal 
                matrix[i][j] = s[i]*2
            # elif s[i] == s[j]:
            #     matrix[i][j] = 2 + matrix[i+1][j-1] #2 + caso long-1 (anterior)
            # else:
            #     matrix[i][j] = max(len(matrix[i][j-1]),len(matrix[i+1][j]))
    # return matrix[0][l-1]
    for i in matrix:
        print(i)
    
    pass
s="agbdba"
arr=[7,10,6,4,5,7,0,2,5]
# print(subsecuenciaPalindromica(s))
# print(s[0:6])
print(subsecuenciaAlternante(arr))