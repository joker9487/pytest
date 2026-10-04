import pytest
from cart import validate_quantity
@pytest.mark.parametrize("quantity, expected", [
    (1, True),
    (0, False),
    (2, True),
    (98, True),
    (99,True),
    (100,False),
    (50,True),
    (15.5,False),
    (-1,False),
    ("5",False),
    (True, False),
    (None,False)
])
def test_validate_quantity(quantity,expected):
    assert validate_quantity(quantity) == expected
    