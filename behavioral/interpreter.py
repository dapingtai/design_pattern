from abc import ABC, abstractmethod

# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self, context: dict) -> bool:
        pass

# Terminal Expression
class VariableExpression(Expression):
    def __init__(self, name: str):
        self.name = name

    def interpret(self, context: dict) -> bool:
        return context.get(self.name, False)

# Non-terminal Expression for AND
class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context: dict) -> bool:
        return self.expr1.interpret(context) and self.expr2.interpret(context)

# Non-terminal Expression for OR
class OrExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2

    def interpret(self, context: dict) -> bool:
        return self.expr1.interpret(context) or self.expr2.interpret(context)

# Non-terminal Expression for NOT
class NotExpression(Expression):
    def __init__(self, expr: Expression):
        self.expr = expr

    def interpret(self, context: dict) -> bool:
        return not self.expr.interpret(context)

def main():
    # The context (variables and their values)
    context = {"x": True, "y": False}

    # Create expressions
    x = VariableExpression("x")
    y = VariableExpression("y")
    not_y = NotExpression(y)
    x_and_not_y = AndExpression(x, not_y)

    # Interpret expressions
    print(f"x = {x.interpret(context)}")
    print(f"y = {y.interpret(context)}")
    print(f"not y = {not_y.interpret(context)}")
    print(f"x and (not y) = {x_and_not_y.interpret(context)}")

    # Create and interpret a more complex expression: (x OR y) AND (NOT y)
    complex_expression = AndExpression(
        OrExpression(x, y),
        not_y
    )
    print(f"(x OR y) AND (NOT y) = {complex_expression.interpret(context)}")

if __name__ == "__main__":
    main()