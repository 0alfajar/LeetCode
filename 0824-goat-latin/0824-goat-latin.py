class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        goat_latin = []
        for i in range(len(sentence)):
            if sentence[i][0].lower() in "aiueo":
                goat_word = sentence[i] + "ma" + "a"*(i+1)
                goat_latin.append(goat_word)
            else:
                goat_word = sentence[i][1:len(sentence[i])] + sentence[i][0] + "ma" + "a"*(i+1)
                goat_latin.append(goat_word)
            
        res = ""
        for i in range(len(goat_latin)):
            if i > 0:
                res += " " + goat_latin[i]
            else:
                res = goat_latin[i]
        
        return res
