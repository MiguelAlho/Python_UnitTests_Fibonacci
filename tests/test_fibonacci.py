from src.fibonacci import FibonacciCalculator

def test_nth_fibonacci_for_0_is_0():
    #arrange
    calculator = FibonacciCalculator()
    #act
    result = calculator.Nth(0)
    #assert
    assert result == 0

def test_nth_fibonacci_for_1_is_1():
    calculator = FibonacciCalculator()
    result = calculator.Nth(1)
    assert result == 1