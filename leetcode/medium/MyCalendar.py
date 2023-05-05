class MyCalendar:

    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        if self.books == []:
            self.books.append([start,end])
            return True
        for loc in self.books:
            if loc != []:
                if not ( (start<loc[0] and end<=loc[0] and start<loc[1] and end<loc[1]) or (start>=loc[0] and end>=loc[0] and start>=loc[1] and end>=loc[1])):
                    return False
        self.books.append([start, end])
        return True

if __name__ == '__main__':
    test= MyCalendar()
    print(test.__init__())
    print(test.book(47,50))
    print(test.book(33,41))
    print(test.book(39,45))
    print(test.books)
# ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
# [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]