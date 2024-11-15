class RandomizedSet:

    def __init__(self):
        self.randomized_set = set() 

    def insert(self, val: int) -> bool:
        if val in self.randomized_set:
            return False
        
        self.randomized_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomized_set:
            return False
        
        self.randomized_set.remove(val)
        return True

    def getRandom(self) -> int:
        index = randint(0, len(self.randomized_set)-1)
        
        for item in self.randomized_set:
            if not index:
                return item
            index -= 1
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()