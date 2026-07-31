def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def division(a, b):
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("cannot divide by 0")
    return a / b
