class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        
        while left<right:
            sum=numbers[left]+numbers[right]
            if sum==target:
                return (left+1,right+1)
                while left<right and numbers[left]==numbers[left-1]:
                    left=left+1
                while left<right and numbers[right]==numbers[right+1]:
                    right=right-1
            else:
                if sum<target:
                    left=left+1
                else:
                    right=right-1

            