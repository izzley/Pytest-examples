# https://realpython.com/pytest-python-testing/

# test_with_pytest.py

def test_always_passes():
    assert True

def test_logical_numeracy():
    assert 1 > -1

def test_always_fails():
    good_example = False
    # Cannot assert False statement. This is a test
    assert not good_example

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }