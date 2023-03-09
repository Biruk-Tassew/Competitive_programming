class StockSpanner:

    def __init__(self):
        self.stack = []
        self.poped = {}
        
    def next(self, price: int) -> int:
        count = 0
        while self.stack and self.stack[-1] <= price:
            if self.stack[-1] in self.poped:
                count += self.poped[self.stack[-1]][1]
            self.stack.pop()
            count += 1
            
        self.stack.append(price)
        self.poped[price] = (price, count)
            
        return count+1
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)