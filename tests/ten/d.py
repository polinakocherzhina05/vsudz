from ten.c import Fraction


class IrreducibleFraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
        self.reduce()
