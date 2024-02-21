class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.validate()
        if self.numerator == self.denominator:
            print("Число целое")
        else:
            print("Число не целое")

    def input_fraction(self):
        self.numerator = int(input("Введите числитель: "))
        self.denominator = int(input("Введите знаменатель: "))
        self.validate()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def validate(self):
        if self.denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")

# t = Fraction
# t.input_fraction
# print(t)