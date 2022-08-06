class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leads = -1
        self.winner = -1
        self.res = []
        board = {}
        for person in persons:
            if person not in board:
                board[person] = 0
            board[person] += 1
            if board[person] >= self.leads:
                self.leads = board[person]
                self.winner = person
            self.res.append(self.winner)
                

    def q(self, t: int) -> int:
        
        left = 0
        right = len(self.times)-1
        idx = -1
        
        while left <= right:
            mid = (left+right)//2 
            
            if self.times[mid] < t:
                left = mid + 1
            elif self.times[mid] > t:
                right = mid - 1
            else:
                idx = mid 
                break
        if idx == -1:
            idx = right
        return self.res[idx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
