class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r=1,sum(nums)
        ans=-1
        def fun(num):
            tot=0
            for i in nums:
                tot+=ceil(i/num)
            return tot

        while l<=r:
            mid=(l+r)//2
            num=fun(mid)
            if num<=threshold:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans



        