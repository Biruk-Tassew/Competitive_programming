class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_chars = 0
        t = text.split()
        for i in text:
            if i != " ":
                total_chars += 1
                
        spaces_to_add = len(text) - total_chars
        
        in_btn_spaces = spaces_to_add // (len(t)-1 or 1)
        extra_spaces = spaces_to_add % (len(t)-1 or 1)
        if len(t) == 1:
            return t[0] + " "*in_btn_spaces
        return ((" "*in_btn_spaces).join(t)+(" "*extra_spaces))
        
        