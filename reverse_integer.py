class Solution:
    def reverse(self, x: int) -> int:
        s=(x>0)-(x<0)
        r=int(str(x*s)[::-1])*s
        return r if -2**31<=r<2**31 else 0