class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split()
        s_reverse = s_split[::-1]

        sentence = ''
        for i in range(len(s_reverse)):
            sentence += s_reverse[i]
            sentence += ' '
        
        return sentence[:-1]
            
        