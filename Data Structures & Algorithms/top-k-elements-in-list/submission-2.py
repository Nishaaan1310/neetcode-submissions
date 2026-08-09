from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        heap=[]
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

        while len(heap)>k:
            heapq.heappop(heap)
        sol=[num for count, num in heap]
        return sol



        
        