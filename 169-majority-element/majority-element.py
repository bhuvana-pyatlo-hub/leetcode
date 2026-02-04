class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        n = len(nums)

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        for key, val in seen.items():
            if val > n // 2:
                return key
