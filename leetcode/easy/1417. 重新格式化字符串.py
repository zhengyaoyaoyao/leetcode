import collections


class Solution:
    def reformat(self, s: str) -> str:
        digitArr=collections.deque()
        wordArr=collections.deque()
        i,numDigit,numWord=0,0,0
        while i <len(s):
            if s[i].isdigit():
                numDigit+=1
                digitArr.append(s[i])
                i+=1
            else:
                numWord+=1
                wordArr.append(s[i])
                i += 1
        #构建好两个数组
        if abs(numDigit-numWord)>1:
            return ""
        ans =""
        if numWord>numDigit:
            for i in range(len(s)):
                if i%2==0 and len(wordArr)>0:
                    ans+=wordArr.popleft()
                else:
                    ans+=digitArr.popleft()
        else:
            for i in range(len(s)):
                if i%2==0 and len(digitArr)>0:
                    ans += digitArr.popleft()
                else:
                    ans += wordArr.popleft()
        return ans

if __name__ == '__main__':
    s = "covid2019"
    test = Solution()
    print(test.reformat(s))