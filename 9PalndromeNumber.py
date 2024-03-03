class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)[::-1]
        if temp == str(x):
            return True
        else:
            return False

a = Solution()
x = 11211
s = a.isPalindrome(x)
print(s)