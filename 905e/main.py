class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd_list = []
        combined_list = []

        if len(nums) == 1: # if the size of the list is 1, then there is nothing to reorder so return the list right away
            return nums

        for number in nums:
            if number % 2 == 0: # if it's an even number
                combined_list.append(number) # append it to the new list
            else:
                odd_list.append(number) # if the number is odd, append it to a seperate list for odd number
            

        for i in odd_list:
            combined_list.append(i) # now append every number from the odd list to the end of the combined list that already contains the even numbers
        return combined_list

        
