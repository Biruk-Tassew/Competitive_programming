class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        indices_growTime = [(growTime[i], i) for i in range(len(growTime))]
        indices_growTime.sort(reverse=True)
        plant_time = 0
        earliest_time = 0
        
        for i in indices_growTime:
            plant_time += plantTime[i[1]]
            earliest_time = max(earliest_time, plant_time + growTime[i[1]])
            
        return earliest_time
