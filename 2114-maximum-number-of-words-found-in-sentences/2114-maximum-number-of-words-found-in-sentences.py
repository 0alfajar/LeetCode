class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        total_words = []
        for sentence in sentences:
            s = sentence.split()
            total_words.append(len(s))
        
        return max(total_words)
