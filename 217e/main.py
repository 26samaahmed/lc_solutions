class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        boolean = False # Have a default boolean value
        dictionary = {} # Create a dictionary that holds key value pairs where the number in the array is the key and how many time it appears is the value
        for number in nums:
            # If the key exists, increment its value. Otherwise, insert the key with value 1
            if number in dictionary:
                dictionary[number] += 1
            else:
                dictionary[number] = 1
    
        for val in dictionary.values(): # Loop through the values in the dictionary
            # If the value is bigger than 1, it means it has appeared more than once
            if val > 1:
                boolean = True # Change the value for the boolean since there is a duplicate
                return boolean
        return boolean # Returns false if the if condition in the for loop above wasn't satisified. If the if condition passed then it returns true

        
