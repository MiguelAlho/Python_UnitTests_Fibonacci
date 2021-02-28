# Python_UnitTests_Fibonacci
A sample unit tested project implementing a fibonacci sequence to demo the motions of TDD.

## using the repo

Clone the repo and install the dependencies:

```
pip install -U virtualenv
pip install pytest
pip install pytest-cov
```

Use a virtual environment if you prefer (But it's still a foreign concept to me!).

To run the tests:

```
pytest tests/
```

Or, with coverage:

```
pytest --cov-report term-missing --cov=src tests/
```

## completed solution for the excercise

A complete, step by step (commit-by-commit version is setup in the demo branch). You can see the changes perfomed throughout the motions.


## Premise

So, you've been asked to build a python module that can calculate the Nth value of the Fibonacci sequence. Recall that the Fibonacci sequence is produced by adding the previous two numbers in the sequence, that starts with 0 and 1:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

At this point in time in the overall project, all that has been asked is for this. Maybe in the future more features may be necessary, but you're not sure. It's really YAGNI at the moment.

