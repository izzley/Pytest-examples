import pytest


def a():
    raise AttributeError

def test_attribute():
    with pytest.raises(AttributeError):
        a()


# https://docs.pytest.org/en/6.2.x/getting-started.html#run-multiple-tests
# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x
    # this one passes because str has "lower" function
    def test_two(self):
        x = "hello"
        assert hasattr(x, "lower")

    # this one fails because str doesn't have "check" function
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")