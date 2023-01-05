class RandomizedSet:

    def __init__(self):
        self.pos = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            last_val = self.nums[-1]
            val_idx = self.pos[val]
            self.pos[last_val] = val_idx
            self.nums[val_idx] = last_val
            self.nums.pop()
            self.pos.pop(val)
            return True
        return False
    
    def getRandom(self) -> int:
        return self.nums[randint(0, len(self.nums)-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()