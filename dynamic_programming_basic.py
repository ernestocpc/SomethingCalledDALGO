#!/usr/bin/env python
# -*- coding: utf-8 -*-


p1= [3,4,-1,0,6,2,3]
def maximum_sum_increasing_subsequenc(array):
    """
    Fing a subsequence of a given sequence such that the subsequence sum is as
    high as possible and the subsequence's elements are sorted in ascending order
    Arguments:
        array: array of Int numbers
    Returns:
        The sum of the maxmum increasing subsequence of array (Int)
    Complejidad de la funcion:
        O(n^2) - Se esta iterando sobre el array de entrada con dos indices lo qu evuelve la complejidad n^2.
    """    
    l = len(array)
    table = [1] * l

    for i in range (1,l):
        for j in range (0,l):
            if array[i] > array[j]: # Si el de mas adelante es mayor
                if table[j] + 1> table[i]:# Revisar que en la tabla no exusta ya una subsecuencia mayor hasta i
                    table[i] = table[j] + 1
    
    max_subsecuencia = 0
    for n in table:
        if n > max_subsecuencia:
            max_subsecuencia = n
    return max_subsecuencia
# print(maximum_sum_increasing_subsequenc(p1))    

p2="AGBDBA"
def longest_palindromic_subsequence(s):
    """
    Find the length of the longest palindromic subsequence in the string s 
    Arguments:
        s: a String
    Returns:
        The length of the longest palindromic subsequence in s (Int)
    """
    
    l= len(s)
    matrix = [[0 for x in range(l)] for y in range(l)]
    # Reemplazar diagonal por 1, porque el minimo palindromo es de longitud 1 cuando es la letra consigo misma.
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i==j:
                matrix[i][j] = 1
    

    for long in range(2,l+1): #Se comienza con long = 2 y se va incrementando hasta la longitud de el String 
        for i in range (0,l-long+1):
            j= i + long -1      # Asi recorremos matriz por sus diagonales (hacia la derecha)
            if long==2 and s[i] == s[j]: #Caso especial
                matrix[i][j] = 2
            elif s[i] == s[j]:
                matrix[i][j] = 2 + max(matrix[i][j-1],matrix[i+1][j]) #2 + caso long-1 (anterior)
            else:
                matrix[i][j] = max(matrix[i][j-1],matrix[i+1][j])
    return matrix[0][l-1]
    
    # pass
print (longest_palindromic_subsequence(p2))

def longest_common_substring(s,t):
    """
    Function to find the longest common substring of strings: s,t
    Arguments:
        s: a String
        t: a String
    Returns:
        The longest common substring of s and t (String)
    """
    pass

