import pytest
from dz.one import swap



@pytest.mark.parametrize(
    ('pl', 'k', 'end'),
    [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2]),
        ([1, 2], 3, [2, 1])
    ]
)
def test(pl, k, end):
    assert swap(pl, k) == end