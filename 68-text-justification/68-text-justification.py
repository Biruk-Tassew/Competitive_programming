class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_list = []
        cur_len = 0
        
        for word in words:
            if len(cur_list) + cur_len + len(word) > maxWidth:
                for i in range(maxWidth - cur_len):
                    cur_list[i%(len(cur_list)-1 or 1)] += " "
                    
                res.append("".join(cur_list))
                cur_list = []
                cur_len = 0
                
            cur_list.append(word)
            cur_len += len(word)
            
        res.append(" ".join(cur_list) + " "*(maxWidth - len(cur_list)-cur_len+1))
        return res
                    