class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        length = len(word)
        idx = word.find(ch)

        if idx == -1:
            return word
        
        return word[idx::-1] + word[idx+1:]
