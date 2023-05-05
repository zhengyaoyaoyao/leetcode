from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0]*len(boxes)
        for i in range(len(boxes)):
            sumNum = 0
            for j in range(len(boxes)):
                if boxes[j]=='1' and i!=j:
                   sumNum+=abs(j-i)
            ans[i]=sumNum
        return ans
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left,right,operations = int(boxes[0]),0,0
        for i in range(1,len(boxes)):
            if boxes[i]=='1':
                right+=1
                operations+=i
        ans=[operations]
        for i in range(1,len(boxes)):
            operations+=left-right
            if boxes[i]=='1':
                left+=1
                right-=1
            ans.append(operations)
        return ans

if __name__ == '__main__':
    boxes = "110"
    test =Solution()
    print(test.minOperations(boxes))
