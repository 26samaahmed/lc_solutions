class Solution(object):
    def intersection(self, nums1, nums2):
        common_elem_arr = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    if i not in common_elem_arr and j not in common_elem_arr:
                        common_elem_arr.append(i)
        return common_elem_arr
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
