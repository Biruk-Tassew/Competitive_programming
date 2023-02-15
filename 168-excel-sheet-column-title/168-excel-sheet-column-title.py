class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            
            columnNumber -= 1
            cur_char = chr(columnNumber%26 + 65)
            title += cur_char 
            columnNumber //= 26
            
        return title[::-1]
            
            
        