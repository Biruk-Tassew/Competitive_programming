class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        ans = [''] * numRows
        idx, dirc = 0, 1

        for char in s:
            ans[idx] += char
            if not idx:
                direc = 1
            elif idx == numRows -1:
                direc = -1
            idx += direc

        return ''.join(ans)