class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # get the sum of the current list + the sum of the length of the list and return the diff
        sum_nums = 0
        for i in range(len(nums) + 1):
            sum_nums += i
        return sum_nums - sum(nums)