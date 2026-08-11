class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        volume=0
        while left<right:
            volume = max( min(heights[left], heights[right]) * (right-left), volume)
            if heights[left]>heights[right]:
                    right-=1
            elif heights[left]<heights[right]:
                    left+=1
            else:
                right-=1
        return volume