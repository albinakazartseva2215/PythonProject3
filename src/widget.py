import typing
from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция mask_account_card умеет обрабатывать информацию как о картах, так и о счетах.
    Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером."""
    type_ = []
    digit_ = []
    for char in account_card:
        if char.isdigit():
            digit_.append(char)
        else:
            type_.append(char)

    type_card = "".join(type_)
    digit_card = "".join(digit_)

    if len(digit_card) == 16:
        mask_digit_card = (get_mask_card_number(int(digit_card)))
        return f"{type_card} {mask_digit_card}"
    elif len(digit_card) == 20:
        mask_digit_card = (get_mask_account(int(digit_card)))
        return f"{type_card} {mask_digit_card}"
    elif len(digit_card) != 16 or len(digit_card) != 20:
        raise ValueError("Неправильные данные карты или счета")


def get_date(date_str: str, format: object = "%d.%m.%Y") -> str:
    """Функция get_date, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    if date_str:
        if format:
            date_string = date_str[0:10]
            date_str_split = date_string.split("-")
            new_date = ".".join(date_str_split[::-1])
            new_date_time = datetime.strptime(new_date, "%d.%m.%Y")
            date_object = new_date_time.strftime(format)
            return date_object
        else:
            raise TypeError("Неправильный формат даты")
    raise ValueError("Введите правильную строку с датой")


print(mask_account_card("Visa Platinum 7000792289606361"))
print(get_date("2024-03-11T02:26:18.671407"))
