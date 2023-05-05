import collections
from typing import List

'''
当合并的条件有很多的时候，注意反过来思考，不要一味的找合并条件
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans =[]
        intervals=sorted(intervals)
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans
if __name__ == '__main__':
    intervals =[[1,4],[0,4]]
    # intervals=sorted(intervals)
    # print(intervals)
    test = Solution()
    print(test.merge(intervals))
