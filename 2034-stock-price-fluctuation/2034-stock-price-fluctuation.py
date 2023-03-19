class StockPrice:

    def __init__(self):
        self.updated = {}
        self.min_heap = []
        self.max_heap = []
        self.cur_price = (0, -1)

    def update(self, timestamp: int, price: int) -> None:
        self.updated[timestamp] = price 
        
        heappush(self.min_heap, [price, timestamp])
        heappush(self.max_heap, [-price, timestamp])
        
        if timestamp >= self.cur_price[1]:
            self.cur_price = (price, timestamp)
        
    def current(self) -> int:
        return self.cur_price[0]

    def maximum(self) -> int:
        temp = heappop(self.max_heap)
        while self.updated[temp[1]] != -temp[0]:
            temp = heappop(self.max_heap)
            
        heapq.heappush(self.max_heap, temp)
        return -temp[0]

    def minimum(self) -> int:
        temp = heappop(self.min_heap)
        while self.updated[temp[1]] != temp[0]:
            temp = heappop(self.min_heap)
            
        heapq.heappush(self.min_heap, temp)
        return temp[0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()