class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        return count_s == count_t
s1 = "anagram"
t1 = "nagaram"
solution = Solution()
print(solution.isAnagram(s1, t1))  

s2 = "rat"
t2 = "car"
solution = Solution()
print(solution.isAnagram(s2, t2))  
