class FibonacciCalculator():
    def nth(self, ordinal):
        if ordinal == 0:
            return 0
        if ordinal == 1:
            return 1
        return self.nth(ordinal-1) + self.nth(ordinal-2)
