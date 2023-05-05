from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index= {p[0]:i for i,p in enumerate(pieces)}
        i =0
        while i<len(arr):
            if arr[i] not in index:
                return False
            p = pieces[index[arr[i]]]
            if arr[i:i+len(p)] != p:
                return False
            i = i+len(p)
        return True

if __name__ == '__main__':
    arr =  [91,4,64,78]
    pieces =  [[78],[4,64],[91]]
    test = Solution()
    print(test.canFormArray(arr,pieces))