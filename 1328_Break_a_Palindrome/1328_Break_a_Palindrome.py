class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        outPut =  palindrome
        
        for i in range(len(palindrome)//2):
            if  palindrome[i] != "a":
                outPut = palindrome[:i] + "a" + palindrome[i+1:]   
                break
                
        if outPut !=  palindrome:
            return  outPut
        return  palindrome[:-1]+"b"
