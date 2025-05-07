class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        mp={}
        for i in range(len(nums)):
            mp[nums[i]]=i
        nums.sort()
        return mp[nums[-1]]
        