class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        first_char = ""

        for word in words:
            first_char += word[0]
        
        return first_char == s
        