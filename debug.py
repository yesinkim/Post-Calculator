Operators = set(['+', '-', '*', '/', '(', ')'])  # collection of Operators

Priority = {'+':1, '-':1, '*':2, '/':2} # dictionary having priorities of Operators
 
 
def infixToPostfix(expression): 

    stack = [] # initialization of empty stack

    output = '' 

    

    for character in expression:    # expression을 돌면서

        if character not in Operators:  # if an operand append in postfix expression

            output+= character

        elif character=='(':  # else Operators push onto stack

            stack.append('(')

        elif character==')':

            while stack and stack[-1]!= '(':

                output+=stack.pop()

            stack.pop()

        else: 
            # stack에 있는 것과 가장 최근에 담긴 것이 "("이 아니면서 해당 character의 우선순위가 stack[-1]에 있는 것보다 작으면
            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:

                output+=stack.pop()

            stack.append(character)

    while stack:

        output+=stack.pop()

    return output


expression = input('Enter infix expression:')
print('infix notation:',expression)
print('postfix notation:',infixToPostfix(expression))