class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums) // 2 
        dictionary = dict()
        # start by looping through the list
        for number in nums:
            if number in dictionary: # if it exists in the dictionary
                dictionary[number] += 1 # we increment the count of occurence
            else: # if the number doesn't exist yet in the dict
                dictionary[number] = 1 # provide a starting value of 1 since it now exists
        # i would sort the dictionary
        for x, y in dictionary.items():
            if y > size:
                return x

# 1. input: an array of nums
# 2. output: the number that appears the most in the array
# 3. thought process: i would calculate the value for the floor rounding of the array size divided by 2. Then I would create a dictionary where i increment the count for the number everytime it appears. Then i would loop through each pair and compare the values with the len(nums)// 2 and if it's bigger then return the key
# 4. edge cases i thought of: 
# - if there are 2 numbers that are both considered the majority element (occur an equal amount of times)
# - if there is only 1 element in the array
