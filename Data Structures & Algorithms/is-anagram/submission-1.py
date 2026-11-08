class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}
        for token in s:
            if token in s_dict:
                s_dict[token] += 1
            else:
                s_dict[token] = 1
        
        for token in t:
            if token in t_dict:
                t_dict[token] += 1
            else:
                t_dict[token] = 1

        return s_dict == t_dict    