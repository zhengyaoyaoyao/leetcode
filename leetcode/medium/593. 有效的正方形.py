from typing import List

#正方形的判断可以用6条边，对角线相等，四条边相等即可。
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def is_Square(p1: List[int], p2: List[int], p3: List[int], p4: List[int]):
            #默认p1和p3是对角进行
            l12 = (p2[1]-p1[1])**2+(p2[0]-p1[0])**2
            l23 = (p3[1]-p2[1])**2+(p3[0]-p2[0])**2
            l34 = (p4[1] - p3[1]) ** 2 + (p4[0] - p3[0]) ** 2
            l41 = (p4[1] - p1[1]) ** 2 + (p4[0] - p1[0]) ** 2
            l13 =(p3[1] - p1[1]) ** 2 + (p3[0] - p1[0]) ** 2
            l24 =(p4[1] - p2[1]) ** 2 + (p4[0] - p2[0]) ** 2
            if l12 == l23 == l34 ==l41 and l13 ==l24 and l13 !=0 and l24!=0:
                return True
            else:
                return False
        return is_Square(p1,p2,p3,p4) or is_Square(p1,p2,p4,p3) or is_Square(p1,p3,p2,p4)

if __name__ == '__main__':
    p1 = [1,1]
    p2 = [5, 3]
    p3 = [3, 5]
    p4 = [7, 7]
    test= Solution()
    print(test.validSquare(p1,p2,p3,p4))
