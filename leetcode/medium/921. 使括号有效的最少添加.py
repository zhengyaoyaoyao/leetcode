class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while "()" in s:
            s = s.replace("()","")
        return len(s)

'''
使用得分的方法进行求解
'''
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        score,ans = 0,0
        for c in s:
            score += 1 if c=='(' else -1
            # 小于0就是右括号多了，这是一定无法匹配的。所以得分归零。相当于只要多了一个右括号就ans+1
            if score<0:
                score = 0
                ans +=1
        return ans +score



if __name__ == '__main__':
    s = "())"
    test = Solution()
    print(test.minAddToMakeValid(s))