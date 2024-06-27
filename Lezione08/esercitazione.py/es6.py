def longest_palindrome(s: str) -> int:
    from collections import Counter
    
    # Count the frequency of each character in the string
    char_count = Counter(s)
    
    length = 0
    odd_found = False
    
    # Iterate through the frequency count
    for count in char_count.values():
        if count % 2 == 0:
            # If the count is even, it can fully contribute to the palindrome
            length += count
        else:
            # If the count is odd, one less can contribute as pairs and we can potentially use one character as center
            length += count - 1
            odd_found = True
    
    # If there was any character with an odd count, we can place one in the center
    if odd_found:
        length += 1
    
    return length

print(longest_palindrome("abccccdd"))

print(longest_palindrome("a"))

print(longest_palindrome("Aa"))

print(longest_palindrome("abccccba"))

print(longest_palindrome("abcabcabc"))