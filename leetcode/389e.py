class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # If string s has length 0, then this means the difference is whatever we have in t
        if len(s) == 0:
            return t

        s_map = {}
        t_map = {}
        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)

        # since t is a larger string than t, i have to find the occurence in 2 different loops. If i did them both in 1 loop, I would get index out of range
        for j in range(len(t)):
            t_map[t[j]] = 1 + t_map.get(t[j], 0)

        for k in t_map:
            if k not in s_map or s_map[k] < t_map[k]:
                return k

# Thought Process: store the occurence of each value in each string in dicts
# then compare the values in the dicts, if a key in t has a bigger value than the same key in s, then return that key because that is the difference
# also check if the key at t doesn't exist in the s dict because if so then we found the extra letter
        