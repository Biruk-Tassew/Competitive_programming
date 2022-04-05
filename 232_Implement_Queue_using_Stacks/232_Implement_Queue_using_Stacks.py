class MyQueue:
    def __init__(self):
        self.stackOne = []
        self.stackTwo = []
    
    def push(self, x: int) -> None:
        while self.stackTwo:
            self.stackOne.append(self.stackTwo.pop())
        self.stackOne.append(x)

    def pop(self) -> int:
        if len(self.stackOne)==0:
            return self.stackTwo.pop()
        else:
            while len(self.stackOne) > 0:
                self.stackTwo.append(self.stackOne.pop())
                
        return self.stackTwo.pop()
        

    def peek(self) -> int:

        if len(self.stackOne)==0:
            return self.stackTwo[-1]
        else:
            while len(self.stackOne) > 0:
                self.stackTwo.append(self.stackOne.pop())
                
        return self.stackTwo[-1]

    def empty(self) -> bool:
        return len(self.stackOne)==0 and len(self.stackTwo)==0
