class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        tot=0
        mp={}
        for i in skill:
            if i not in mp:
                mp[i]=0
            mp[i]+=1
            tot+=i
        
        if tot%(len(skill)//2)!=0:
            return -1
        i=0
        con=0
        target=tot//(len(skill)//2)
        while i<len(skill):
            if mp[skill[i]]>0:
                num=target-skill[i]
                if num in mp and mp[num]>0:
                    con+=num*skill[i]
                    mp[num]-=1
                    mp[skill[i]]-=1
                else:
                    return -1
            i+=1
        return con
            

                



        
        