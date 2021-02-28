# Tutorial steps

## Context

So, you've been asked to build a python module that can calculate the Nth value of the Fibonacci sequence. Recall that the Fibonacci sequence is produced by adding the previous two numbers in the sequence, that starts with 0 and 1:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

At this point in time in the overall project, all that has been asked is for this. Maybe in the future more features may be necessary, but you're not sure. It's really YAGNI at the moment.

## Before you start coding:

So, you think about the requirement and consider that maybe a class would be useful, with an `Nth()` method that can return the value in the sequence for the index passed in. You're thinking that the single, integer input parameter would suffice, representing the index in the sequence. In this case, the index is to be zero-based. So:

| index | value |
|-------|-------|
| 0     | 0     |
| 1     | 1     |
| 2     | 1     |
| 3     | 2     |
| 4     | 3     |
| 5     | 5     |
| 6     | 8     |
| 7     | 13    |
| 8     | 21    |
| 9     | 34    |
| 10    | 55    |
| ...   | ...   |

You also know that the formula to get the next value is F(n) = F(n-1) + F(n-2);

## Creating the initial test

In the `tests` folder, create a new test file: `test_fibonacci.py`.

It seems the easiest way to get started is to pick the first value pair on the table and get going, based on the decision above. That means you'll need to create the test file and method that tests that. As a starting point, it'll help setup files, classes and method definition, and get us going with the test suite. Start simple.

With the file created, let's fill it in with the minimum we can use, defining our first test:

```
def test_nth_fibonacci_for_0_is_0():
    #arrange
    calculator = FibonacciCalculator()
    #act
    result = calculator.Nth(0)
    #assert
    assert result == 0
```

This is a basic test. We define the test method as a method prefixed with `test_`. The test method name gives us a good indication of our expectation. It's not a complete test suite, but it is one individual test that makes sense to us.

Let's run the tests:
```
pytest tests/
```

And see our output:
```
=========================================================================================================================== test session starts ===========================================================================================================================
platform win32 -- Python 3.9.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\gh\pyFibonacci
plugins: cov-2.11.1
collected 1 item                                                                                                                                                                                                                                                           

tests\test_fibonacci.py F                                                                                                                                                                                                                                            [100%]

================================================================================================================================ FAILURES =================================================================================================================================
______________________________________________________________________________________________________________________ test_nth_fibonacci_for_0_is_0 ______________________________________________________________________________________________________________________

    def test_nth_fibonacci_for_0_is_0():
        #arrange
>       calculator = FibonacciCalculator()
E       NameError: name 'FibonacciCalculator' is not defined

tests\test_fibonacci.py:3: NameError
========================================================================================================================= short test summary info =========================================================================================================================
FAILED tests/test_fibonacci.py::test_nth_fibonacci_for_0_is_0 - NameError: name 'FibonacciCalculator' is not defined
============================================================================================================================ 1 failed in 0.17s ============================================================================================================================
```

Tests are RED. We've got errors as expected, sincve we are excercising a class and method we haven't yet implemented. That's our first sign of what we need to do, so let's get to work on that.

### Create the fibonacci class

Create the Fibonacci class file at `src/finbonacci.py` and fill it with the minimal implementation that coudl pass the test:

```
class FibonacciCalculator():
    def Nth(self, ordinal):
        return 0
```

test test file will need to import the class so add the missing header in the test file:

```
from src.fibonacci import FibonacciCalculator

(...)
```

And run the tests with `pytest tests/`: 

```
=========================================================================================================================== test session starts ===========================================================================================================================
platform win32 -- Python 3.9.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\gh\pyFibonacci
plugins: cov-2.11.1
collected 1 item                                                                                                                                                                                                                                                           

tests\test_fibonacci.py .                                                                                                                                                                                                                                            [100%]

============================================================================================================================ 1 passed in 0.07s ============================================================================================================================
```

Tests are now green! We've got our first test in and one of the conditions - 0th index returns 0 - is implemented (event though it is not the complete solution).

Time to commit!

### Add another test

There is another test condition that is not based on a sum - the value with an index of 1. Let's test and implement that case. In the test file, add a new test method:

```
def test_nth_fibonacci_for_1_is_1():
    calculator = FibonacciCalculator()
    result = calculator.Nth(1)
    assert result == 1
```

And run the tests:

```
=========================================================================================================================== test session starts ===========================================================================================================================
platform win32 -- Python 3.9.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\gh\pyFibonacci
plugins: cov-2.11.1
collected 2 items                                                                                                                                                                                                                                                          

tests\test_fibonacci.py .F                                                                                                                                                                                                                                           [100%]

================================================================================================================================ FAILURES =================================================================================================================================
______________________________________________________________________________________________________________________ test_nth_fibonacci_for_1_is_1 ______________________________________________________________________________________________________________________

    def test_nth_fibonacci_for_1_is_1():
        calculator = FibonacciCalculator()
        result = calculator.Nth(1)
>       assert result == 1
E       assert 0 == 1

tests\test_fibonacci.py:14: AssertionError
========================================================================================================================= short test summary info =========================================================================================================================
FAILED tests/test_fibonacci.py::test_nth_fibonacci_for_1_is_1 - assert 0 == 1
======================================================================================================================= 1 failed, 1 passed in 0.26s =======================================================================================================================
```

Of the 2 tests, one is failing, as expected, since we haven't implemented a complete fibonacci, and the current one only covers the 0 index. Let's make this one pass. Modify the implementation using a simple implementation based on ifs:


```
class FibonacciCalculator():
    def Nth(self, ordinal):
        if ordinal == 1:
            return 1
        return 0
```

And run the tests again. They now pass! Time for a new commit.

## index 2 requires the sum

Add the next test:

```
def test_nth_fibonacci_for_2_is_1():
    calculator = FibonacciCalculator()
    result = calculator.Nth(2)
    assert result == 1
```
 
 And run to confirm the failure. It's important to have a failure when we start since we know we haven't covered the case. By having a failure at this point, we know our test is valid.  The counter axample would be to imagine that our fibonacci implementation were the following:

 ``` 
 class FibonacciCalculator():
    def Nth(self, ordinal):
        if ordinal == 0:
            return 0
        return 1
```

This code would pass on all the tests, even though the implementation for 2 would be incorrect, as it is not summing. It would be a false positive. We should always look into having a failing test to be sure the test is valid.

let's implement the case as we wan't it:

```
class FibonacciCalculator():
    def Nth(self, ordinal):
        if ordinal == 0:
            return 0
        if ordinal == 1:
            return 1
        return self.Nth(ordinal-1) + self.Nth(ordinal-2)

```

And run the tests. All passes. Let's add an extra test on a higher number since we are aware of the false positive.:

```
def test_nth_fibonacci_for_10_is_55():
    calculator = FibonacciCalculator()
    result = calculator.Nth(10)
    assert result == 55
```

runnning the tests we have 4 tests covering a good amount. Lets check on coverage, too:

```
pytest --cov-report term-missing --cov=src tests/
```

```
=========================================================================================================================== test session starts ===========================================================================================================================
platform win32 -- Python 3.9.2, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: C:\gh\pyFibonacci
plugins: cov-2.11.1
collected 4 items                                                                                                                                                                                                                                                          

tests\test_fibonacci.py ....                                                                                                                                                                                                                                         [100%]

----------- coverage: platform win32, python 3.9.2-final-0 -----------
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
src\__init__.py        0      0   100%
src\fibonacci.py       7      0   100%
------------------------------------------------
TOTAL                  7      0   100%


============================================================================================================================ 4 passed in 0.25s ============================================================================================================================
```

We've got 100% code coverage meaning every single production code line is hit at least once in the test suite. We're exercising all our code (but not necessarily every possible case).

Time to commit!

## Time to Refactor

We've got working code and working tests, but that doesn't mean the jobe is done. We should look into cleaning up and refactoring what we've done. The big advantage is that since we now have tests in place, we can make changes and understand if we've broken something.

### Idiomatic python - method name.

As a C# developer, I'm used to seeing capitilized method names. In Python, seems there is a preference for lowercased names. Let's refactor that. 

In the `fibonacci.py` file, using VScode, place the cursor on the `Nth` method name and hit F2. Rename the method to `nth` (lover-case n).

Since we've made a change (even a simple one with the help of the IDE), let's run the tests to make sure everything is ok.

In my case, because I didn't also save the test file on the refactor, tests failed. Save it, rerun tests, everything now OK.

Commit!





