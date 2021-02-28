from src.fibonacci import FibonacciCalculator

def test_nth_fibonacci_for_0_is_0():
    #arrange
    calculator = FibonacciCalculator()
    #act
    result = calculator.Nth(0)
    #assert
    assert result == 0