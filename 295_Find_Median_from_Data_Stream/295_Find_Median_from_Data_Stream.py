
# space_complexity: O(1)
class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        
        
    # time_complexity: O(nlogn) for sorting
    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr)%2:
            return self.arr[len(self.arr)//2]
        return (self.arr[len(self.arr)//2 - 1] + self.arr[len(self.arr)//2])/2


class MedianFinder:

     def __init__(self):
         self.heap_one = []
         self.heap_two = []
         
     # time_complexity: O(logn)
     def addNum(self, num: int) -> None:
         heapq.heappush(self.heap_two, -num)
         
         if len(self.heap_two) - len(self.heap_one) >= 2:
             temp_val = -heapq.heappop(self.heap_two)
             heapq.heappush(self.heap_one, temp_val)
             
         if len(self.heap_one) >= 1 and self.heap_one[0] < -self.heap_two[0]:
             temp_val =  -heapq.heappop(self.heap_two)
             temp_val2 = -heapq.heappop(self.heap_one)
             
             heapq.heappush(self.heap_one, temp_val)
             heapq.heappush(self.heap_two, temp_val2)
             
         
             

     def findMedian(self) -> float:
         total_size = len(self.heap_one)+len(self.heap_two) 
         if total_size % 2 == 0:
             if len(self.heap_one):
                 return (self.heap_one[0]-self.heap_two[0])/2
             else:
                 return (-self.heap_two[1]-self.heap_two[0])/2
         else:
             return -self.heap_two[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
