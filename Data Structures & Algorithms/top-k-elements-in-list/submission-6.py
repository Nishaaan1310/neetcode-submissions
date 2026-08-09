from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        freq_bucket= [[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            freq_bucket[count].append(num)

        sol=[]
        for i in range (len(freq_bucket)-1,0, -1):
            for num in freq_bucket[i]:
                sol.append(num)
                if len(sol)==k:
                    return sol
        

        
        