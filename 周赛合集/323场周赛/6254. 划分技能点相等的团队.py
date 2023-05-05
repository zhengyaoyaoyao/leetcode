from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        count = skill[0]+skill[-1]
        ans = 0
        while left<right:
            if skill[left]+skill[right]!=count:
                return -1
            else:
                ans+=skill[left]*skill[right]
            left+=1
            right-=1
        return ans
if __name__ == '__main__':
    skill = [1,1,2,3]
    test = Solution()
    print(test.dividePlayers(skill))
