#暴力枚举
#返回从第i个元素开始的最长递增子序列长度
def lengthFromI(nums,i):
    max_len = 1
    for j in range(i+1,len(nums)):
        if nums[i]<nums[j]:
            max_len = max(max_len,lengthFromI(nums,j)+1)
    return max_len

def numsLength(nums):
    maxLength = 1
    for i in range(0,len(nums)-1):
        maxLength = max(lengthFromI(nums, i),maxLength)
    return maxLength

nums=[1,5,2,4,3]
print(numsLength(nums))







