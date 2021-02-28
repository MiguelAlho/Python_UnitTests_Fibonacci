class FibonacciCalculator():
    def Nth(self, ordinal):
        if ordinal == 0:
            return 0
        if ordinal == 1:
            return 1
        return self.Nth(ordinal-1) + self.Nth(ordinal-2)