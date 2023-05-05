from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for i in range(len(items)):
            if ruleKey == "type":
                if items[i][0] == ruleValue:
                    res+=1
            elif ruleKey == "color":
                if items[i][1] == ruleValue:
                    res+=1
            else:
                if items[i][2]==ruleValue:
                    res+=1
        return res


if __name__ == '__main__':
    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    test = Solution()
    print(test.countMatches(items,ruleKey,ruleValue))