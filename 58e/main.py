class Solution(object):
    def lengthOfLastWord(self, s):
# thought process: i will start by using .split so that i can split the string into individual words in a list then i get the length of the last element in the list
        y = s.split()
        return len(y[-1])
        
    """
    :type s: str
    :rtype: int
    """
