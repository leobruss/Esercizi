#1. Two Sum

#Given a list of integers and a target sum, find all unique pairs of integers within the list that sum up to the target.
def find_pairs_with_sum(number, target):
    pairs = set()
    seen = set()

    for n in number:
        complement = target - n
        if complement in seen:
            pair = (min(n, complement), max(n, complement))
            pairs.add(pair)
        seen.add(n)

    return pairs


number = [1, 2, 3, 4, 5, 6]
target = 7
result = find_pairs_with_sum(number, target)
print("Pairs with sum", target, ":", result)


print("\n")



#2. Longest Increasing Subsequence

#Given a list of integers, find the length of the longest increasing 
#subsequence within the list. An increasing subsequence is a sequence of elements from the array where each element is greater than or equal to the previous element.
def length_of_lis(nums):
    if not nums:
        return 0

    # Initialize a dp array to store the length of the longest increasing subsequence ending at each index
    dp = [1] * len(nums)

    # Iterate through the list
    for i in range(1, len(nums)):
        # For each element, check all previous elements
        for j in range(i):
            # If the current element is greater than the previous element,
            # update the length of LIS ending at the current index
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array
    return max(dp)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of longest increasing subsequence:", length_of_lis(nums))

print("\n")

#3. Longest Common Subsequence

#Given two strings, find the length of the longest common subsequence (LCS) between them. An LCS is a subsequence of one string that is also a subsequence of 
#the other string while maintaining the relative order of elements.
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    
    # Initialize a table to store lengths of LCS for subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of LCS will be at dp[m][n]
    return dp[m][n]

# Example usage
text1 = "abcde"
text2 = "ace"
print("Length of Longest Common Subsequence:", longest_common_subsequence(text1, text2))

print("\n")
#4. Word Break Problem: 

#Given a string and a dictionary of words, determine whether the string can be segmented into a space-separated sequence of one or more dictionary words. 
#Each word in the dictionary must be a contiguous substring of the input string.
def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

# Example usage
s = "leetcode"
word_dict = {"leet", "code"}
print("String can be segmented:", word_break(s, word_dict))

print("\n")
#5. Longest Palindrome Subsequence:
def longest_palindrome_subsequence(s):
    n = len(s)
    
    # Initialize a 2D array to store the lengths of LPS for subproblems
    dp = [[0] * n for _ in range(n)]

    # Base case: LPS length is 1 for single characters
    for i in range(n):
        dp[i][i] = 1

    # Fill the dp table in a bottom-up manner
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of LPS will be at dp[0][n-1]
    return dp[0][n - 1]

# Example usage
s = "bbbab"
print("Length of Longest Palindrome Subsequence:", longest_palindrome_subsequence(s))

#A palindrome is a word, phrase, or sequence that reads the same backwards as forward. Given a string, the task is to find the longest palindrome subsequence within the string. A subsequence is obtained from a string by deleting zero or more elements without changing the order of the remaining elements.

#6. Armstrong Number Checker:

#Develop a function to check if a given number is an Armstrong number (the sum of its digits raised to the power of the number of digits equals the number itself).

#7. Merge Two Sorted Lists: 

#Implement a function to merge two sorted lists into a single sorted list.

#8. Find the Most Frequent Element:

#Create a function that finds the element that appears most frequently in a given list.

#9. Find the Second Largest Element in an Array:

#Implement a function to find the second largest element in an unsorted list without using sorting algorithms.

#10. Find the Intersection of Two Sorted Arrays:

#Implement a function to find the elements that are present in both of the two sorted lists.