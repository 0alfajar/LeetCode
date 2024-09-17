class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s = {}
        for c in s:
            if c in dict_s:
                dict_s[c] += 1
            else:
                dict_s[c] = 1

        dict(sorted(dict_s.items(), key=lambda item: item[1]))
        first_el = list(dict_s.keys())[0]

        if dict_s[first_el] > 1:
            return -1
        else:
            return s.index(first_el)
