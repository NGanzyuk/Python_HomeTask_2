import re

from Exceptions import CalcError
from calculator import Calculator

Operations = {'+': (1, "__add__"), '-': (1, "__sub__"),
              '*': (2, "__mul__"), '/': (2, "__div__")}


def evaluate(formula):
    def parse(expression):
        parsed_exp = re.split(r'\s+', expression)

        for i in range(len(parsed_exp)):
            if i == 0 and (parsed_exp[i] in Operations or parsed_exp[i] == ")"):
                raise CalcError(CalcError.ret_wrong_input() + expression)
            try:
                yield float(parsed_exp[i])
            except ValueError:
                if parsed_exp[i] in Operations or parsed_exp[i] in "()":
                    if i >= 1 and (parsed_exp[i - 1] in Operations or parsed_exp[i - 1] == "("):
                        raise CalcError(CalcError.ret_wrong_input() + expression)
                    else:
                        yield parsed_exp[i]
                else:
                    raise CalcError(CalcError.ret_wrong_input() + expression)

    def to_polish(parsed):
        stack = []
        for elem in parsed:
            if elem in Operations:
                while stack and stack[-1] != "(" and Operations[elem][0] <= Operations[stack[-1]][0]:
                    yield stack.pop()
                stack.append(elem)
            elif elem == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif elem == "(":
                stack.append(elem)
            else:
                yield elem
        while stack:
            yield stack.pop()

    def calculate(polish):
        stack = []
        for elem in polish:
            if elem in Operations:
                y, x = stack.pop(), stack.pop()
                calculator = Calculator(x, y)
                method = getattr(Calculator, Operations[elem][1])
                stack.append(method(calculator))
            else:
                stack.append(elem)
        return float_or_int(stack[0])

    def float_or_int(x):
        if int(x) == x:
            return int(x)
        else:
            return x

    return calculate(to_polish(parse(formula)))
