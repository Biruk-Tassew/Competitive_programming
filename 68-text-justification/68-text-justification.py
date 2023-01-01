class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_list = []
        cur_len = 0
        
        for word in words:
            if cur_len + len(cur_list) + len(word) > maxWidth:
                if len(cur_list) == 1:
                    res.append(cur_list[0]+" "*(maxWidth-len(cur_list[0])))
                else:
                    spaces_to_add = maxWidth - cur_len
                    in_btn_space = spaces_to_add // (len(cur_list)-1)
                    extra_space = spaces_to_add % (len(cur_list)-1)
                    
                    for i in range(extra_space):
                        cur_list[i] += " "
                        
                    res.append((" "*in_btn_space).join(cur_list))
                    
                cur_list = []
                cur_len = 0
                
            cur_list.append(word)
            cur_len += len(word)
            
        res.append(" ".join(cur_list)+" "*(maxWidth-cur_len-len(cur_list)+1))
        return res
                    