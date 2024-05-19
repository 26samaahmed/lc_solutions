class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        for i in nums:
            i = i * i
            new_list.append(i)
        new_list.sort()
        return new_list
