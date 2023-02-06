class DetectSquares:

    def __init__(self):
        self.points = []
        self.point_count = defaultdict(lambda: 0)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.point_count[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        count_s = 0
        
        for i in self.points:
            if (abs(i[0]-point[0]) == abs(i[1]-point[1])) and i[0] != point[0] and i[1] != point[1]:
                count_s += self.point_count[(i[0], point[1])]*self.point_count[(point[0], i[1])]
                
        return count_s

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)