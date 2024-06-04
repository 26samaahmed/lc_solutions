class Solution: # after understanding neetcode's explanation, my solutions were overcomplicating the question
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
                j += 1
            elif s[i] != t[j]:
                i += 1
        # subtract length of t from the last matching index we found
        return len(t) - j

# My first solution: passed 61 cases out of the 85
# class Solution:
#     def appendCharacters(self, s: str, t: str) -> int:
#         # if t has only 1 letter and that letter is already in s then return 0
#         if len(t) == 1 and t in s:
#             return 0

#         # if s has only 1 letter and that letter is not in t, then append t to s. Subtract 1 from the length so we don't count the letter in s
#         if len(s) == 1 and s not in t:
#             s += t
#             return len(s) - 1

#         i = 0
#         j = 0

#         og = len(s)
#         while i < len(t):
#             if s[i] == t[j]:
#                 i += 1
#                 j += 1
#             elif s[i] != t[j]:
#                 s += t[j]
#                 i += 1
#             elif t[i: len(t)] not in s:
#                 return len(t)
#         return len(s) - og
    

# My second solution: passed 67 cases out of the 85
#   class Solution:
#     def appendCharacters(self, s: str, t: str) -> int:
#         # if t has only 1 letter and that letter is already in s then return 0
#         if len(t) == 1 and t in s:
#             return 0

#         # if s has only 1 letter and that letter is not in t, then append t to s. Subtract 1 from the length so we don't count the letter in s
#         if len(s) == 1 and s not in t:
#             s += t
#             return len(s) - 1

#         for i in range(len(t)):
#             # if the letters in each string at the current index are not equal AND the current letter in t never appears again in the rest of the s string
#             if s[i] != t[i] and t[i] not in s[i:len(s)]:
#                 # return whatever is left in t
#                 return len(t[i: len(t)])
            

# My third solution: passed 33 out of the 85 cases
# class Solution:
#     def appendCharacters(self, s: str, t: str) -> int:
#         if len(t) == 1 and t in s:
#             return 0

#         # if s has only 1 letter and that letter is not in t, then append t to s. Subtract 1 from the length so we don't count the letter in s
#         if len(s) == 1 and s not in t:
#             s += t
#             return len(s) - 1

#         i = 0
#         j = 0
#         while j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#                 j += 1
#             elif s[i] != t[j]:
#                 i += 1
#             elif t[j: len(t)] not in s:
#                 return len(t)
#         return i - j