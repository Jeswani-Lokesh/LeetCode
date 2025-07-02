class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i,j = 0, len(s)-1

        while True:
            if s[j] == " ":
                j-=1
                continue
            break
        
        i=j-1

        while True:
            if i>=0 and s[i]!= " ":
                i-=1
                continue
            break
        return j-i

        