class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # starting from the beginning if i find a number that's odd append that to a new list, and continue
        # if the current number isnt odd then reset the list if it's not length 3
        # if i reach the end of the list and the size of the odd list is not 3 then return false
        odd_list = []
        for i in range(len(arr)):
            if arr[i] % 2 != 0: # if the number is odd
                odd_list.append(arr[i])
                if (len(odd_list)) == 3:
                    return True
            else: # if the number is not odd then reset the list
                odd_list = []
        return False
