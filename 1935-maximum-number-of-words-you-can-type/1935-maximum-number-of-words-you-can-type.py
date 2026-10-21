class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        count = 0
        for i in text:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                count += 1
        return count