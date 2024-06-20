class Calculator:
    def add(self, a, b):
      if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Custom Error: Input must be Numeric")
      return a + b


    def minus(self, a, b):
      if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Custom Error: Input must be Numeric")
      return a - b
      