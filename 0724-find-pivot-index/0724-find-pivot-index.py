class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot=0
        for i in range(len(nums)):
            tot+=nums[i]
        l=0
        
        for i in range(len(nums)):
            if tot-nums[i]==l:
                return i
            l+=nums[i]
            tot-=nums[i]
        return -1