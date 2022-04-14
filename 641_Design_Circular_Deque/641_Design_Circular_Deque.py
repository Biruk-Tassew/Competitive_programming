class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [""]*k
        self.front = 0
        self.last = 0

    def insertFront(self, value: int) -> bool:
        if self.front < -1 * len(self.queue):
            self.front = 0
        if self.queue[self.front] == "":
            self.queue[self.front] = value
            return True
        else:
            if self.queue[self.front - 1] == "":
                self.queue[self.front - 1] = value
                self.front -= 1
                return True

        return False
    def insertLast(self, value: int) -> bool:
        if self.last > len(self.queue):
            self.last = 0
        if self.queue[self.last] == "":
            self.queue[self.last] = value
            return True
        else:
            if self.queue[self.last + 1] == "":
                self.queue[self.last + 1] = value
                self.last += 1
                return True

        return False

    def deleteFront(self) -> bool:
        if self.queue[self.front] != "":
            self.queue[self.front] = ""
            if self.queue[self.front + 1] != "":
                self.front += 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.queue[self.last] != "":
            self.queue[self.last] = ""
            if self.last > 0:
                if self.last == self.front:
                    self.front -= 1
                self.last -= 1
            elif self.last < 0:
                self.last -= 1
                
            else:
                if self.queue[-1] != "":
                    self.last -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.queue[self.front] != "":
            return self.queue[self.front]
        return -1

    def getRear(self) -> int:
        if self.queue[self.last] != "":
            return self.queue[self.last]
        return -1

    def isEmpty(self) -> bool:
        if self.queue[self.front] != "" or self.queue[self.last] != "":
            return False
        return True
    
    def isFull(self) -> bool:
        if "" in self.queue:
            return False
        return True
