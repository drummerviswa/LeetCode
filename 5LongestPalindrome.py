class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        maxlength=1
        result=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > maxlength and s[i:j+1] == s[i:j+1][::-1]:
                    maxlength = j-i+1
                    result = s[i:j+1]

        return result

a = Solution()
str = "cbbd"
s = a.longestPalindrome(str)
print(s)