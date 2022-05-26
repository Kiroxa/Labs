from banknote import Banknote
import pytest


@pytest.mark.parametrize("value", ["1", "2", "5", "10", "20", "50", "100", "200"])
def test_true_validate(value):
    assert Banknote.validate(value)


@pytest.mark.parametrize("value", ["-1", "2.2", "55", "19", "2000000", "a", "Asd", "!223@"])
def test_false_validate(value):
    assert Banknote.validate(value) == False


def test_generate_fund():
    test_fund = Banknote.generate_fund()
    for key, value in test_fund.items():
        assert key in Banknote.values
        assert value == 0
