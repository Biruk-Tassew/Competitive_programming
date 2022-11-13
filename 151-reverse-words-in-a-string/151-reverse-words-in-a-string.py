class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        ans = [" "]*len(s)
        
        idx = 0
        while idx < len(s):
            if s[idx] != " ":
                cur_len = 1
                while idx < len(s)-1 and s[idx+1] != " ":
                    cur_len += 1
                    idx += 1
                
                for i in range(idx, -1, -1):
                    if not cur_len:
                        break
                    ans[len(s)-i-1] = s[idx-cur_len+1]
                    cur_len -= 1
                
            idx += 1
            
        res = ""
        for i in range(len(ans)):
            if ans[i] == " " and ans[i-1] == " ":
                continue
            res += ans[i]
            
        return res