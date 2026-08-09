class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i=0
        n= len(s)
        sol=[]
        while i<n:
            j=i
            while j<n and s[j]!="#":
                j+=1
            length=int(s[i:j])
            sol.append( s[j+1 : j+1+length] )
            i=j+1+length

        return sol
        