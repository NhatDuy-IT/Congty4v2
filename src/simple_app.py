"""
Simple calculator module for Git practice exercises.

Functions:
- add(a, b)
- sub(a, b)
- mul(a, b)
- div(a, b) -> raises ZeroDivisionError on division by zero

This small module is intentionally straightforward so you can edit it
in branches, run tests, and practice commits/merges.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def sub(a, b):
    """Return a minus b."""
    return a - b


def mul(a, b):
    """Return a multiplied by b."""
    return a * b


def div(a, b):
    """Return a divided by b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def main():
    """Simple CLI when run as a script. Usage: python -m src.simple_app add 1 2"""
    import sys

    if len(sys.argv) < 4:
        print("Usage: python -m src.simple_app <add|sub|mul|div> x y")
        return 1

    op = sys.argv[1]
    try:
        x = float(sys.argv[2])
        y = float(sys.argv[3])
    except ValueError:
        print("x and y must be numbers")
        return 1

    ops = {"add": add, "sub": sub, "mul": mul, "div": div}
    if op not in ops:
        print(f"Unknown operation: {op}")
        return 1

    try:
        result = ops[op](x, y)
    except ZeroDivisionError as e:
        print("Error:", e)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
