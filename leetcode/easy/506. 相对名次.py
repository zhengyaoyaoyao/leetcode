import heapq
from typing import List


class Solution1:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        copyScore = score[:]
        scoreDit =dict()
        heapq.heapify(copyScore)
        ans = []
        for i in range(n):
            scoreDit[heapq.heappop(copyScore)] = n-i
        for x in score:
            if scoreDit[x] == 1:
                ans.append("Gold Medal")
            elif scoreDit[x] == 2:
                ans.append("Silver Medal")
            elif scoreDit[x] == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(scoreDit[x]))
        return ans

'''
在python中直接用元组其实更快
'''
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        desc = ["Gold Medal","Silver Medal","Bronze Medal"]
        ans=[""]*len(score)
        # 创建一个排序好的元组记录了从大到小的信息
        arr = sorted(enumerate(score),key=lambda x:-x[1])
        for i,(idx,_) in enumerate(arr):
            #ans[idx]就是把原本的填进去
            ans[idx]= desc[i] if i<3 else str(i+1)
        return ans

if __name__ == '__main__':
    test = Solution()
    score = [10,3,8,9,4]
    print(test.findRelativeRanks(score))