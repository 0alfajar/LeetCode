class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alfabet = string.ascii_lowercase
        weight_dict = dict(zip(alfabet, weights))

        new_word = []
        sum_weight_word = 0
        for word in words:
            for c in word:
                sum_weight_word += weight_dict[c]
            sum_weight_word = sum_weight_word % 26
            new_c = alfabet[25 - sum_weight_word]
            new_word.append(new_c)
            sum_weight_word = 0
        
        return "".join(new_word)



        