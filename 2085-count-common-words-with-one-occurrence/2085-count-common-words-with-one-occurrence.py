class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        count = 0
        for word in words1:
            if words1.count(word) == 1:
                if words2.count(word) == 1:
                    count += 1
        return count