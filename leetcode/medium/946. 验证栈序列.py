from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [-1]*(len(popped))
        indexPop=0
        indexPush=0
        #栈顶指针
        index=0
        #扫描popped
        while indexPop<len(popped):
            if stack[index-1] == popped[indexPop]:
                indexPop+=1
                stack[index-1]=-1
                index-=1
            else:
                #因为已经入了的在push里面变成-1了，所以如果入了就-1，没入就没变。报错的情况是已经入了，那么就不再
                if popped[indexPop] not in pushed:
                    return False
                #下面这种情况就是还没入这个元素，那么就把他入进去
                for i in range(indexPush,len(pushed)):
                    stack[index]=pushed[i]
                    index+=1
                    pushed[i]=-1#说明已经进入栈过了。
                    if stack[index-1]==popped[indexPop]:
                        indexPush=i+1
                        break
        return True


'''
简化上述的思想：
方法其实都是让push进队，然后判断是否和pop相同，如果不同就继续进，如果相同就弹出去。但是上述设置的不精良
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        indexPop=0
        for valuePush in pushed:
            stack.append(valuePush)
            while stack and stack[-1]==popped[indexPop]:
                stack.pop()
                indexPop+=1
        return len(stack)==0


if __name__ == '__main__':
    pushed=[1,2,3,4,5]
    popped=[4,5,3,2,1]
    test = Solution()
    print(test.validateStackSequences(pushed,popped))