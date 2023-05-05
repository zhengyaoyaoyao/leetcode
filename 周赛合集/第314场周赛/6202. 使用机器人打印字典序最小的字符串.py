import collections
import string
'''
思路一样，差距在出栈的代码
'''
class Solution:
    def robotWithString(self, s: str) -> str:
        ans=[]
        # cnt的作用就是取最小的一个字符到底是谁，遍历过一个字符就删去一个字符，然后看第一个非零的字符是谁，就是谁
        cnt = collections.Counter(s)
        min=0 # 剩余的最小字母
        stack=[]
        # 每次都会找到一个c，也每次都会找到c后面的最小值。反正就添加，如果添加的这个值比后面小，那么就跳出。不然就加
        for c in s:
            cnt[c]-=1 # 遍历过了就删除
            while min<25 and cnt[string.ascii_lowercase[min]]==0:
                min+=1 # 就是从a开始找，不断地往后，如果非0就停止,这样就能找到最小值
            stack.append(c)
            while stack and stack[-1] <=string.ascii_lowercase[min]:
                ans.append(stack.pop())
        return ''.join(ans)



'''
错误的解答，在存入栈的过程和出栈过程没想明白，
思路没有问题，但是中间有卡壳，没想明白。
'''
class Solution:
    def robotWithString(self, s: str) -> str:
        mapAtoNum={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        sList = collections.deque()
        for i in s:
            sList.append(mapAtoNum[i])
        stack=[]
        ans=""
        while sList:
            curMin = 25
            minindex=0
            for i in range(len(sList)):
                if sList[i]<curMin:
                    minindex=i
                    curMin=sList[i]
            #找到最小值，然后不断的进栈中
            if stack:
                #如果栈不是空的
                while stack[-1]<sList[minindex] and stack:
                    ans +=chr(stack.pop()+97)
                    if len(stack)==0:
                        break
            else:
                #如果栈是空的
                for i in range(minindex+1):
                    stack.append(sList[i])
                for i in range(minindex+1):
                    sList.popleft()
        while stack:
            ans+=chr(stack.pop()+97)
        return ans



if __name__ == '__main__':
    s = "bydizfve"
    test = Solution()
    print(test.robotWithString(s))
    # print(chr(97))