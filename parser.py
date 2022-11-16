import re
from typing import List

from exceptions import InvalidExpressionError, InvalidTokenError
from tokens import (BaseToken, NonTerminalToken, NumberToken, OperatorToken,
                    ParenToken)
from tree import (BaseTree, EnclosedTree, ExpressionTree, FactorsTree,
                  
                  FactorTree, IncrementsTree, IncrementTree, ScalingsTree,
                  ScalingTree, TermTree)


class CalculatorParser():
    """Parse expression and show and calculate the result"""
    def __init__(self):
        pass

    def tokenize(self, expression: str) -> List[BaseToken]:
        """parse the expression and return list consist of token"""
        tokens = []
        split_expression = re.findall(r"[0-9.]+|[\+\-\*\/\(\)]", expression)
        for token in split_expression:
            if NumberToken.is_valid(token):
                tokens.append(NumberToken(token))

            elif OperatorToken.is_valid(token):
                tokens.append(OperatorToken(token))

            elif ParenToken.is_valid(token):
                tokens.append(ParenToken(token))
                
            else:
                raise InvalidTokenError(f"{expression} is not a valid token")
        return tokens

    def parse(self, expression: str):
        self.tokens = iter(self.tokenize(expression))
        self.current_token = next(self.tokens, None)
        self.next_token = next(self.tokens, None)

        result = self.expression()
        return result

    def is_accept(self, type: str) -> bool:
        return self.current_token and self.current_token.type == type

    def advance(self):
        self.current_token = self.next_token
        self.next_token = next(self.tokens, None)

    def expression(self) -> BaseTree:
        """Expr -> Term Increments"""
        tree = ExpressionTree(NonTerminalToken("Expression"))
        tree.insert(self.term())
        tree.insert(self.increments())
        return tree

    def term(self) -> TermTree:
        """Term -> Factor Scales"""
        tree = TermTree(NonTerminalToken("Term"))
        tree.insert(self.factors())
        tree.insert(self.scalings())
        return tree

    def factors(self) -> FactorsTree:
        """Factors -> factor | -factor"""
        tree = FactorsTree(NonTerminalToken("Factors"))
        if self.is_accept("Number") or self.is_accept("LParen"):
            tree.insert(self.factor())

        elif self.is_accept("Sub"):
            tree.insert(self.current_token)
            self.advance()
            tree.insert(self.factor())

        else:
            raise InvalidExpressionError(f"Should not arrive here {self.current_token}")
        return tree

    def factor(self) -> FactorTree:
        """Factor -> Number | Enclosed"""
        tree = FactorTree(NonTerminalToken("Factor"))
        if self.is_accept("Number"):
            tree.insert(self.current_token)
            self.advance()      # advance to next token

        elif self.is_accept("LParen"):
            tree.insert(self.enclosed())
        
        else:
            raise InvalidExpressionError(f"Should not arrive here {self.current_token}")
        return tree

    def enclosed(self) -> ExpressionTree:
        """Enclosed -> ( Expr )
        Enclosed는 반드시 current_token이 LParen일 때만 호출되어야 한다.
        """
        self.advance()
        expr_value = self.expression()
        if self.is_accept("RParen"):
            self.advance()

        else:
            raise InvalidExpressionError(f"Should not arrive here {self.current_token}")
        return expr_value

    def scalings(self) -> ScalingsTree:
        """Scalings -> Scalings Scaling | epsilon"""
        tree = ScalingsTree(NonTerminalToken("Scalings"))
        if self.is_accept("Mul") or self.is_accept("Div"):
            tree.insert(self.scaling())
            tree.insert(self.scalings())
        return tree

    def scaling(self) -> ScalingTree:
        """Scaling -> MulOp Factors
        scaling은 여기밖에 사용하지 않기 때문에 MulOp인지 확인하지 않아도 된다."""
        if self.is_accept("Mul") or self.is_accept("Div"):
            tree = ScalingTree(NonTerminalToken("Scaling"))
            tree.insert(self.mul_operator())
            tree.insert(self.factors())
            return tree

    def mul_operator(self) -> OperatorToken:
        """MulOp -> * | /"""
        if self.is_accept("Mul") or self.is_accept("Div"):      # 넣어도 되고 안 넣어도 된다. 확장성/유지보수성을 위해 넣는다.
            token = self.current_token
            self.advance()
            return token

    def increments(self) -> IncrementsTree:
        """Increments -> Increment Increments | epsilon"""
        tree = IncrementsTree(NonTerminalToken("Increments"))
        if self.is_accept("Add") or self.is_accept("Sub"):
            tree.insert(self.increment())
            tree.insert(self.increments())
        return tree

    def increment(self) -> IncrementTree:
        """Increment -> AddOp Term"""
        if self.is_accept("Add") or self.is_accept("Sub"):
            tree = IncrementTree(NonTerminalToken("Increment"))
            tree.insert(self.add_operator())
            tree.insert(self.term())
            return tree

    def add_operator(self) -> OperatorToken:
        """AddOp -> + | -"""
        if self.is_accept("Add") or self.is_accept("Sub"):      # 넣어도 되고 안 넣어도 된다. 확장성/유지보수성을 위해 넣는다.
            token = self.current_token
            self.advance()
            return token