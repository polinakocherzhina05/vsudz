import pytest
import mock
import builtins
from ten.c import Fraction


@pytest.mark.parametrize(
    "numerator, denominator, expected_numerator, expected_denominator",
    [
        (6, 9, 2, 3),
        (8, 12, 2, 3),
        (15, 25, 3, 5),
        (-10, -15, 2, 3),
        (-2, 4, -1, 2),
        (6, -12, -1, 2),
        (0, 2, 0, 1)
    ],
)
def test_fraction_reduce(
    numerator, denominator, expected_numerator, expected_denominator
):
    fraction = Fraction(numerator, denominator)
    fraction.reduce()
    assert fraction.numerator == expected_numerator
    assert fraction.denominator == expected_denominator


@pytest.mark.parametrize(
    "numerator, denominator",
    [
        (1, 2),
        (2, 3),
        (10, 5),
        (-1, 2),
    ],
)
def test_init(numerator, denominator):
    fraction = Fraction(numerator, denominator)
    assert fraction.numerator == numerator
    assert fraction.denominator == denominator


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 5, 5),
        (5, 0, 5),
        (12, 8, 4),
        (17, 23, 1),
        (-12, 8, 4),
        (1, 5, 1),
        (5, 1, 1),
        (0, 0, 0),
    ],
)
def test_gcd(a, b, expected):
    assert Fraction.gcd(a, b) == expected


if __name__ == "__main__":
    pytest.main()


@pytest.mark.parametrize(
    ("num", "den", "res"),
    [
        (12, 12, "12/12"),
        (23, 121, "23/121"),
        (0, 1, "0/1"),
    ],
)
def test_str(num, den, res):
    a = Fraction(num, den)
    assert str(a) == res


@pytest.mark.parametrize(
    ("values", "ans"), [("12 21", "12/21"), ("1141 2142", "1141/2142"), ("0 1", "0/1")]
)
def test_input_digits(values, ans):
    a = Fraction()
    with mock.patch.object(builtins, "input", lambda _: values):
        a.input_fraction()
    assert str(a) == ans


@pytest.mark.parametrize(
    ("num", "den", "res"),
    [(12, 15, (12, 15)), (1, 12, (1, 12)), (12232, 213, (12232, 213))],
)
def test_validity(num, den, res):
    a = Fraction()
    assert a.validate(num, den) == res


def test_validity_exception():
    a = Fraction()
    with pytest.raises(ZeroDivisionError, match="Знаменатель не может быть равен нулю"):
        a.validate(1, 0)
    with pytest.raises(ValueError, match="Неверный формат данных"):
        a.validate("ewfmlkwje", "kl;afsnar")
