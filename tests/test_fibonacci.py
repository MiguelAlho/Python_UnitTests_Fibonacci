from src.fibonacci import FibonacciCalculator
import pytest

@pytest.mark.parametrize("ordinal, expected", [
    (0, 0), 
    (1, 1), 
    (2, 1),
    (3, 2),
    (10,55)
])
def test_fibonacci_for_index_is_expected_value(ordinal, expected):
    calculator = FibonacciCalculator()
    result = calculator.nth(ordinal)
    assert result == expected

def test_fibonacci_raises_exception_for_negative_ordinal():
    with pytest.raises(ValueError):
        FibonacciCalculator().nth(-1)