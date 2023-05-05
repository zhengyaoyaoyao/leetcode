class Solution:
    def minOperations(self, s: str) -> int:
        s1, s2 = "", ""
        for i in range(len(s)):
            s1 += "1" if i % 2 == 0 else "0"
            s2 += "0" if i % 2 == 0 else "1"
        count1 = 0
        count2 = 0
        for i in range(len(s)):
            if s[i]!=s1[i]:
                count1+=1
            if s[i]!=s2[i]:
                count2+=1
        return min(count1,count2)

class Solution:
    def minOperations(self, s: str) -> int:
        n,cnt = len(s),0
        for i ,c in enumerate(s):
            cnt +=(ord(c)-ord('0'))^(i&1)
        return min(cnt,n-cnt)
if __name__ == '__main__':
    list =[0,1,0,0]
    for i in range(4):
        print(list[i]^(i&1))
