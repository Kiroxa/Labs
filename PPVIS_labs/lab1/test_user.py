from user import Phone
import pytest


@pytest.mark.parametrize("test_phone_number", ["+375(33)111-22-33", "+375(44)654-78-90", "+375(29)001-10-99"])
def test_true_phone_number(test_phone_number):
    assert Phone.check_phone_number(test_phone_number)


@pytest.mark.parametrize("test_phone_number", ["375(33)111-22-33", "+aaa(44)654-78-90", "+375()001-10-99", "+375()0011-1033-991", "+375()001_10_92"])
def test_false_phone_number(test_phone_number):
    assert Phone.check_phone_number(test_phone_number) == False