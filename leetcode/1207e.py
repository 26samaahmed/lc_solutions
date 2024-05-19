class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        default_bool = True
        # store key value pairs where each number in the array is the key and the value is the occurence
        dictionary = {}
        for number in arr:
            if number in dictionary: # if it exists in the dictionary then increment its occurence
                dictionary[number] += 1
            else:
                dictionary[number] = 1 # if it's not in the dict yet then insert it with value 1
        # Hint: Sets don't allow duplicates so if I took the length of the set of the dictionary's values, i would be able to find out if the values are unique
        # by checking if the length of the set of the dict values is the same as the length of the dict values
        # Ex: [-3,0,1,-3,1,1,1,-3,10,0]
        # the length of the set of the dict's values is 4, and the length of the dict values was also 4, this means no duplicates were found

        # Ex: [1,2]
        # The length of the set of the dict's values was 1 because both keys had the same value, while the length of the dict's value was 2 therefore they're not equal
        if len(set(dictionary.values())) != len(dictionary.values()):
            default_bool = False
        return default_bool
