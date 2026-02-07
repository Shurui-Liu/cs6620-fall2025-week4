"""Simple calculator module.

Provides basic arithmetic operations and a small demo when run directly.
"""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two numbers.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operation: str, num1: float, num2: float) -> float:
    """Perform a calculation based on the operation string.

    Args:
        operation: One of 'add', 'subtract', 'multiply', 'divide'.
        num1: First operand.
        num2: Second operand.

    Returns:
        The result of the operation.

    Raises:
        ValueError: If the operation is unknown.
    """
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    func = operations.get(operation)
    if func is None:
        raise ValueError(f"Unknown operation: {operation}")

    return func(num1, num2)


def main() -> None:
    """Run a small demo of the calculator."""
    print("Simple Calculator")
    print("-" * 20)

    result1 = calculate("add", 10, 5)
    print(f"10 + 5 = {result1}")

    result2 = calculate("multiply", 7, 3)
    print(f"7 * 3 = {result2}")

    print("Calculator completed successfully!")


if __name__ == "__main__":
    main()
