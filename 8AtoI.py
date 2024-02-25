class Solution:
    def myAtoi(self, x: str) -> int:
        s = str(x)
        if s[0] == '-':
            m = -1
            s = s[1:]
        else:
            m=1 
        a = m*(int(s[::-1]))
        if a in range(-2**31, 2**31):
            return a
        else:
            return 0
a = Solution()
x = "-5-"
s = a.myAtoi(x)
print(s)