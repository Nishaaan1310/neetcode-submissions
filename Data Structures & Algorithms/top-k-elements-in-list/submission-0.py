class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        sorted_freq=sorted(freq.keys(), key=lambda k: freq[k], reverse=True)
        sol=[]
        count=0
        for key in sorted_freq:
            sol.append(key)
            count+=1
            if count==k:
                break
        return sol

        
        