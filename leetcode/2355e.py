class Solution(object):
    def repeatedCharacter(self, s):
        # thought process: i start by looping though the string and then i create a new list and append the new values as i loop through the string, once i find a letter that already exists in the new list, we return it right away
        new_list = []
        for i in s:
            if i not in new_list:
                new_list.append(i)
            else:
                return i

        """
        :type s: str
        :rtype: str
        """
