import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return collections.Counter(s) == collections.Counter(t)
        return sorted(s)==sorted(t)
if __name__ == '__main__':
    s="1231111"
    counter = collections.Counter(s)
    for i in counter.items():
        print(i)
