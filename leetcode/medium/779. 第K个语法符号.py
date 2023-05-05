import collections


'''
超时了，这是最基本的思想，这题很显然感觉可以用规律来做。
'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        queue = collections.deque()
        queue.append(0)
        i=1
        while i<n:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == 0:
                    queue.append(0)
                    queue.append(1)
                else:
                    queue.append(1)
                    queue.append(0)
            i+=1
        print(queue)
        return queue[k-1]
'''
规律：
1   0
2   01
3   0110
4   01101001

显然，前半部分和前一行一样，后面是前一半的取反。
'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k ==1:
            return 0
        if k>(1<<(n-2)):#1<<(n-2)就是2的n-2次方就是当前的一半
            return 1^self.kthGrammar(n-1,k-(1<<(n-2)))
        return self.kthGrammar(n-1,k)



if __name__ == '__main__':
    test = Solution()
    print(test.kthGrammar(2,1))