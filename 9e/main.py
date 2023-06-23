class Solution(object):
    def isPalindrome(self, x):
# thought process: to access the indices of the number, i should convert it to a string first
# check if the string from position 0 till the end is equal to when we reverse the string and start from -1
        y = str(x)
        if y[0:] == y[::-1]:
            return True
        else:
            return False
        """
        :type x: int
        :rtype: bool
        """
