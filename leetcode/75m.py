class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # so we know that we have 3 variations for numbers, we have 0 1 and 2
        # sorting them means that we want all the zeros on the left side and then all the 2s on the right side
        # to keep track of them both, let's use a left and right pointer
        l, r = 0, len(nums) - 1

        # let's also have an i pointer that will keep moving to be swaped

        i = 0

        # since we're swapping in multiple diff if statements, let's create a helper function to do that so it's less lines of code
        def swap(j, h):
            nums[h], nums[j] = nums[j], nums[h]
        
        # now we start looping as long as i doesn't cross r since once they cross we know the list should be alrdy sorted
        while i <= r:
            # if the number at i == 0
            if nums[i] == 0:
                swap(l, i)
                # increment the l value
                l += 1
            # if the number at i == 2
            if nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1