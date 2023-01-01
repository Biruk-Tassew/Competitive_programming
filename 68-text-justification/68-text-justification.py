class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_list = []
        cur_len = 0
        
        for word in words:
            if cur_len + len(word) + len(cur_list) > maxWidth:
                if len(cur_list) == 1:
                    res.append(cur_list[0]+" "*(maxWidth-cur_len))
                else:
                    spaces = maxWidth - cur_len
                    space_btn = spaces//(len(cur_list)-1)
                    space_extra = spaces%(len(cur_list)-1)
                    
                    for i in range(space_extra):
                        cur_list[i] += " "
                        
                    res.append((" "*space_btn).join(cur_list))
                cur_list = []
                cur_len = 0
            cur_list.append(word)
            cur_len += len(word)
            
        
        res.append(" ".join(cur_list)+" "*(maxWidth-cur_len-len(cur_list)+1))    
        return res
                    