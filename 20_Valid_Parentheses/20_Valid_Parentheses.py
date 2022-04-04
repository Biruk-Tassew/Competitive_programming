class Solution:
    def isValid(self, s: str) -> bool:
        br_dict = {'(' : ')', '{':'}', '[':']'} 
        stackArr = []
        
        revStr = s[::-1]
        for i in revStr:
            if len(stackArr) == 0:
                stackArr.append(i)
                continue

            if i in br_dict.values():
                stackArr.append(i)
            else:
                
                if stackArr[-1] in br_dict.values() and i == list(br_dict.keys())[list(br_dict.values()).index(stackArr[-1])]:
                    stackArr.pop()
                else:
                    return False
                    
        if (len(stackArr)==0):
            return True
        else:
            return False
