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