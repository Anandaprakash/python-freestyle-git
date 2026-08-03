import pytest

from app.calculator import multiply, division

@pytest.mark.smoke
def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(-2, 4) == -8

@pytest.mark.regression
def test_division():
    assert division(10, 2) == 5
    assert division(7.5, 2.5) == 3.0

@pytest.mark.regression
def test_division_by_zero_raises():
    with pytest.raises(ValueError, match="cannot divide by 0"):
        division(5, 0)
        
@pytest.mark.regression
def test_divide_by_zero():
    with pytest.raises(ValueError, match="cannot divide by 0"):
        division(10, 0)