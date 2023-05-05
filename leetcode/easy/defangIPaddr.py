class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = address.replace('.',"[.]")
        return  res


if __name__ == '__main__':
    address = "1.1.1.1"
    test = Solution()
    print(test.defangIPaddr(address))