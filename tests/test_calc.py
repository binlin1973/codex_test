import pytest

from src.calc import add, sub


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-4, 6, 2),
        (2.5, 0.5, 3.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (-3, -6, 3),
        (4.5, 0.5, 4.0),
    ],
)
def test_sub(a, b, expected):
    assert sub(a, b) == expected


@pytest.mark.parametrize(
    "a,b",
    [
        ("1", "2"),
        ("3", 4),
        (object(), 1),
    ],
)
def test_add_rejects_non_numeric(a, b):
    with pytest.raises(TypeError):
        add(a, b)


@pytest.mark.parametrize(
    "a,b",
    [
        ("5", "1"),
        (7, "8"),
    ],
)
def test_sub_rejects_non_numeric(a, b):
    with pytest.raises(TypeError):
        sub(a, b)
