"""単純な計算モジュール（Phase 4 検証用のダミー）。"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # Fixed bug: previously performed addition instead of multiplication.
    return a * b


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value


def divide(a, b):
    """Return a / b. If b is zero, return None instead of raising ZeroDivisionError."""
    if b == 0:
        return None
    return a / b
