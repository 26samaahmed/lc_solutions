class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # i can use a map where the sorted word is the key and the value is the original words
        # that are the exact same when sorted
        # if the current word is in the map then append it to the value list
        sorted_list = []
        res = defaultdict(list)
        for word in strs:
            # sort word and append to new list
            sorted_word = ''.join(sorted(word))
            if sorted_word in res:
                res[sorted_word].append(word)
            else:
                res[sorted_word] = [word]
        return res.values()


''' og solution but i got stuck
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # if i sort each word then the i can compare strings and see if any 2
        # are the same and return the original string using the index

        sorted_list = []
        for word in strs:
            # sort word and append to new list
            sorted_word = sorted(word)
            sorted_word = ''.join(sorted_word)
            sorted_list.append(sorted_word)
          
        for i in range(len(sorted_list)):
            # if the current word exists somewhere else , push the current word and the original
            # word at that same index in the og list
 

'''