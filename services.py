class MathService:
    def pow(self, base: int, exp: int) -> int:
        return base ** exp

    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return 1 if n == 0 else n * self.factorial(n - 1)

    def fibonacci(self, n: int) -> int:
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
