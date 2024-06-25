class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # we're given a specific row number but add 1 since it's 0 indexed
        # if we have row 3 then we want 4 numbers
        res = [[1]]
        for i in range(rowIndex):
            # im going to do the same process of finding the previous rows and return the list at the specified index
            row = []
            # append 0 to beginning and end
            temp = [0] + res[-1] + [0]
            # loop through the previous list and start adding the nums together
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)

        return res[rowIndex]