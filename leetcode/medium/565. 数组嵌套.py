from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = set()
        maxSize = 0
        for val in nums:
            currentVal = val
            foot=0
            while currentVal not in ans:
                foot+=1
                ans.add(currentVal)
                currentVal=nums[currentVal]
            maxSize = max(foot,maxSize)
        return maxSize

'''
从题的理解，你会发现从某个点出发会得到一张有向图，不同顶点出发可能会有不同的有向图，那么我们实际上就是判断有向图的顶点多少
因为条件的终止是相等的时候，所以必然是一个环，我们可以用vis数组来表示是否访问过。
所以考点：图的遍历DFS或者BFS
'''
class Solution2:
    def arrayNesting(self, nums: List[int]) -> int:
        maxSize= 0
        n= len(nums)
        vis =[False]*n #判断是否访问过
        for i in range(n):
            currentFoot=0
            '''
            这里其实把我的set改成了数组的形式。元素个数还是那么多个，如果访问过了就为True，反正都再那个环中
            '''
            while not vis[i]:
               vis[i]= True
               i = nums[i]
               currentFoot+=1
            maxSize=max(currentFoot,maxSize)
        return maxSize

'''
再次优化！
我们必须有一个同样大小的数组或者set去标记是否遍历过，那其实我们可以直接再原有的数组上修改。没必要浪费那个空间（前提是原数组可以改）
'''
class Solution3:
    def arrayNesting(self, nums: List[int]) -> int:
        maxSize,n=0,len(nums)
        for i in range(n):
            currentFoot= 0
            #为什么用这个判断条件，因为我们如果遍历到了把它设为n那么其实就表示已经出界了。就是访问过了，同理设为-1也是一样的
            while nums[i]<n:
                num = nums[i]
                nums[i]=n
                i= num
                currentFoot+=1
            maxSize=max(currentFoot,maxSize)
        return maxSize


if __name__ == '__main__':
    A = [5, 4, 0, 3, 1, 6, 2]
    test = Solution()
    print(test.arrayNesting(A))
