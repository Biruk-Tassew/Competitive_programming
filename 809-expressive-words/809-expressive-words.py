class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
           
        cnt = 0
        for word in words:
            left = len(s)-1
            right = len(word)-1
            
            stretchy = True
            while left >= 0 and right >= 0:
                if s[left] != word[right]:
                    stretchy = False
                    break
                    
                current_letter = s[left]
                
                s_cnt = 0
                while left >= 0 and s[left] == current_letter:
                    s_cnt += 1
                    left -= 1
                
                w_cnt = 0
                while right >= 0 and word[right] == current_letter:
                    w_cnt += 1
                    right -= 1
                    
                if w_cnt > s_cnt or ((s_cnt > w_cnt) and s_cnt < 3):
                    stretchy = False
                
            if len(word) <= len(s) and stretchy and left < 0:
                cnt+= 1
        
        return cnt