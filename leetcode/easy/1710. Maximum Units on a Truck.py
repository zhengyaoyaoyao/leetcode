'''
贪心策略：
我们要最大的单元格，所以对单元排序

'''
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        ans = 0
        for i in range(len(boxTypes)):
            if truckSize-boxTypes[i][0]>=0:
                truckSize = truckSize-boxTypes[i][0]
                ans+=boxTypes[i][0]*boxTypes[i][1]
            else:
                ans+=truckSize*boxTypes[i][1]
                break
        return ans


if __name__ == '__main__':
    boxTypes =[[5,10],[2,5],[4,7],[3,9]]
    test =Solution()
    print(test.maximumUnits(boxTypes,10))