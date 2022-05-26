from db_and_files import Server
import pytest


def test_read_from_json_file():
    expected_result = {
        "a": 100,
        "1": 500.01,
        "@": False,
        "false": "hello"
    }

    test_file = 'read_test_file.json'
    test_data = Server.read_from_json_file(test_file)

    assert test_data == expected_result

def test_get_bd_data():
    expected_cards = [('1234 5678 9010', '1234'), ('1009 8765 4321', '4321')]
    expected_phones = ['+375(33)670-17-49', '+375(29)123-45-67']

    test_cards, test_phones = Server.get_bd_data()

    for card_data in test_cards:
        assert card_data in expected_cards

    for phone_data in test_phones:
        assert phone_data in expected_phones