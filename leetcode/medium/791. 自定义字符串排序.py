import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        val =collections.defaultdict(int)
        for i , ch in enumerate(order):
            val[ch]  = i+1
        return "".join(sorted(s,key=lambda ch :val[ch]))