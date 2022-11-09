class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        count_less = 1
        while self.stock and self.stock[-1][0] <= price:
            count_less += self.stock.pop()[1]
            
        self.stock.append([price, count_less])
        return count_less


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)