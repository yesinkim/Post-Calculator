from parser import CalculatorParser


if __name__ == '__main__':
    parser = CalculatorParser()
    test_case = ["1+2"]#, "2-1"]#, "1+2", "1/2", "(1.2+1)*2)/3-3"]
    for case in test_case:
        print(parser.tokenize(case))
        print('----------------------------------------')
        tree = parser.parse(case)
    
        tree.print_tree_()
        print(tree.evaluate())


# Tree.left에 있는 NonTerminal token이 문제일수도 있다..!