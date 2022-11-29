class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.nums.append(val)
        self.indices[val] = len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        last_val = self.nums[-1]
        val_idx = self.indices[val]
        self.nums[val_idx] = last_val
        self.indices[last_val] = val_idx
        self.nums.pop()
        self.indices.pop(val, 0)
        return True

    def getRandom(self) -> int:
        return self.nums[randint(0, len(self.nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()