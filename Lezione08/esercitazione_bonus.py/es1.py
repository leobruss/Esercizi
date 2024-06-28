#The Number of Beautiful Subsets: write a function with an array nums of positive integers and a positive integer k given as inputs. 
#A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k. Return the number of non-empty 
#beautiful subsets of the array nums. A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. 
#Two subsets are different if and only if the chosen indices to delete are different.

def beautiful_number(nums: list, k: int) ->int:
    correct_list = len(nums)
    lista_numeri_corretti = []
    for n in nums: 
        for m in nums:
            if  m - n == k or n - m == k :
                if n in nums and len(nums) > 1:
                    nums.remove(m)
                    print(nums)
                    lista_numeri_corretti.append(m)
                    #lista_numeri_corretti.append(n)
                    
                    if m in nums:
                        pass
                    else: 
                        correct_list += 1
    return correct_list


#Example 1:
print(beautiful_number([2, 4, 6 ], 2) )


#Example 2:
print(beautiful_number([1], 1))

#Example 1:
print(beautiful_number([4, 2, 5, 9, 10, 3],100 ) )


                
