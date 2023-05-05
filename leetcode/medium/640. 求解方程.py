class Solution:
    def solveEquation(self, equation: str) -> str:
        factor= val = 0
        i,n,sign =0,len(equation),1 #灯饰左边默认系数为正，到等号右边就变成负号
        while i <n:
            if equation[i] =='=':
                sign =-1
                i+=1
                continue
            s = sign #每次遍历都要知道是否到等号右边，在左边就是正得
            if equation[i] =='+': #去掉前面符号，读取数字
                i+=1
            elif equation[i] =='-':
                s= -s
                i+=1
            num,valid =0,False
            #因为不一定就一位数，所以要读取数据,这一段就是数据得读取
            while i<n and equation[i].isdigit():
                valid = True
                num = num*10+int(equation[i])
                i+=1
            if i<n and equation[i] =='x': #变量得系数
                factor += s*num if valid else s
                i+=1
            else:#数值
                val +=s*num
        if factor ==0:
            return "No solution" if val else "Infinite solutions"
        return f"x={-val//factor}"
