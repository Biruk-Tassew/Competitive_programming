class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        
        
        chars_lenght = len(chars)
        idx = 0
        i = 0
        while i < len(chars):
            count = 0
            curr_char = chars[i]
            
            while(i < len(chars) and chars[i]==curr_char):
                i += 1
                count += 1
                
            chars[idx] = curr_char
            idx += 1
            
            if count != 1:
                for j in str(count):
                    chars[idx] = j
                    idx += 1
                
        return idx
                
            
                
        
            
                
