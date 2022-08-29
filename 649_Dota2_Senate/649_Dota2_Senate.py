class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        rad = deque()
        dire = deque()
        
        for i in range(len(senate)):
            if senate[i] == "R":
                rad.append(i)
            else:
                dire.append(i)
                
        while rad and dire:
            rad_idx = rad.popleft()
            dire_idx = dire.popleft()
            
            if rad_idx < dire_idx:
                rad.append(rad_idx+len(senate))
            else:
                dire.append(dire_idx+len(senate))
                
        if rad:
            return "Radiant"
        else:
            return "Dire"
