class Solution:
    def reformatNumber(self, number: str) -> str:
        res=list()
        for ch in number:
            if ch.isdigit():
                res.append(ch)
        n, pt = len(res), 0
        ans = list()

        while n > 0:
            if n > 4:
                ans.append("".join(res[pt:pt + 3]))
                pt += 3
                n -= 3
            else:
                if n == 4:
                    ans.append("".join(res[pt:pt + 2]))
                    ans.append("".join(res[pt + 2:pt + 4]))
                else:
                    ans.append("".join(res[pt:pt + n]))
                break
        return "-".join(ans)


if __name__ == '__main__':
    number = "123 4-5678"
    test = Solution()
    print(test.reformatNumber(number))
