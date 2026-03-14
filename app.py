import math


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def square_root(self, x):
        return math.sqrt(x)


class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width


if __name__ == "__main__":

    calculator = Calculator()
    geometry = GeometryCalculator()

    # Arithmetic operations
    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # Square root calculations
    num3 = 25
    num4 = 144
    num5 = 1000

    print(f"√{num3} = {calculator.square_root(num3)}")
    print(f"√{num4} = {calculator.square_root(num4)}")
    print(f"√{num5} = {calculator.square_root(num5)}")

    # Geometry calculations
    radius = 5
    length = 10
    width = 6

    print(f"The area of the circle with radius {radius} = {geometry.calculate_circle_area(radius)}")
    print(f"The area of the rectangle with length {length} and width {width} = {geometry.calculate_rectangle_area(length, width)}")
