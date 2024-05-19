class Solution(object):
    def hammingWeight(self, n):
        counter = 0
        for i in bin(n):
            if i == '1':
                counter += 1
        return counter
        """
        :type n: int
        :rtype: int
        """
        
# Input: an integer
# Output: number of 1 bits in the binary form of the integer
# Thought Process: start by converting to binary number, then loop through the number. If a 1 is found, increase the count.
