import bank
import pytest


@pytest.mark.parametrize("test_pin, test_true_pin", [('1234', '1234'), ('0909', '0909'), ('4444', '4444')])
def test_true_pin(test_pin, test_true_pin):
    assert bank.Bank.check_pin(test_pin, test_true_pin)


@pytest.mark.parametrize("test_pin, test_true_pin", [('1234', '@@@@'), ('0909', '9090'), ('aaaaa', '4444')])
def test_false_pin(test_pin, test_true_pin):
    assert bank.Bank.check_pin(test_pin, test_true_pin) == False 

@pytest.mark.parametrize("test_store, expected_result", [
    ({'1': 5, '10': 3}, 35),
    ({'100': 50, '20': 5}, 5100),
    ({'5': 1, '10': 0}, 5),
    ({'200': 1, '2': 1}, 202),
])
def test_get_all_sum(test_store, expected_result):
    assert bank.Bank.get_all_sum(test_store) == expected_result

@pytest.mark.parametrize("test_cash", [50, 100, 1, 200])
def test_true_get_money(test_cash):
    test_bank = bank.Bank()
    test_bank.atm.storage.fund = {
        '1': 10,
        '2': 20,
        '5': 50,
        '50': 100,
        '100': 1
    }

    assert test_bank.atm.storage.get_money(test_cash)

@pytest.mark.parametrize("test_cash", [-50, 10000000000000, 9.9999])
def test_false_get_money(test_cash):
    test_bank = bank.Bank()
    test_bank.atm.storage.fund = {
        '1': 10,
        '2': 20,
        '5': 50,
        '50': 100,
        '100': 1
    }

    assert test_bank.atm.storage.get_money(test_cash) == False 