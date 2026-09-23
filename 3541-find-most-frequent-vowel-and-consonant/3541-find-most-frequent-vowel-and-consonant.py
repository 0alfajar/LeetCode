class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = 0
        consonant = 0

        for c in s:
            if c in "aiueo":
                vowel = max(vowel, s.count(c))
            else:
                consonant = max(consonant, s.count(c))
        
        return vowel + consonant
        