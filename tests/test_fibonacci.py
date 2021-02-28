from src.fibonacci import FibonacciCalculator

def test_nth_fibonacci_for_0_is_0():
    #arrange
    calculator = FibonacciCalculator()
    #act
    result = calculator.nth(0)
    #assert
    assert result == 0

def test_nth_fibonacci_for_1_is_1():
    calculator = FibonacciCalculator()
    result = calculator.nth(1)
    assert result == 1

def test_nth_fibonacci_for_2_is_1():
    calculator = FibonacciCalculator()
    result = calculator.nth(2)
    assert result == 1

def test_nth_fibonacci_for_10_is_55():
    calculator = FibonacciCalculator()
    result = calculator.nth(10)
    assert result == 55