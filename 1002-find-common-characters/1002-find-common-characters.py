class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        res = collections.Counter(words[0])
        for word in words:
            res &= collections.Counter(word)
        return list(res.elements())