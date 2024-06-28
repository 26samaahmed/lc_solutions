class Solution:
    def addDigits(self, num: int) -> int:
        # we could do recursion where the base case is if the digit is length 1
        # the visit case would be a for loop that gets the total of the current digits we have and then we pass that new value in the recusrive call
        if len(str(num)) == 1:
            return num
        res = 0
        for i in str(num):
            res += int(i)
        num = res
        return self.addDigits(num)