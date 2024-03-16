class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator, self.denominator = self.validate(numerator, denominator)

    def reduce(self):
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def input_fraction(self):
        self.numerator, self.denominator = self.validate(*input(" ").split(" "))

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def validate(num, den):
        if den == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        if str(num).lstrip("-").isdigit() and str(den).lstrip("-").isdigit():
            return num, den
        raise ValueError("Неверный формат данных")

    def __add__(self, other):
        new_num = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        new_denom = self.denominator * other.denominator
        return self.__class__(new_num, new_denom)

    def __sub__(self, other):
        new_num = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        new_denom = self.denominator * other.denominator
        return self.__class__(new_num, new_denom)

    def __eq__(self, other):
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )


class IrreducibleFraction(Fraction):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
        self.reduce()


# f = Fraction(0, 2)
# f.reduce()
# print(f.denominator)
# print(f.numerator)
