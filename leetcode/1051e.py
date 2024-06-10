class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        y = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != y[i]:
                count += 1
        return count