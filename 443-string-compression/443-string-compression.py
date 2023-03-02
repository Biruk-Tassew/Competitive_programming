class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        
        
        idx = 0
        main_idx = 0
        
        while idx < len(chars):
            cur_char = chars[idx]
            cur_count = 0
            
            while idx < len(chars) and chars[idx] == cur_char:
                idx += 1
                cur_count += 1
                
            chars[main_idx] = cur_char
            main_idx += 1
            
            if cur_count != 1:
                for i in str(cur_count):
                    chars[main_idx] = i
                    main_idx += 1
                
        return main_idx