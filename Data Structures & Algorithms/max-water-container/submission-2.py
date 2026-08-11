class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        volume=0
        while left<right:
            current_volume =min(heights[left], heights[right]) * (right - left)
            if current_volume>volume:
                volume=current_volume
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return volume