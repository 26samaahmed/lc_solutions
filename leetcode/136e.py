class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) == 1:
                return i

# thought process:
# inputs: an array of numbers
# outputs: the only number that doesn't appear twice in the list
# i would loop though the array, check what value has the count 1 and then return that number
