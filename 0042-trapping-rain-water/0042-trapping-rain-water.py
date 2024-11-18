class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_left = height[left]
        max_right = height[right]
        water = 0
        
        while left < right:
            if max_left < max_right:
                water += max_left - height[left]
                
                left += 1
                max_left = max(max_left, height[left])
            else:
                water += max_right - height[right]
                
                right -= 1
                max_right = max(max_right, height[right])
                
        return water
                