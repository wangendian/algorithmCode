#迭代
def numsLength(nums):
    n = len(nums)
    lengthFromI = [1]*n
    for i in reversed(range(n-1)):
       for j in range(i,n-1):
            if(nums[j]>nums[i]):
                lengthFromI[i] = max(lengthFromI[i],lengthFromI[j]+1)
    return max(lengthFromI)


nums=[1,5,2,4,3]
print(numsLength(nums))







