class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        left = 0
        
        for i in logs:
            temp = i.split()
            if temp[1].isdigit():
                logs[left] = i
                left += 1
            else:
                letters.append(temp)
                
        letters.sort()
        letters.sort(key=lambda x:x[1:])
        temp_left = left
        for i in letters:
            logs[left] = " ".join(i)
            left += 1
            
        return logs[temp_left:]+logs[:temp_left]