class FibonacciCalculator():
    def nth(self, ordinal):
        if ordinal < 0:
            raise ValueError("ordinal must be a positive integer")
        
        if ordinal <= 1:
            return ordinal
        return self.nth(ordinal-1) + self.nth(ordinal-2)
