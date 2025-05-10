class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r=1,2e6
        ans=0
        while l<=r:
            mid=int((l+r)//2)
            tot=(mid*(mid+1))/2   
            if tot<=n:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
            



        