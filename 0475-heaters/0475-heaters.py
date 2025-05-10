class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        l,r=0,1e9
        houses.sort()
        heaters.sort()
        ans=-1
        while l<=r:
            mid = int((l + r) // 2)
            c=0
            for hos in houses:
                idx=bisect_left(heaters,hos)
                if 0<idx:
                    lf2,ri2=heaters[idx-1]-mid,heaters[idx-1]+mid
                    if lf2<=hos<=ri2:
                        c+=1
                        continue
                if idx<len(heaters):
                    lf1,ri1=heaters[idx]-mid,heaters[idx]+mid
                    if lf1<=hos<=ri1:
                        c+=1
                        continue
            if c==len(houses):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
                


        
        