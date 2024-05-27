class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for x in range(len(nums) + 1):
            for i in nums:
                if i >= x:
                    counter += 1
            if counter == x:
                return counter
            else:
                counter = 0
        if counter == 0:
            return -1

# if x is equal to a certain number
# Loop through the list and check if we have x amount of numbers that are >= x
# technically the maximum x can be is the length of the the list, if x == len(list), then there must be x numbers bigger than or equal to x
