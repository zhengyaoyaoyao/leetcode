class StockSpanner:

    def __init__(self):
        self.stack=[]
    def next(self, price: int) -> int:
        #每天都有自己的一个权重
        weight=1
        while self.stack and price >= self.stack[-1][0]:
            #把第i天的事情pop了，然后把weight这个权重加给了自身存入栈。
            weight+=self.stack.pop()[1]
        self.stack.append((price,weight))
        return weight

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == '__main__':
    test = StockSpanner()
    print(test.next(100))
    print(test.next(80))
    print(test.next(60))
    print(test.next(70))
    print(test.next(60))
    print(test.next(75))
    print(test.next(85))