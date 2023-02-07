class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for i in logs:
            if i[:2] == ".." and count:
                count -= 1
            elif i[0] != ".":
                count += 1
                
                
        return count