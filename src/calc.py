from numbers import Number


def _ensure_numeric(*values: object) -> None:
    """Ensure every provided value is a numeric type."""
    if not all(isinstance(value, Number) for value in values):
        raise TypeError("calc operations require numeric arguments")


def add(a, b):
    _ensure_numeric(a, b)
    return a + b


def sub(a, b):
    _ensure_numeric(a, b)
    return a - b
