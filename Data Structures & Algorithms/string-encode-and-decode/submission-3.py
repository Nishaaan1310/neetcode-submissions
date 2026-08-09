class Solution:
    def encode(self, strs: List[str]) -> str:
        n=len(strs)

        for i in range(n):
            strs[i]= str(len(strs[i])) + "#" + strs[i]
        sol= "".join(strs)
        return sol

    def decode(self, s: str) -> List[str]:
        i=0
        n= len(s)
        sol=[]
        while i<n:
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            sol.append( s[j+1 : j+1+length] )
            i=j+1+length

        return sol
        