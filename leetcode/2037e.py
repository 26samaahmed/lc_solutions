class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(seats)):
            count += (abs(sorted(seats)[i] - sorted(students)[i]))
        return count
        