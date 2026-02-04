class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l_good_index=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=l_good_index:
                l_good_index=i
        
        if l_good_index==0:
            return True
        return False

        