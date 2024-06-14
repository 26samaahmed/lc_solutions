class Solution:
    def longestPalindrome(self, s: str) -> int:
        # if we think about it, a palindrome can't have 2 letters that both have an odd number of occurence. A palindrodme can always be formed if the letters have an 
        # even number of occurence.
        # If we look at the example bananas, we get {b: 1, a: 3, n: 2: s: 1} and the longest palindrome to be formed is anana where we count the n since it has
        # an even number of occurences and we take the character with the biggest odd occurence which is a
        # if we look at abccccdd, we get {a: 1, b: 1, c: 4, d: 2}, in this case a palindorme can be formed with either a or b, it doesn't matter\
        s_map = {}
        count = 0
        has_odd = False
        odd_list = []

        for i in s:
            s_map[i] = 1 + s_map.get(i, 0)
        print(s_map)
        
        for j in s_map:
            # if the current letter has an even occurence, then count it right away
            if s_map[j] % 2 == 0:
                count += s_map[j]
            # else if the number is odd, then we set that to a var and count it at the end when we are sure it's the smallest odd number
            else:
                has_odd = True
                # we do -1 because that will give an even number that make a palindrome
                count += (s_map[j] - 1)
        
        # if an odd occurence was found, then add 1 to the count to place a letter in the center
        if has_odd == True:
            count += 1
        return count
