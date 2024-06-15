class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        range_nums = []
        for i in range(1, len(nums) + 1):
            range_nums.append(i)
        return list(set(range_nums) - set(nums))
