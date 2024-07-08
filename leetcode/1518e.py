class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # so we know the sum will always contain numBottles and a few other numbers
        # Take the ex: numBottles = 15 and u can keep exchanging every 4 bottles to 1 full bottle
        # so 15 module 4 means we have 3 extra bottles that are still empty . For every 4 empty bottles, replace the value with 1
        # so now we have 3 full bottles and 3 empty, when u drink it, u have 6 empty bottles. 6 modolu 4 is 2 so we have 1 full bottle and 2 empty one
        # once u drink the one full bottle u are left with 3 empty bottles. Keep track of how many full bottes i have through each iteration.

        res = 0
        remainder = 0
        total = numBottles
        while total >= numExchange:
            remainder = total % numExchange
            res += int((total - remainder) / numExchange)
            total = (total % numExchange) + int((total - remainder) / numExchange)
        return res + numBottles