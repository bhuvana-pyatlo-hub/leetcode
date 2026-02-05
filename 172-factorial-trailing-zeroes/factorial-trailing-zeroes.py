class Solution:
    def trailingZeroes(self, n: int) -> int:
        # the count of trailing zeros is given by counting the number of 
        # factor of 5 in factorial
        i=0
        while n>0:
            n //=5
            i+=n

        return i

        