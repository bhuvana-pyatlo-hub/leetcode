class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift=0
        m=left
        n=right
        while m!=n:
            m=m>>1
            n=n>>1
            shift=shift+1
        return m<<shift
        