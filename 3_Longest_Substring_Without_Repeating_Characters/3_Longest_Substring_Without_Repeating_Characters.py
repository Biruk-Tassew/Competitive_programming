class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = {}
        longest_list = 0
        
        for i in range(len(s)):
            if s[i] in end:
                start = max(start, end[s[i]] + 1)
            longest_list = max(longest_list, i-start + 1)

            end[s[i]] = i

 

        return longest_list
