from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        dis = float("inf")
        for index,(pointX,pointY) in enumerate(points):
            if pointX==x or pointY ==y:
                pre = abs(pointX-x)+abs(pointY-y)
                if pre< dis:
                    dis = pre
                    ans = index
        return ans

if __name__ == '__main__':
    points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    x=3
    y=4
    test = Solution()
    print(test.nearestValidPoint(x, y, points))