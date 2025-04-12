class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot=1
        ze=0
        for i in nums:
            if i != 0:
                tot*=i
            else:
                ze+=1
        if ze>1:
            for i in range(len(nums)):
                nums[i]=0
        elif ze==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=tot
                else:
                    nums[i]=0
        else:
            for i in range(len(nums)):
                nums[i]=int(tot/nums[i])
        return nums
        
        