class Solution:
    def decodeString(self, s: str) -> str:
        
        self.curPos = 0
        
        def realDecoder(curPos, s):
            outPut = ""
            while self.curPos < len(s) and s[self.curPos] != ']':
                if not s[self.curPos].isdigit():
                    outPut += s[self.curPos]
                    self.curPos += 1
                else:
                    tempNo = 0
                    while curPos < len(s) and s[self.curPos].isdigit():
                        tempNo = tempNo*10 + int(s[self.curPos])
                        self.curPos += 1

                    self.curPos += 1
                    tempAlpha = realDecoder(self.curPos, s)
                    self.curPos += 1 
                    
                    
                    outPut = outPut + (tempAlpha * tempNo)
                    tempNo = 0
            return outPut

        return realDecoder(self.curPos, s)
