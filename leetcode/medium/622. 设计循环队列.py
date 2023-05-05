class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*(k+1)
        self.font=0
        self.rear=0
        self.length=k+1
    def enQueue(self, value: int) -> bool:
        # 入队要看有没有满
        if self.isFull():
            return False
        self.queue[self.rear]=value
        self.rear=(self.rear+1+self.length)%self.length
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.font = (self.font+1+self.length)%self.length
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.font]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear-1)%self.length]

    def isEmpty(self) -> bool:
        return self.font == self.rear

    def isFull(self) -> bool:
        return (self.rear+1+self.length)%self.length==self.font


