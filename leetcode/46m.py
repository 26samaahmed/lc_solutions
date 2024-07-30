class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]] # start with an empty list

        # for every number, generate a new permutation
        for n in nums:
            new_perms = []
            # for each existing permutation, insert the current number
            for p in perms:
                for i in range(len(p) + 1): # insert into every possible position in p
                    p_copy = p.copy() # copy the current permutation
                    p_copy.insert(i, n) # insert in the ith position
                    new_perms.append(p_copy) # append the new permutation
            perms = new_perms
        return perms