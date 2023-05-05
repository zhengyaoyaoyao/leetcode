class MyCalendarTwo:

    def __init__(self):
        self.booked =[]
        # 多用一个来保存他们的交集
        self.overlaps=[]

    def book(self, start: int, end: int) -> bool:
        if any(current_start<end and current_end>start for current_start,current_end in self.overlaps):
            return False
        for current_start,current_end in self.booked:
            if start<current_end and end>current_start:
                self.overlaps.append((max(current_start,start),min(current_end,end)))
        self.booked.append((start,end))
        return True
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

if __name__ == '__main__':
    test = MyCalendarTwo()
    print(test.book(10,20))
    print(test.book(50,60))
    print(test.book(10,40))
    print(test.book(5,15))
    print(test.book(5,10))
    print(test.book(25,55))