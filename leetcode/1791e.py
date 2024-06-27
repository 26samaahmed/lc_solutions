class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # if one of the 2 numbers in the first list occurs in every other pair then return that
        # whoever has the same count as the length of the edges is the common element
        first = edges[0][0]
        second = edges[0][1]
        count1 = 1
        count2 = 1
        for i in range(1, len(edges)):
            if first in edges[i]:
                count1 += 1
            elif second in edges[i]:
                count2 += 1
        if count1 == len(edges):
            return first
        if count2 == len(edges):
            return second