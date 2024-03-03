class Solution:
    def intToRoman(self, num: int) -> str:
        hashtable={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = ""
        while(num!=0):
            rem=num%10
            for key,i in hashtable.items():
                if rem<=i:
                    print(rem)
            num//=10
        return result
a = Solution()
re = a.intToRoman(121)
print(re)