import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    filename="../logs/masks.log",
                    filemode="w", encoding="utf-8")

# Создаем логеры для различных компонентов программы
mask_loger = logging.getLogger("masks")


def get_mask_card_number(card_number: int) -> str:
    """Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску
    """
    mask_loger.debug("Начало работы функции по принятию номера карты")
    if not isinstance(card_number, int):
        mask_loger.error("Ошибка ввода данных карты")
        raise TypeError("Ошибка ввода данных")

    if len(str(card_number)) == 16:
        mask_loger.debug("Номер карты введен верно")
        return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"

    mask_loger.error("Неправильный номер карты")
    raise ValueError("Неправильный номер карты")


def get_mask_account(account: int) -> str:
    """Функция get_mask_account принимает на вход номер счета и возвращает его маску"""
    mask_loger.debug("Начало работы функции по принятию номера счета")
    if not isinstance(account, int):
        mask_loger.error("Ошибка ввода данных счета")
        raise TypeError("Ошибка ввода данных")

    if len(str(account)) == 20:
        mask_loger.debug("Номер счета введен верно")
        return f"**{str(account)[-4:]}"

    mask_loger.error("Неправильный номер счета")
    raise ValueError("Неправильный номер счета")



if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
    mask_loger.debug("Работа программы завершена")
