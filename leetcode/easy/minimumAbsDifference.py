from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()

        best, ans = float('inf'), list()
        for i in range(n - 1):
            delta = arr[i + 1] - arr[i]
            if delta < best:
                best = delta
                ans = [[arr[i], arr[i + 1]]]
            elif delta == best:
                ans.append([arr[i], arr[i + 1]])
        return ans