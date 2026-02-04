class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.strip().split() #strip removes the trailing left and right spaces
        return len(words[-1])
        