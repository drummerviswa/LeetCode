# Definition for singly-linked list.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        suml1=0
        suml2=0
        for a in l1:
            suml1+=a
        print(suml1)
        for b in l2:
            suml2+=b
        print(suml2)

a = Solution()
l1 = [5,6,4]
l2 = [2,4,3]
a.addTwoNumbers(l1,l2)
