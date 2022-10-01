def nLIS(nums):
    """
    Given an integer array, return the number of longest increasing subsequences
    Arguments:
        nums: array of Int numbers
    Returns:
        The number of longest increasing subsequences

    """
    l=len(nums)
    solution_Base = [1]*l
    max_sub= 1
    for i in range(1,l): #Va de 1 a 6
        for j in range(0,i):
            if nums[i] > nums[j]: #10>4
                if solution_Base[j] +1> solution_Base[i]: #2+1 > 3
                    solution_Base[i] = solution_Base[j] + 1
                elif solution_Base[j] +1 == solution_Base[i]:
                    max_sub +=1
    print(solution_Base)
    return max_sub
p1=[0,7,1,2,1,-1]
# print (nLIS(p1))

def LIS(nums):
    l=len(nums)
    solution_Base = [1]*l
    for i in range(1,l): #Va de 1 a 6
        for j in range(0,i):
            if nums[i] > nums[j]: #10>4
                if solution_Base[j] +1> solution_Base[i]: #2+1 > 3
                    solution_Base[i] = solution_Base[j] + 1
    return solution_Base
print (LIS(p1))

def LDS(nums):
    l=len(nums)
    solution_Base = [1]*l
    for i in range(1,l): #Va de 1 a 6
        for j in range(0,i):
            if nums[i] < nums[j]: #10>4
                if solution_Base[j] +1> solution_Base[i]: #2+1 > 3
                    solution_Base[i] = solution_Base[j] + 1
    return solution_Base
print(LDS(p1))

def LBS_usingLIS_LDS(nums):
    """
    Given an integer array, return the len of the longest bitonic subsequence 
    This implementation must use LIS and LDS (longest decreasing subsequence).
    Arguments:
        nums: array of Int numbers
    Returns:
        The len of the longest bitonic subsequence
    """
    # Sumar los dos arreglos en la misma posicion y retornar el maximo
    pass
p2=[1,3,2,5,7,7,7,7,7,7]
# print(LBS_usingLIS_LDS(p2))

def LBS_usingLIS(nums):
    """
    Given an integer array, return the len of the longest bitonic subsequence 
    This implementation should use only the LIS function.
    Arguments:
        nums: array of Int numbers
    Returns:
        The len of the longest bitonic subsequence
    """
    inc = LIS(nums)
    print(inc)
    initialMax = max (inc)
    maxInc = max(inc)
    for i in range(len(inc)):
        if inc[i] == initialMax and i==len(inc)-1:
            return maxInc
        elif inc[i] == initialMax and inc[i+1] == initialMax:
            maxInc = maxInc + 1
        elif inc[i] == initialMax and inc[i+1] != initialMax:
            maxInc += inc[i+1]
            return maxInc 
p3 = [1,2,10,5,3,10,5,4,3,2,1] # 9
# print(LBS_usingLIS(p3))
def MSIS(nums):
    """
    Given an integer array, suppose that S is an increasing subsequence with 
    max sum, this function returns the int value of that sum.    
    Arguments:
        nums: array of Int numbers
    Returns:
        The sum of the increasing subsequence with max sum
    """
