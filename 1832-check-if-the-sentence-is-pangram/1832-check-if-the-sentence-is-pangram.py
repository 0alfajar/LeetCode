class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter = {char for char in sentence.lower() if char.isalpha()}
        return len(letter) == 26