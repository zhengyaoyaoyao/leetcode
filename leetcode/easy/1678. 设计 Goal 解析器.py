class Solution:
    def interpret(self, command: str) -> str:
        i  = 0
        ans = ""
        while i<len(command):
            if command[i]=="G":
                i+=1
                ans+="G"
            elif command[i] =="(":
                if command[i+1]==")":
                    ans+="o"
                    i=i+2
                else:
                    ans+="al"
                    i=i+4
        return ans
