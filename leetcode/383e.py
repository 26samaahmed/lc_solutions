class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # make a string ransomNote by using letters from magazine
        # note each value can be used once, if we have aa ab as the magazine then we can use a once which is why the test case aa fails
        # so the number of occurences should match
        ransom_map = {}
        magazine_map = {}
        # find the occurence of each letter in both strings
        for i in ransomNote:
            ransom_map[i] = 1 + ransom_map.get(i, 0)
        for j in magazine:
            magazine_map[j] = 1 + magazine_map.get(j, 0)

        # since we want to find all the letters that are in ransomNote
        for k in ransom_map:
            # check if the letter is in the magazine string. Return False if it doesn't since we can't construct a string using magazine
            if k in magazine_map:
                # since all letters can only be used once, we have to make sure that the letter appears more than or equal times its occurence in ransomNotes
                # ex: magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj" and ransomNote = "bg"
                # if we want to create a string "bg" then b and g have to appear at least once or more in magazine. If we can't do that, then return False
                if magazine_map[k] < ransom_map[k]:
                    return False
            else:
                return False
        
        return True