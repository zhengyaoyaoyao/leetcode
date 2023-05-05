import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        # need中统计了c的个数
        for c in t :
            need[c]+=1
        needCnt = len(t)
        start = 0
        res=(0,float('inf'))
        for end ,c in enumerate(s):
            # 一共needCnt个，如果减完了。那么说明那个right就是到right了。要动left了。
            if need[c]>0:
                needCnt-=1
            # 每个s的字符都会被need[c]减掉，可能不再里面的。
            need[c]-=1
            # 要开始动left了。
            if needCnt==0:
                while True:
                    c = s[start]
                    if need[c] ==0:
                        break
                    need[c]+=1
                    start+=1
                if end-start<res[1]-res[0]:
                    res=(start,end)
                need[s[start]]+=1
                needCnt+=1
                start+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]

if __name__ == '__main__':
    s="ADOBECODEBANC"
    t = "ABC"
    test = Solution()
    print(test.minWindow(s,t))