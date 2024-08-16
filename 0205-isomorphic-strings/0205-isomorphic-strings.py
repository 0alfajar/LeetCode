class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}

        for i in s:
            if i in s_freq:
                s_freq[i] += 1
            else:
                s_freq[i] = 1
        
        for i in t:
            if i in t_freq:
                t_freq[i] += 1
            else:
                t_freq[i] = 1

        if list(s_freq.values()) == list(t_freq.values()):
            return True
        else:
            return False