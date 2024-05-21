class Solution: # my implementation after understanding neetcode's solution
    
    # loop through the list, if target - number is a number that's in the hashmap, then return the indices of these 2 numbers. Otherwise, add the value and it's index in the hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if target - nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                return [i, hash_map[target - nums[i]]]

'''
my original solution: got stuck when tried getting the indices because i sorted the list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # start by checking for lists with length 2. If the sum of the list is == target then return [0, 1]
        if len(nums) == 2:
            if sum(nums) == target:
                return [0, 1]

        end = len(nums) - 1
        sorted_sum_list = []
        index_list = []
        start = 0
        sorted_nums = sorted(nums)
        while start < end:
            if sorted_nums[start] + sorted_nums[end] == target:
                sorted_sum_list.append(sorted_nums[start])
                sorted_sum_list.append(sorted_nums[end])
                break
            elif sorted_nums[start] + sorted_nums[end] < target:
                start += 1
            elif sorted_nums[start] + sorted_nums[end] > target:
                end -= 1

        print(list(enumerate(sorted_sum_list)))
        for i in sorted_sum_list:
            index = nums.index(i)
            # if we have the value 3 in index 0 and 2, this will prevent us from getting a list [0, 0] and instead get [0, 2]
            if index in index_list:
                index += 1
            else:
                index_list.append(index)
        return index_list
        

# start by sorting the list. Have a left pointer that starts from index 0 and then a right pointer that is at the last index
# if the sum of both < target, then move the left pointer
# if the sum of both > target, move the right pointer
# if the sum of both == target, then return indices

'''