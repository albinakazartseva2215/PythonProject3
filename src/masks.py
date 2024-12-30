def get_mask_card_number(card_number: int) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску
    :rtype: object
    """
    if not isinstance(card_number, int):
        raise TypeError("Ошибка ввода данных")

    if len(str(card_number)) == 16:
        return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"

    raise ValueError("Неправильный номер карты")


def get_mask_account(account: int) -> str:
    """Функция get_mask_account принимает на вход номер счета и возвращает его маску"""
    if not isinstance(account, int):
        raise TypeError("Ошибка ввода данных")

    if len(str(account)) == 20:
        return f"**{str(account)[-4:]}"

    raise ValueError("Неправильный номер счета")



if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
