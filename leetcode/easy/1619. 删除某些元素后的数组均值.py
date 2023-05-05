from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        deleteNum = int(len(arr)*0.05)
        arr.sort()
        arr = arr[deleteNum:-deleteNum]
        return sum(arr)/len(arr)


if __name__ == '__main__':
    arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
    test = Solution()
    print(test.trimMean(arr))