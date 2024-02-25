class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        nums1.sort()
        size = len(nums1)
        if size%2!=0:
            t = int(size/2)
            return nums1[t]
        else:
            t1 = int(size/2) -1
            t2 = int(size/2)
            t = (nums1[t1]+nums1[t2])/2
            return t
a = Solution()
x=[1,3]
y=[2]
f=a.findMedianSortedArrays(x,y)
print(f)