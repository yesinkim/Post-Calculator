from parser import CalculatorParser


if __name__ == '__main__':
    parser = CalculatorParser()
    test_case = ["1+1", "1-1", "1+2", "1/2", "(1.2+*1)*2)/3-3"]
    for case in test_case:
        print(parser.tokenize(case))
        # tree = parser.parse(case):
        # tree.print_tree()