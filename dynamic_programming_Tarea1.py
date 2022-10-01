#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Realizado por: Ernesto Perez - 202112530
def maximum_sum_increasing_subsequenc(array):
    """
    Fing a subsequence of a given sequence such that the subsequence sum is as
    high as possible and the subsequence's elements are sorted in ascending order
    Arguments:
        array: array of Int numbers
    Returns:
        The sum of the maxmum increasing subsequence of array (Int)
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

def longest_palindromic_subsequence(s):
    """
    Find the length of the longest palindromic subsequence in the string s 
    Arguments:
        s: a String
    Returns:
        The length of the longest palindromic subsequence in s (Int)
    Complejidad de la funcion:
        O(n^2) - Primero se crea una matriz n*n 'matrix', se recorre a esta con un ciclo anidado por lo que la complejidad esta 
            altura*ancho de la matriz (n*n).
            Seguidamente se vuelve a hacer un recorrido similar pero con un rango mas pequeño y recorriendo sobre las diagonales
            por lo que el primer ciclo es el de mayor complejidad (n^2) 
            Al final simplemente se saca el valor de la primera fila- ultima columna que seria O(1)
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
                matrix[i][j] = 2 + matrix[i+1][j-1] #2 + caso long-1 (anterior)
            else:
                matrix[i][j] = max(matrix[i][j-1],matrix[i+1][j])
    return matrix[0][l-1]


def longest_common_substring(s,t):
    """
    Function to find the longest common substring of strings: s,t
    Arguments:
        s: a String
        t: a String
    Returns:
        The longest common substring of s and t (String)
    Complejidad de la funcion:
        O(m*n) - Donde m y n son las longitudes de las cadenas de caracteres. 
            Esto pues se crea una matriz de tamaño m+1, n+1 y se itera sobre esta con dos for's anidados.
            En esta iteracion unicamente se hacen comparaciones y modificaciones a la matriz pero todo de complejidad O(1)
            Finalmente cuando ya estan todas las modificaciones a la matriz se recuperan los indices del string mas largo que tampoco supera la complejidad de la iteracio
            sobre la matriz n*m
    """
    l_s= len(s)
    l_t = len(t)
    # Crear la matriz filas son las letras de t +1; columnas son las letras de s +1
    matrix = [[0 for x in range(l_s+1)] for y in range(l_t+1)]
    substring_length = 0
    substring=''
    # Iterar pero dejando primera columna y fila en 0
    for i in range(1,len(matrix)):
        for j in (range(1,len(matrix[0]))):   
            if t[i-1] == s[j-1]: #El -1 es para que no se salga de los indices de las palabras
                matrix[i][j] = 1 + matrix[i-1][j-1] #Si son iguales es la diagonal anterior +1 
                if matrix[i][j] > substring_length:
                    substring_length = matrix[i][j]

    for i in range(substring_length,0,-1):
        substring += t[i]
    return substring[::-1]