class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        
        s = 0 
        i = 2
        ans = []
        while s <= finalSum:
            ans.append(i)
            s += i
            i += 2
    
        if s > finalSum:
            ans.remove(s - finalSum)
    
        return ans