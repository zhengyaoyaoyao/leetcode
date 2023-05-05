"""
O(n^2)看数据范围猜算法
每次操作结束后，剩下的还是一个子串（一个完整的字符串）
又可以对子串进行同样的操作 => 子问题 =>dp
f[i] = 操作s[i:] 所需要的最大操作次数。（从后往前统计）（相当于逆向迭代）
所以结果就是:f[0]的值

f[i] =f[i+j]+1, if s[i:i+j] == s[i+j:i+2*j]
f[i] = 1
取max

重点放在怎么快速判断两个子串是否相同上.
lcp 两个后缀的最长公共前缀
lcp[i][j] = s[i:] 和 s[j:] 的最长公共前缀

s[i:i+j] ==s[i+j:i+2*j]
等价于 lcp[i][i+j] >=j

lcp[i][j] = lcp[i+1][j+1] +1 if s[i] ==s[j]
          =  0               else s[i] !=s[j]
"""

class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        #这个lcp表格就记录了所有的从i和j开始的公共前缀。
        lcp = [[0] *(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] ==s[j]:
                    lcp[i][j] =lcp[i+1][j+1] +1

        f = [0]*n
        for i in range(n-1,-1,-1):
            # i+2*j<= n
            # j<= (n-i)//2
            for j in range(1,(n-i)//2+1):
                # 只要两个公共前缀大于j那么就取最大的。
                if lcp[i][i+j]>=j:
                    f[i] = max(f[i],f[i+j])
            f[i] +=1
        return f[0]

'''
以下做法错误.
'''
class Solution:
    def deleteString(self, s: str) -> int:
        def sub(s:str,flag) ->int:
            if s is None or flag==False:
                return -1
            index = 0
            for i in range(1,len(s)//2+1):
                flag=False
                if s[:i]==s[i:i+i]:
                    index=i
                    flag=True
                    break
            record = s[index:]
            res = ""
            for i in record:
                res+=i
            return 1+sub(res,flag)
        count = 1+sub(s,True)
        return count

if __name__ == '__main__':
    s = "aaaaa"
    test = Solution()
    print(test.deleteString(s))