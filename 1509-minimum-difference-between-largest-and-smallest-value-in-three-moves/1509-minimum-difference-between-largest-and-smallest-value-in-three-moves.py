class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        elif len(nums) <= 7:
            return self.calc_diff(nums, True)
        
        min_heap = nums
        heapq.heapify(min_heap)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        four_min_max = [0]*8
        temp = []
        for i in range(8):
            if i < 4:
                four_min_max[i] = heapq.heappop(min_heap)
            else:
                temp.append(-heapq.heappop(max_heap))
        
        four_min_max += temp[::-1]
        return self.calc_diff(four_min_max, False)
       
    def calc_diff(self, nums, flag):
        if flag:
            nums.sort()
        min_diff = float('inf')
        
        # change the three biggest elements
        min_diff = min(min_diff, nums[-4]-nums[0])
        
        # change the three smallest elemnts
        min_diff = min(min_diff, nums[-1]-nums[3])
        
        # change the the two smalles and 1 biggest element
        min_diff = min(min_diff, nums[-2]-nums[2])
        
        # change 1 smallest and 2 biggest elements
        min_diff = min(min_diff, nums[-3]-nums[1])
        
        return min_diff