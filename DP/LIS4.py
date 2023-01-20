#另一种递推公式的解法
def numsLength(nums):
    n = len(nums)
    lengthEndI = [1]*n #以i为结尾的最长单调子序列长度
    for i in (range(1,n)):
       for j in range(0,i):
            if(nums[j]<nums[i]):
                lengthEndI[i] = max(lengthEndI[i],lengthEndI[j]+1)
    return max(lengthEndI)


nums=[1,5,2,4,3]
print(numsLength(nums))







