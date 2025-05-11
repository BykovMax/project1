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
