import sys
class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        t=x
        if(x<0):
            x*=-1
            flag=1
            t=x
        rev=0
        while x>0:
            a = x % 10
            rev = rev * 10 + a 
            x = x // 10
        if flag==1:
            rev*=-1
        if rev < -2**31 or rev > 2**31-1:
            return 0
        return rev
a = Solution()
x = 1534236469
s = a.reverse(x)
print(s)