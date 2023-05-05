class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        index = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                index.append((i, s1[i]))
        s1Arr = list(s1)
        if len(index) != 2:
            return False
        else:
            s1Arr[index[0][0]] = index[1][1]
            s1Arr[index[1][0]] = index[0][1]
            return "".join(s1Arr) == s2


'''
看完官方解，所以为什么要交换？只要判断是不是相等即可。所以不用进行交换的步骤，只要拿出下标看下这两个地方是不是相互相等就行。
'''


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i = j = -1
        for index in range(len(s1)):
            if s1[index]!=s2[index]:
                if i < 0:
                    i = index
                elif j < 0:
                    j = index
                else:
                    return False
        return i < 0 or j >= 0 and s1[i] == s2[j] and s1[j] == s2[i]


if __name__ == '__main__':
    s1 = "bank"
    s2 = "kanb"
    test = Solution()
    print(test.areAlmostEqual(s1, s2))
