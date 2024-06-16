class Solution: # how i understood after watching neetcode's video
    def generate(self, numRows: int) -> List[List[int]]:
        # we know the list has to contain at least the first row
        res = [[1]]
        # i will start looping through the range of numRows. Since the list already has [1], make sure to subtract 1 from numRows when i loop
        for i in range(numRows - 1):
            # create an empty row
            row = []
            # append 0s to the beginning and ending of the previous row because we want to add evry 2 numbers from the previous row
            # res[-1] signifies the last row in the list
            temp = [0] + res[-1] + [0]
            # loop through the range of the length of the previous row + 1 to create the new row
            for j in range(len(res[-1]) + 1):
                # now append to the row, the sum of every 2 numbers. Ex: row 1 has [0, 1, 0] so add 0 to 1 to get 1 and so on until we end up with [1, 1,]
                row.append(temp[j] + temp[j + 1])
            res.append(row)

        return res