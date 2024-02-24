import pytest
from nine.a import Fraction
 

@pytest.mark.parametrize(
    ("numerator", "denominator"),
    [(5, 2), (1, 1), (3, 1)]
)
def test_str_representation(numerator, denominator):
    fraction = Fraction(numerator, denominator)
    if denominator == 1:
        expected_str = str(numerator)
    else:
        expected_str = f"{numerator}/{denominator}"
    assert str(fraction) == expected_str


@pytest.mark.parametrize(
    ("numerator", "denominator"),
    [(5, 2), (1, 1), (3, 1)]
)
def test_input_fraction(numerator, denominator):
    fraction = Fraction()    
    fraction.numerator = numerator
    fraction.denominator = denominator
    fraction.validate()


@pytest.mark.parametrize(
    ("numerator", "denominator"),
    [(1, 0), (2, 0)]
)
def test_validate_fraction(numerator, denominator):
    fraction = Fraction(numerator, denominator)
    with pytest.raises(ValueError):
        fraction.validate()


@pytest.mark.parametrize(
    ("numerator", "denominator"),
    [(5, 2), (1, 1), (3, 1)]
)
def __init__(numerator,denominator):
    f = Fraction(numerator, denominator)
    assert f.numerator == numerator
    assert f.denominator == denominator
