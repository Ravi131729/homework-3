class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Dictionary to store the most recent index of each character
        max_length = 0  # Maximum length of substring without repeating characters
        start = 0  # Start index of the current substring
        
        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1  # Move the start to the next position
            
            char_index[char] = end  # Update the most recent index of the character
            max_length = max(max_length, end - start + 1)  # Update the maximum length
        
        return max_length

# Test the code with the input "abcabcbb"
solution = Solution()
result = solution.lengthOfLongestSubstring("abcabcdbb")
print(result)  # Output: 3
