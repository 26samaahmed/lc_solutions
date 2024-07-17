class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # start with an empty record
        # an integer x -> create a new score of x
        # + -> create a new score that is the sum of the 2 previous scores
        # D -> create a new score that is double the previous score
        # C -> remove the previous score from the record (potentially change the value to 0)
        # return the sum of the list after these operations
        stck = []
        for i in range(len(operations)):
            # check if i is not C, D, or +
            if operations[i] != 'C' and operations[i] != 'D' and operations[i] != '+':
                # add the value to a new list
                stck.append(int(operations[i])) # make sure to conver the current number to int
            elif operations[i] == 'C': # make the value at index i -1 = 0
                stck.pop()
            elif operations[i] == 'D': # multiply i - 1 in the new list by 2
                stck.append(stck[len(stck) - 1] * 2)
            else: # if it's a plus then add the 2 previous values
                stck.append(stck[len(stck) - 1] + stck[len(stck) - 2])

        return sum(stck)