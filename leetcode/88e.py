
''' original solution but doens't pass all test cases
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # lets start by comparing the value at m and n so in ex1, we have m at index 2 with value 3 for nums1, and we have n at index 2 with value 6 in nums2
        # if the number at n is bigger than the number at m then insert the value at n in the end of nums1
        r = len(nums1) - 1

        # loop through something
        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1.insert(r, nums2[n - 1])
                r -= 1 # move on to the next empty space
                n -= 1
            if nums2[n - 1] < nums1[m - 1]:
                nums1[m - 1], nums1[m] = nums1[m], nums1[m - 1]
                m -= 1
            else: # if the 2 numbers are equal then insert
                nums1.insert(m - 1, nums2[n - 1])
                n -= 1
'''