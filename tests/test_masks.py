import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number() -> list[int]:
    return [7000792289606361, 7000792289606362]


@pytest.mark.parametrize("card_number, expected", [(7000792289606361, "7000 79** **** 6361")])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_invalid_length_mask_card_number():
    with pytest.raises(ValueError):
        get_mask_card_number(card_number=700079228960636)


def test_get_without_mask_card_number():
    with pytest.raises(TypeError):
        get_mask_card_number(card_number=[])


def test_get_invalid_type_mask_card_number(A000792289606361=None):
    with pytest.raises(TypeError):
        get_mask_card_number(card_number=A000792289606361)


@pytest.fixture
def account():
    return 73654108430135874305


@pytest.mark.parametrize("account, expected", [(73654108430135874305, "**4305")])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


def test_get_mask_account_invalid_length():
    with pytest.raises(ValueError):
        get_mask_account(account=736541084301358743056)


def test_get_mask_account_invalid_type(A3654108430135874305=None):
    with pytest.raises(TypeError):
        get_mask_account(account=A3654108430135874305)

