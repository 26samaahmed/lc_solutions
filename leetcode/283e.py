class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

'''
Example explanation: Consider [0, 1, 0, 3, 12]. l and r will start at index 0. Since r == 0, it doesn't satisfy our if condition so we go
to the next iteration. l will stay at index 0 while r is now at index 1. In this iteration, r == 1 which satisifes our if condition so we
swap the values of l and r to get the following list [1, 0, 0, 3, 12] where l is now at index 1 and r is at index 2. In thid iteration,
r == 0 so we don't do anything and go to the next loop. l is still at index 1 while r is at index 3. The value for r here is 3 which satisfies
our if condition so we swap the value of l which was the 0 at index 1 with the value of r. Now we get this [1, 3, 0, 0, 12]. Now l is at index 2
and r is at index 4. r == 12 which satisfies our if condition so we swap and get the final answer [1, 3, 12, 0, 0, 0]
'''

'''
My original solution:
I was very close to the solution but I started from index 1 which made some test cases not pass.
After understanding neetcode's solution, i learned what quick sort algorithm is. I also had the wrong condition for my
if statement which made some test cases fail. I swapped whenever I found a 0 but this failed test cases like [0, 0, 1]. I
should swap only when the current index is not 0. My code printed [0, 0, 1, 3, 12] instead of [1, 3, 12, 0, 0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for r in range(1, len(nums)):
            if nums[r] == 0:
                nums[r - 1], nums[r] = nums[r], nums[r - 1]
      
'''