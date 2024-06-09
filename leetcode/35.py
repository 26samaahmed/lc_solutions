class Solution: # After watching and understanding neetcode's solution
    def searchInsert(self, nums: List[int], target: int) -> int:
        # i would prob use binary search since it's sorted in ascending order. The middle index is the root, anything on the left is smaller and anything on the righ is bigger
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid_index = (start + end) // 2
            # if target is less than the number in the middle then change the end var
            if target == nums[mid_index]:
                return mid_index
            elif target < nums[mid_index]:
                end = mid_index - 1
            else:
                start = mid_index + 1
        return start

# Think of it like this, let's say we have this [1] and we want to insert 2. Initially, start and end both start at index 1. We know that 2 > 1
# so this means the start pointer would move to the right and become at index 1 which is exactly where we want to insert 2
# Let's say our target was 0 and the list is [1], we know 0 < 1 so the end pointer would move to the left and put the target at index 0

'''
My original solution: passed 28/65 cases but then would get out of range error
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # i would prob use binary search since it's sorted in ascending order. The middle index is the root, anything on the left is smaller and anything on the righ is bigger

        # If number exists in list, return its index right away
        if target in nums:
            return nums.index(target)

        start = 0
        end = len(nums) - 1
        while start <= end:
            # Before finding the middle index, check that the start and end are not equal because if they are, then dividing would give out of range error
            if start == end:
                if target > nums[start]:
                    nums.insert(start + 1, target)
                    return start + 1
                else:
                    nums.insert(start, target)
                    return start

            mid_index = start + end // 2
            mid_num = nums[mid_index]
            # if target is less than the number in the middle then change the end var
            if target < mid_num:
                end = mid_index - 1
            elif target > mid_num:
                start = mid_index + 1
            else:
              return 0

        nums.insert(start, target)
        return start


'''