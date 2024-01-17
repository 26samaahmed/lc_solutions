class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        sum = 0
        for i in stones:# to check how many stones are in jewels, i would loop through the stones and see if the current value exist in jewels
            if i in jewels: # if the common letter is found
                sum += 1 # add to total
        return sum
