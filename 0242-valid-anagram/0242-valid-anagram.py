class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        d1 = {}
        for i in s:
            d1[i]=d1.get(i,0)
            d1[i]+=1
            
        d2 = {}
        for j in t:
            d2[j]=d2.get(j,0)
            d2[j]+=1
            

        if (d1==d2):
            return True
        else:
            return False

         
        