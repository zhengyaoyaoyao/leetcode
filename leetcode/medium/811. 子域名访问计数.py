from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = dict()
        for i in cpdomains:
            curArr = i.split(" ")
            rep = int(curArr[0])
            url = curArr[1]
            urlArr= url.split(".")
            s = urlArr[-1]
            if s not in ans.keys():
                ans[s] = rep
            else:
                ans[s] +=rep
            for j in range(len(urlArr)-2,-1,-1):
                s = urlArr[j]+"."+s
                if s not in ans.keys():
                    ans[s]=rep
                else:
                    ans[s]+=rep
        res = []
        for key in ans.keys():
            curS = str(ans[key])+" "+key
            res.append(curS)
        return res

if __name__ == '__main__':
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    test = Solution()
    print(test.subdomainVisits(cpdomains))