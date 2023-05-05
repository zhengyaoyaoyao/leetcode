import collections


class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = collections.deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        if len(self.deque)!=self.deque.maxlen:
            self.deque.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) != self.deque.maxlen:
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.deque)!=0:
            self.deque.popleft()
            return True
        return False


    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return not len(self.deque)

    def isFull(self) -> bool:
        return len(self.deque)==self.deque.maxlen

