# Realizado por: Ernesto Perez - 202112530 y Juan Daniel Sepulveda
def nLIS(nums):
    """
    Given an integer array, return the number of longest increasing subsequences
    Arguments:
        nums: array of Int numbers
    Returns:
        The number of longest increasing subsequences
    Complejidad de la funcion:
        O(n^2) - Se itera sobre el array de numeros n*n veces primero con el indice i y este itera n veces el indice j
        asi que seria n^2.
    """
    l=len(nums)
    solution_Base = [1]*l
    new_longest,longest,max_sub=1,1,1
    for i in range(1,l): #Va de 1 a 6
        if longest !=new_longest:
            max_sub=1
        longest = max(solution_Base)
        for j in range(0,i):
            if nums[i] > nums[j]: #10>4
                if solution_Base[j] +1> solution_Base[i]: #2+1 > 3
                    solution_Base[i] = solution_Base[j] + 1
                elif solution_Base[j] + 1 == solution_Base[i]:
                    max_sub+=1
        new_longest=max(solution_Base)
    return max_sub 
# print(nLIS([3,10,1,2,20,19,30,50]))

def LIS(nums):
    l=len(nums)
    solution_Base = [1]*l
    for i in range(1,l): #Va de 1 a 6
        for j in range(0,i):
            if nums[i] > nums[j]: #10>4
                if solution_Base[j] +1> solution_Base[i]: #2+1 > 3
                    solution_Base[i] = solution_Base[j] + 1
    return solution_Base

def LDS(nums):
    l=len(nums)
    solution_Base = [1]*l
    for i in range(1,l): #Va de 1 a 6
        for j in range(0,i):
            if nums[i] < nums[j]: #10>4
                if solution_Base[j] +1> solution_Base[i]: #2+1 > 3
                    solution_Base[i] = solution_Base[j] + 1
    return solution_Base


def LBS_usingLIS_LDS(nums):
    """
    Given an integer array, return the len of the longest bitonic subsequence 
    This implementation must use LIS and LDS (longest decreasing subsequence).
    Arguments:
        nums: array of Int numbers
    Returns:
        The len of the longest bitonic subsequence
    Complejidad de la funcion:
        O(n^2) - La maxima complejidad es la de LIS pues es un array que se itera n*n veces es decir n^2 junto con la complejidad
            de LDS que tambien es n^2, seria 2n^2 asi que en el peor de los casos y quitando la constante queda O(n^2)
    """
    # Sumar los dos arreglos en la misma posicion y retornar el maximo
    inc_array = LIS(nums)
    dec_array= LDS(nums)
    sublist= [1] * len(nums)
    for i in range(len(nums)):
        sublist[i] = inc_array[i] + dec_array[i] -1 
    print (nums, nums[::-1])
    print(inc_array,dec_array)
    return max(sublist)

print('here')
print(LBS_usingLIS_LDS([2,-1,4,3,5,-1,3,2])) #2,3,5,3,2 = 5 

def LBS_usingLIS(nums):
    """
    Given an integer array, return the len of the longest bitonic subsequence 
    This implementation should use only the LIS function.
    Arguments:
        nums: array of Int numbers
    Returns:
        The len of the longest bitonic subsequence
    Complejidad de la funcion:
        O(n^2) - La maxima complejidad es la de LIS pues es un array que se itera n*n veces es decir n^2.
    """
    inc = LIS(nums)
    initialMax = max (inc) 
    maxInc = max(inc)
    extras = 0
    for i in range(len(inc)):
        if inc[i] == initialMax and i==len(inc)-1:
            return maxInc
        elif inc[i] == initialMax and inc[i+1] == initialMax:
            extras+= 1
        elif inc[i] == initialMax and inc[i+1] == initialMax-1:
            maxInc += inc[i+1]
            maxInc += extras
            return maxInc 
        elif inc[i] == initialMax and inc[i+1] != initialMax:
            return maxInc


def MSIS(array):
    """
    Given an integer array, suppose that S is an increasing subsequence with 
    max sum, this function returns the int value of that sum.    
    Arguments:
        nums: array of Int numbers
    Returns:
        The sum of the increasing subsequence with max sum
    Complejidad de la funcion:
        O(n^2) - El primer ciclo con indice i itera una unica vez sobre el array pero tiene un ciclo anidado con indice j 
                que recorre el array n veces asi que queda n(n) = n^2.
    """
    l = len(array)
    table = array.copy()
    for i in range (1,l):
        for j in range (0,i):
            suma = table[j] + array[i]
            if array[i] > array[j]:
                if suma > table[i]:
                    table[i] = suma
    return max(table)