class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # can start by storing key value pairs from arr1, then start by looping through array 2 and append to the new list the number of occurences, if there's anything left
        # that's not in the list then sort then append
        
        # first start by eliminating all the numbers that are uncommon
        uncommon = []
        combined = []
        arr1_map = {}
        combined_map = {}
        for i in arr1:
            if i not in arr2:
                # store what's not common
                uncommon.append(i)
            arr1_map[i] = 1 + arr1_map.get(i, 0)

        for j in arr2:
            if j in arr1_map:
                # store the occurence of letter j from arr1 in the combined dict at that specific key
                combined_map[j] = arr1_map[j]

        # append the values depending on how many times they appear in the list
        for k in combined_map:
            for e in range(combined_map[k]):
                combined.append(k)   

        for c in sorted(uncommon):
            combined.append(c)
        return combined

