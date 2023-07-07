class Solution(object):
    def fizzBuzz(self, n):
        num_array = []
        for i in range(1, n + 1, 1):
            if i % 15 == 0:
                i = "FizzBuzz"
                num_array.append(i)
            elif i % 5 == 0:
                i = "Buzz"
                num_array.append(i)
            elif i % 3 == 0:
                i = "Fizz"
                num_array.append(i)
            else: # if it's not divisible by any of the above then just append it to the array
                num_array.append(str(i))
        return num_array

        """
        :type n: int
        :rtype: List[str]
        """
