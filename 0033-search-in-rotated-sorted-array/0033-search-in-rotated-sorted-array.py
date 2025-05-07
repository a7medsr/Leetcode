class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mp={}
        for i in range(len(nums)):
            mp[nums[i]]=i
        if target in mp:
            return mp[target]
        return -1
        nums.sort()
        l=0
        r=len(nums)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                ans=1

        