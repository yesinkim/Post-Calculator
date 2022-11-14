from parser import CalculatorParser


if __name__ == '__main__':
    parser = CalculatorParser()
    test_case = ["1+1", "1-1", "1+2", "1/2", "(1.2+*1)*2)/3-3"]
    for case in test_case:
        print(parser.tokenize(case))
        tree = parser.parse(case)
        tree.print_tree()

# 디버깅중인데 빼먹은 거 왜 이렇게 많냐...!?