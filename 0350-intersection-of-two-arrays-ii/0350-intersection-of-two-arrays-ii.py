class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mp1,mp2={},{}
        for i in nums1:
            if i not in mp1:
                mp1[i]=0
            mp1[i]+=1
        for i in nums2:
            if i not in mp2:
                mp2[i]=0
            mp2[i]+=1
        a=set(nums1)
        ans=[]
        for i in a:
            if i in mp1 and i in mp2:
                for j in range(min(mp1[i],mp2[i])):
                    ans.append(i)
        return ans
