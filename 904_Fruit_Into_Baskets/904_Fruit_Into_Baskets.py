class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        occur_dict = {}
        start = 0
        max_fruit = 0
        
        for end in range(len(fruits)):
            right = fruits[end]
            if right in occur_dict:
                occur_dict[right] += 1
            else:
                occur_dict[right] = 1
                
            while len(occur_dict) > 2:
                left = fruits[start]
                occur_dict[left] -= 1
                if not occur_dict[left]:
                    del occur_dict[left]
                start += 1
            max_fruit = max(max_fruit, end-start+1)
        
        return max_fruit
        
