class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []
        for i in range(1, n+1):
            players.append(i)
            
       
        starting = 0
        def realWinnerFinder(players, starting):
            print(players)
            if len(players)==1:
                outPut = players[0]
                return players[0]
            
            starting = (starting+k-1)% len(players)
            players.remove(players[starting])
            return realWinnerFinder(players, starting)
           
        return realWinnerFinder(players, starting)
