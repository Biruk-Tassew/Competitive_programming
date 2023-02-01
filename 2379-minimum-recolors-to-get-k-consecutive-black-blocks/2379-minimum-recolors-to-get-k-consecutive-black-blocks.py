class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        no_black = 0
        no_white = 0
        
        for i in blocks[:k]:
            if i == "W":
                no_white += 1
            else:
                no_black += 1
                
        min_white = no_white
        right = k-1
        left = 0
        while right < len(blocks)-1:
            left += 1
            right += 1
            
            if blocks[left-1] == "W":
                no_white -= 1
            
            if blocks[right] == "W":
                no_white += 1
            
            min_white = min(min_white, no_white)
            
        return min_white