class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1

        print(nums)
        return left

# neetcode video ref to understand: https://youtu.be/DEJAZBq0FDA?si=laanI3PbisDOhsZ7
# non-decreasing order -> increasing but there can be duplicates like this [1,3,3,4,5,5]
# The first value in the list will always be unique since there's no value before it to duplicate
# so start by creating a left and right pointer at index 1
# start by comparing the current value to the one before it, if the current value is a duplicate then
# move the right pointer 1 step ahead. If the current value is not equal to the one before it,
# then this is the first occurence which means we can switch positions and move the left and right pointer to the next value
# Pattern: if the 2 values are equal, only move the right pointer. If the 2 values are different,
# then shift both left and right pointer

# My original solution was to go through the list, and keep track of duplicates using a dictionary. If the value of the key is not 1
# then it means we found a duplicate so I pop it and add an underscore to the end of the list but this didn't work. 