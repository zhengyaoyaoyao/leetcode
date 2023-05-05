from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans =[]
        for i in arr:
            if i not in ans:
                ans.append(i)
        #此时ans是一个不重复的列表
        ans.sort()
        ansMap={}
        for index,val in enumerate(ans):
            ansMap[val]=index+1
        #此时ansMap里面是键：值
        ans.clear()
        for i in arr:
            ans.append(ansMap.get(i))
        return ans
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks ={v:i for i,v in enumerate(sorted(set(arr)),1)}
        return [ranks[v] for v in arr]
if __name__ == '__main__':
    test = Solution()
    arr = [100,100,100]
    print(test.arrayRankTransform(arr))


