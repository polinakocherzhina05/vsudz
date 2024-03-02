import pytest
from ten.d import IrreducibleFraction

    
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
    b = IrreducibleFraction(numerator, denominator)
    assert b.numerator == expected_numerator
    assert b.denominator == expected_denominator