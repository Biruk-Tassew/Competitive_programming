class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(lambda: 0)
        max_fruits = 0
        
        
        left = 0
        right = 0
        
        while right < len(fruits):
            basket[fruits[right]] += 1
            
            if len(basket) > 2:
                basket[fruits[left]] -= 1
                
                if not basket[fruits[left]]:
                    del basket[fruits[left]]
                    
                left += 1
                    
            max_fruits = max(max_fruits, right - left + 1)
            right += 1
            
            
        return max_fruits