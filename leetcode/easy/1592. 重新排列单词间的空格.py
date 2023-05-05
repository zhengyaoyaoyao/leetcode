class Solution:
    def reorderSpaces(self, text: str) -> str:
        result = text.split()
        space = text.count(" ")
        if len(result)<=1:
            return result[0]+" "*space
        jiange = len(result)-1
        jiangeNum = space//jiange
        tire = space%jiange
        ans = (' '*jiangeNum).join(result)+' '*tire
        return ans
if __name__ == '__main__':
    test = Solution()
    text = "  this   is  a sentence "
    words = text.split()
    print(test.reorderSpaces(text))