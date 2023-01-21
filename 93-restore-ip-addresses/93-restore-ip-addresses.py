class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.backTrack(0, "", s)
        return self.res
        
    def backTrack(self, cur_idx, cur_ip, s):
        if cur_idx >= 4:
            if not s:
                self.res.append(cur_ip[:-1])
            return
        
        for i in range(1, len(s)+1):
            if s[:i] == "0" or (s[0]!='0' and 0 < int(s[:i]) <= 255):
                self.backTrack(cur_idx+1, cur_ip+s[:i]+".", s[i:])