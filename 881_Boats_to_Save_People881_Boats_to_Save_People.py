class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        left = 0
        right = len(people)-1
        count = 0 
        
        while left <= right:
            if left == right:
                count += 1
                break
            if people[left]+people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
                
            count += 1
                
        return count
