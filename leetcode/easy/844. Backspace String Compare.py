'''
方案一：
用两个str去接这个改变后的结果
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s:str)-> str:
            ans = []
            for i in range(len(s)):
                if s[i] !='#':
                    ans.append(s[i])
                elif s[i]=='#' and ans:
                    ans.pop()
                else:
                    continue
            return ''.join(ans)
        return process(s)==process(t)

'''
方案二：双指针
'''


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1

        return True

class Solution:
    def backspaceCompare(self,s:str,t:str) -> bool:
        indexS = len(s)-1
        indexT = len(t)-1
        skipS = skipT=0
        while indexS>=0 or indexT>=0:
            # 处理s的#号字符
            while indexS >=0:
                if s[indexS] =='#':
                    skipS+=1
                    indexS-=1
                elif skipS>0:
                    skipS-=1
                    indexS-=1
                else:
                    break
            # 同理处理t的
            while indexT >=0:
                if t[indexT] =='#':
                    skipT+=1
                    indexT-=1
                elif skipT>0:
                    skipT-=1
                    indexT-=1
                else:
                    break
            if indexS >=0 and indexT >=0:
                if s[indexS]!=t[indexT]:
                    return False
            elif indexS>=0 or indexT >=0:
                return False
            indexS-=1
            indexT-=1
        return True



if __name__ == '__main__':
    s= []
    s.pop()
