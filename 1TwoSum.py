class Solution():
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        return [i,j]
nums = [2,7,11,19]
target = 9
a = Solution()
result = a.twoSum(nums,target)
print(result)