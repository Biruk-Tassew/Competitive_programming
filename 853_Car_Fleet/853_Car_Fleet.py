class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = sorted(zip(position, speed))
        time = [0]*len(position)
        
        for i in range(len(stack)):
            time[i] = (target - stack[i][0])/stack[i][1]
        res = 0
        while len(time) > 1:
            front = time.pop()
            
            if front < time[-1]:
                res += 1
            else:
                time[-1] = front
                
        return res + len(time)
                
            
            
