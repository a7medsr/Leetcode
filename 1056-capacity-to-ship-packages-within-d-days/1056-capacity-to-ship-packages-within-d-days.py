class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ans=-1
        l=max(weights)
        r=sum(weights)
        while l<=r:
            mid=((l+r)//2)
            c=1
            tot=0
            for i in weights:
                if tot+i>mid:
                    tot=0
                    c+=1
                tot+=i
            if c<=days:
                ans=mid
                r=mid-1
            else:
                
                l=mid+1
        return ans