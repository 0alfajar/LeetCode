class Solution:
    def halvesAreAlike(self, s: str) -> bool:
       vowel = "aiueoAIUEO"
       count = 0

       l, r = 0, len(s) - 1
       while l < r:
           if s[l] in vowel:
               count += 1
           if s[r] in vowel:
               count -= 1
           l += 1
           r -= 1
       return count == 0