import pytest


@pytest.fixture
def number_card():
    return "7000792289606361"


@pytest.fixture
def number_account():
    return "73654108430135874305"


@pytest.fixture
def number_card_indication():
    return "Maestro 1596837868705199"


@pytest.fixture
def number_account_indication():
    return "Счет 64686473678894779589"


@pytest.fixture
def iso_date():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def mixed_state_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
