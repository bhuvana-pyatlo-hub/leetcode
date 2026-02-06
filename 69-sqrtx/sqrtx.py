class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:

            return x

        left, right = 1, x // 2
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                ans = mid          # mid is a valid square root
                left = mid + 1     # try to find a larger one
            else:
                right = mid - 1    # mid is too large

        return ans
