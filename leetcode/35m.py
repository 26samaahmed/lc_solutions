class Solution: # working solution that passes all test cases
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # so we have a lists of lists where we must make sure
        # that the current list does not include duplicates + the number doesn't exit in the same index in other lists
        # Loop through the current list and store the numbers in a seperate list to check if the length of the list is equal to its set. If it is then no duplicates were found in that row

        # create a map where the current index is the key and the values are the numbers at that index
        # if the value for a key has duplicates then return false
        hash_map = {}
        # insert 9 keys from 0 through 8
        for i in range(0, 9):
            hash_map[i] = []
        index = 0
        for row in board:
            num_list = []
            for num in row:
                if num != ".":
                    num_list.append(int(num))
                    hash_map[index].append(int(num))
                index += 1
            index = 0
            if len(set(num_list)) != len(num_list):
                return False
        
        for a in hash_map:
            if len(hash_map[a]) != len(set(hash_map[a])):
                return False

        # Check for 3 x 3 sub boxes
        for i in range(0, 9, 3): #goes thru the row indices so i will get values 0, 3, 6
            for j in range(0, 9, 3): #goes thru the column indices so i will get values 0, 3, 6
                sub_box = []
                for k in range(3): # loop through the rows in the 3 by 3 box
                    for l in range(3): # loop through the columns in the 3 by 3 box
                        num = board[i + k][j + l]
                        if num != ".":
                            sub_box.append(int(num))
                if len(set(sub_box)) != len(sub_box):
                    return False
        return True
'''
class Solution: # original soltuion which passes 473 / 507 test cases
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # so we have a lists of lists where we must make sure
        # that the current list does not include duplicates + the number doesn't exit in the same index in other lists
        # Loop through the current list and store the numbers in a seperate list to check if the length of the list is equal to its set. If it is then no duplicates were found in that row

        # create a map where the current index is the key and the values are the numbers at that index
        # if the value for a key has duplicates then return false
        hash_map = {}
        # insert 9 keys from 0 through 8
        for i in range(0, 9):
            hash_map[i] = []
        index = 0
        for row in board:
            num_list = []
            for num in row:
                if num != ".":
                    num_list.append(int(num))
                    hash_map[index].append(int(num))
                index += 1
            index = 0
            if len(set(num_list)) != len(num_list):
                return False
        
        for i in hash_map:
            if len(hash_map[i]) != len(set(hash_map[i])):
                return False

        return True
'''