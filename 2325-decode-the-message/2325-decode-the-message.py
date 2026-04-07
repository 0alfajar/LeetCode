import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dict = {}
        alfabet = list(string.ascii_lowercase)

        idx = 0
        for c in key:
            if c != ' ' and c not in key_dict:
                key_dict[c] = alfabet[idx]
                idx += 1

        key_dict[' '] = ' '
        
        decode = [key_dict.get(k) for k in message]
        return "".join(decode)