class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        first_cities = [city[0] for city in costs]
        diff = [j-i for i,j in costs]
        
        return sum(first_cities) + sum(sorted(diff)[:len(costs)//2])