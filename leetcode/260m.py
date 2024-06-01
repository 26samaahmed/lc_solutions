class Solution: # After understanding neetcode's solution using bit manipulation
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
            # in final iteration this will print 00110
        
        # since we want to find the 2 numbers that appear once based on what we have in the second index here 00110 (this is the result of xoring 5 and 3)
        difference = 1
        # start by checking that when anding the result we have with 1, we don't get 00000
        while not (xor & difference):
            # go to next bit by shifting 1 to the left
            difference = difference << 1

        val1, val2 = 0, 0
        for n in nums:
            if n & difference:
                val1 = val1 ^ n
            else:
                val2 = val2 ^ n
        return [val1, val2]

'''
 My original solution:  [first medium :)] my solution was O(n) space and time
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in sorted(nums):
            counter[num] = 1 + counter.get(num, 0)
        return {i for i in counter if counter[i] == 1}
'''