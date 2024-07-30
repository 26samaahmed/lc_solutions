class Solution:
    def isHappy(self, n: int) -> bool:
        exists = set()
        total = 0

        # if the current number is not a 1 and doesnt exist in the set yet
        while n != 1 and n not in exists:
            exists.add(n)
            for i in str(n):
                total += pow(int(i), 2)
            n = total
            total = 0
        return n == 1
'''
class Solution: # passes 417/420 test case
    def isHappy(self, n: int) -> bool:
        # ideally we would use recursion to narrow down as long as the sum is 1
        # if the sum is 1 which is the base case then stop the recursion and return true
        # if one digit is left and it isn't 1 then return False
        # visit case where i get the square of the digits
        
        if len(str(n)) == 1 and n != 1:
            return False

        if n == 1:
            return True

        total = 0
        for i in str(n):
            total += pow(int(i), 2)
        
        n = total
        # recursive case where we pass the new val
        return self.isHappy(n)
            
'''