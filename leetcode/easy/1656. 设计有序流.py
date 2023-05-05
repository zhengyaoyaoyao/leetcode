from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.keys=[""]*(n+1)
        self.ptr=1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.keys[idKey]=value
        res = []
        while self.ptr <len(self.keys) and self.keys[self.ptr]:
            res.append(self.keys[self.ptr])
            self.ptr+=1

        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)