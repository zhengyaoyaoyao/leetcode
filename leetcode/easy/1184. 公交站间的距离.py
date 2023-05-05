from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        #简单办法先做
        if start>destination:
            return self.distanceBetweenBusStops(distance,destination,start)
        forStartToEnd = 0
        for i in distance[start:destination]:
            forStartToEnd+=i
        forEndTostart=0
        for k in distance[destination:]:
            forEndTostart+=k
        for j in distance[:start]:
            forEndTostart+=j
        return min(forEndTostart,forStartToEnd)
class Solution2:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        #再python中有sum函数直接求和
        if start>destination:
            start,destination=destination,start
        return min(sum(distance[start:destination]),sum(distance[destination:])+sum(distance[:start]))