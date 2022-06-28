class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat_cap = 0
        curr_idx = 0
        last_idx = len(people)-1
        
        while curr_idx <= last_idx:
            
            left = limit - people[last_idx]
            last_idx -= 1
            
            if people[curr_idx] <= left:
                curr_idx += 1
                
            boat_cap += 1
