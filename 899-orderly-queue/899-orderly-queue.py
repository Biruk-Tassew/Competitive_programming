class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        s = list(s)

        if k == 1:
            temp = []
            for i in range(len(s)):
                temp.append(s[i:]+s[:i])
            return ''.join(min(temp))
        return "".join(sorted(s))
