class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # this is very similar to a problem i did using Counter and finding the minimum common intersection
        common = []
        x = Counter(nums1)
        x &= Counter(nums2)
        for i in x.elements():
            common.append(i)
        return common
