class Solution: # after understanding neetcode's solution

    def isAnagram(self, s: str, t: str) -> bool:
        # if the lengths are not equal, return false right away
        if len(s) != len(t):
            return False


        # create 2 dicts and store each character as the key and the occurence to be the corresponding value
        s_dict, t_dict = {}, {}
        
        for i in range(len(s)):
            # using .get prevent us from getting an error that the key doesn't exist yet in the dict. So it has a value for 0
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        # now check if the values match
        for j in s_dict:
            # if the number of occurences doesn't match for the same key, then return false
            if s_dict[j] != t_dict.get(j, 0):
                return False
        return True

# note: using .get(key, 0) is useful so I don't get errors if the key doesn't exits in the dict yet

'''
my original solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if ''.join(sorted(s)) != ''.join(sorted(t)):
            return False
        else:
            return True
        

# if we sort car and rat, we would get acr and art which isn't an anagram
# if we sort anagram and nagaram, then we get aaagmnr
# using .join takes all the element in a list and combines them in a string
# thought process: sort each string and return false if they aren't equal because that means that we found 1 case where the strings don't match when re-arranged
'''