class FibonacciCalculator():
    def nth(self, ordinal):
        if ordinal <= 1:
            return ordinal
        return self.nth(ordinal-1) + self.nth(ordinal-2)
