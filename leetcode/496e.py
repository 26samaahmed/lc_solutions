class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums1)):
            # if the current element is the biggest value starting from its index till the end then push -1
            x = nums2.index(nums1[i])
            if nums2[x] == max(nums2[x: len(nums2)]):
                arr.append(-1)
            else:
                i = x + 1
                while i < len(nums2):
                    if nums2[i] > nums2[x]:
                        arr.append(nums2[i])
                        break
                    else:
                        i += 1
        return arr