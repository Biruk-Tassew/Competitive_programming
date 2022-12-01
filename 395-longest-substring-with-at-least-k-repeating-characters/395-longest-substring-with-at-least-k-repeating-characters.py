class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        min_cnt_char = min(set(s), key=s.count)
        if s.count(min_cnt_char) >= k:
            return len(s)
        
        return max(self.longestSubstring(t, k) for t in s.split(min_cnt_char))