class Solution:
    def partitionString(self, s: str) -> int:
        res=0
        cur = list()
        for i in range(len(s)):
            if s[i] in cur:
                res+=1
                cur.clear()
                cur.append(s[i])
            if s[i] not in cur:
                cur.append(s[i])
            if len(cur)==1 and i==(len(cur)-1):
                res+=1
        return res

'''
1. 第一个字串至多可以有多长
2. 去掉第一个字串，剩下的部分就变成了一个子问题
'''
class Solution:
    def partitionString(self, s: str) -> int:
        #因为你本身就至少有1的长度如果都不重复
        ans =1
        vis = set()
        for i ,c in enumerate(s):
            if c in vis:
                vis.clear()
                ans+=1
            vis.add(c)
        return ans

if __name__ == '__main__':
    test = Solution()
    # s = "abacaba"
    s = "ssssss"
    print(test.partitionString(s))