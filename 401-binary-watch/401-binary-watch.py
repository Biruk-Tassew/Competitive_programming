class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.hrs = [1, 2, 4, 8]
        self.mins = [1, 2, 4, 8, 16, 32]
        self.res = set()
        self.solve([0, 0], turnedOn, 0)
        
        return self.res
        
    def solve(self, time, left, st_pt):
        if not left:
            if time[1] < 10:
                self.res.add(str(time[0])+":0"+str(time[1]))
            else:
                self.res.add(str(time[0])+":"+str(time[1]))
                
            return
        
        for i in range(st_pt, 10):
            if i < len(self.hrs):
                time[0] += self.hrs[i]
                if time[0] < 12:
                    self.solve(time, left-1, i+1)
                time[0] -= self.hrs[i]
            else:
                time[1] += self.mins[i-4]
                if time[1] < 60:
                    self.solve(time, left-1, i+1)
                time[1] -= self.mins[i-4]