class Solution:
    def countBits(self, n: int) -> List[int]:
        # for every number from 0 to n + 1, append how many ones were found in the binary version
        one_bits = []
        count = 0
        for i in range(n + 1):
            for j in bin(i):
                if j == '1':
                    count += 1
            one_bits.append(count)
            count = 0

        return one_bits