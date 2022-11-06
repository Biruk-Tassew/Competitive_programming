class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s = list(s)

        if k == 1:
            temp = s
            for i in range(len(s)):
                temp = min(temp, s[i:]+s[:i])
            return ''.join(temp)
        return "".join(sorted(s))
