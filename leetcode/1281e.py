import numpy
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_list = [int(x) for x in str(n)]
        return numpy.prod(n_list) - sum(n_list)