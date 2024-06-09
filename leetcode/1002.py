class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # start by storing each key and value from the word at index 0
        count = Counter(words[0])

        for word in words:
            x = Counter(word)
            count &= x
        
        common = []
        for i in count.elements():
            common.append(i)
        return common