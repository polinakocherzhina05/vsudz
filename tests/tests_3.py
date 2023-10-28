import pytest
from dz.three import notsame


@pytest.mark.parametrize(
    ('x'),
    [
        [True, 1],
        [555]
    ]
)
def test(x):
    assert notsame(x) is True


@pytest.mark.parametrize(
    ('x'),
    [
        [1, 1],
        [1, 2, 5, 1]
    ]
)
def testf(x):
    assert notsame(x) is False