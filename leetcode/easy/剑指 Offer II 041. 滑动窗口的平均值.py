import collections


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window=collections.deque(maxlen=size)
        self.sum=0

    def next(self, val: int) -> float:
        if len(self.window)==self.window.maxlen:
            self.sum-= self.window.popleft()
        self.sum+=val
        self.window.append(val)
        return self.sum/len(self.window)