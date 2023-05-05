from typing import List





class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        res = logs[0][0]
        maxValue = logs[0][1]
        for i in range(1,len(logs)):
            id = logs[i][0]
            spend = logs[i][1]-logs[i-1][1]
            if spend>maxValue:
                maxValue=spend
                res = id
            elif spend ==maxValue and res>id:
                res = id
        return res

if __name__ == '__main__':
    n = 10
    logs = [[0, 3], [2, 5], [0, 9], [1, 15]]
    test = Solution()
    print(test.hardestWorker(n,logs))