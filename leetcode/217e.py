class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# we know that if a number appears twice, then it's length will be different the length of it's set. Since sets don't allow duplicates
# then it will determine whether there are repeated number if length of set is not equal to the length of the list.

# Another Solution:
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store_list = {}
        for i in nums:
            # if the number is already in the dictionary, then there is a duplicate so return True
            if i in store_list:
                return True
            else:
                store_list[i] = 1
        return False
'''