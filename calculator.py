from Exceptions import CalcError


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self):
        return self.x + self.y

    def __sub__(self):
        return self.x - self.y

    def __mul__(self):
        return self.x * self.y

    def __div__(self):
        try:
            div = self.x / self.y
            return div
        except ZeroDivisionError:
            raise CalcError("На ноль делить нельзя")