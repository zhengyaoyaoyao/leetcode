
def test():
    numbers = [30,12,2,7,996,16,31]
    operators = ["+","&","*","+","//"]
    ok = []
    for n1 in range(len(numbers)):
        for n2 in range(len(numbers)):
            for n3 in range(len(numbers)):
                for n4 in range(len(numbers)):
                    for o1 in range(len(operators)):
                        for o2 in range(len(operators)):
                            for o3 in range(len(operators)):
                                if (n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4) or (
                                        o1 == o2 or o2 == o3 or o1 == o3):
                                    continue
                                string = f"((({numbers[n1]}{operators[o1]}{numbers[n2]}){operators[o2]}{numbers[n3]}){operators[o3]}{numbers[n4]})"
                                if eval(string) == 1024:
                                    ok.append(string)

    print(ok)
if __name__ == '__main__':
    test()
    # print((((30|24)+2)**2))