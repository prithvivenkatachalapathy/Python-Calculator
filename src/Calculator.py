def addition(a, b):
    return a + b

def subtraction(a, b):
            a = float(a)
            b = float(b)
            c = b - a
            return c

def multiplication(a, b):
    return a * b

def division(a, b):
    a = float(a)
    b = float(b)
    return round(b / a, 9)

def squarert(a):
    a = float(a)
    b = math.sqrt(a)
    c = float(b)
    return c

class Calculator:

    def __init__(self):
        x = 2 + 2
        self.result = x;
        pass

        def add(self, a, b):
            self.result = addition(a, b)
            return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def sqrt(self, a):
        self.result = squarert(a)
        return self.result



