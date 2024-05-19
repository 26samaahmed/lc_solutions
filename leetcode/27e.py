class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = len(nums) - 1 # try starting from the end of the list
        while i >= 0:
            if nums[i] == val:
                nums.remove(nums[i])
            i -= 1
        return len(nums)

# thought process:
# input: an array of numbers and a value
# output: the length of the elements left after we remove all the occurences of that value
# i would start looping from the end of the list so i'm looping from the end to the beginning, then i check whether 
# the element is equal to the value and if so then we remove it from the list then i decrement. This way i ensure i loop through the whole list
# and not skip the last occurence of the value
