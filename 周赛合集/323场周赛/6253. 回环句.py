class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        split = sentence.split(" ")
        for i,value in enumerate(split):
            if i!=len(split)-1 and split[i][-1] ==split[i+1][0]:
                continue
            elif i==len(split)-1 and split[i][-1]==split[0][0]:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    s= "Leetcode is cool"
    test =Solution()
    print(test.isCircularSentence(s))