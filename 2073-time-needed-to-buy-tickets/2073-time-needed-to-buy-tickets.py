class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
       
        que = deque(tickets)
        time = 0
        
        while que[k]:
        
            if(que[0]==1):
                que.popleft()
                
                if(k==0):
                    return(time+1)
                else:
                    k -= 1
            else:
                que.append(que[0]-1)
                que.popleft()
                if(k==0):
                    k=len(que)-1
                else:
                    k-=1
                    
            time += 1
                    
        return time
                
            
            
                
            