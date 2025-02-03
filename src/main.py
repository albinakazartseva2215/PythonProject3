from src.processing import sort_by_date
from src.search import get_transactions
from src.transactions import read_transactions_from_csv, read_transactions_from_excel
from src.utils import get_path_to_file
from src.widget import get_date, mask_account_card

result_json = get_path_to_file("../data/operations.json")
result_csv = read_transactions_from_csv("../src/transactions.csv")
result_excel = read_transactions_from_excel("../src/transactions_excel.xlsx")


def choice_file(input_file):
    """Функция предназначена для выбора файла"""
    if input_file:
        if input_file == "1":
            result_file = result_json
            print("Для обработки выбран JSON-файл")
            return result_file

        elif input_file == "2":
            result_file = result_csv
            print("Для обработки выбран CSV-файл")
            return result_file

        elif input_file == "3":
            result_file = result_excel
            print("Для обработки выбран EXCEL-файл")
            return result_file


def get_revers_date(choice_category, input_sort_date, input_revers_date):
    """Функция предназначена для фильтрации данных по дате (возрастание или убывание)"""
    if input_sort_date:
        if input_revers_date == "ПО ВОЗРАСТАНИЮ":
            result_date_revers = sort_by_date(choice_category, revers=False)
            return result_date_revers
        elif input_revers_date == "ПО УБЫВАНИЮ":
            result_date_revers = sort_by_date(choice_category, revers=True)
            return result_date_revers


def filter_rub(filter_revers_date, input_filter_rub):
    """Функция предназначена для фильтрации данных по RUB"""
    if input_filter_rub == "ДА":
        result = get_transactions(filter_revers_date, "RUB")
        return result
    else:
        result = filter_revers_date
        return result


def filter_word(filter_revers_date, input_filter_word):
    """Функция предназначена для фильтрации данных по любому слову"""
    if input_filter_word == "ДА":
        input_word = input("Ведите слово для фильтрации\n")
        result = get_transactions(filter_revers_date, input_word)
        return result
    elif input_filter_word == "НЕТ":
        return filter_revers_date


def get_result(result_transaction: list) -> None:
    """Вывод результатов по отфильтрованному списку транзакций"""
    if len(result_transaction) == 0:
        print("Нет ни одной транзакции")
    else:
        print(f"Всего банковских операций в выборке: {len(result_transaction)}\n")

        for transaction in result_transaction:
            date = get_date(transaction.get("date"))

            try:
                card_from_mask = mask_account_card(transaction["from"])
                print(f"{date} {transaction["description"]} {card_from_mask} -> ", end="")
            except KeyError:
                print(f"{date} {transaction["description"]} ", end="")
            except AttributeError:
                print(f"{date} {transaction["description"]} ", end="")

            card_to_mask = mask_account_card(transaction["to"])
            try:
                amount = transaction["amount"]
            except KeyError:
                amount = transaction["operationAmount"]["amount"]
            try:
                currency = transaction["currency_name"]
            except KeyError:
                currency = transaction["operationAmount"]["currency"]["name"]
            print(f"{card_to_mask} Сумма: {amount} {currency}")


def main():
    input_file = (
        input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
                            Выберите необходимый пункт меню:\n
                            1. Получить информацию о транзакциях из JSON-файла\n
                            2. Получить информацию о транзакциях из CSV-файла\n
                            3. Получить информацию о транзакциях из XLSX-файла\n"""
        )
    ).upper()

    result_file = choice_file(input_file)

    input_status = (
        input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
                            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        )
    ).upper()

    choice_category = get_transactions(result_file, input_status)

    print(f"Операции отфильтрованы по статусу {input_status}")

    input_sort_date = (input("Отсортировать операции по дате? Да/Нет\n")).upper()
    input_revers_date = (input("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n")).upper()
    filter_revers_date = get_revers_date(choice_category, input_sort_date, input_revers_date)

    input_filter_rub = (input("Выводить только рублевые тразакции? Да/Нет\n")).upper()

    result_filter_rub = filter_rub(filter_revers_date, input_filter_rub)

    input_filter_word = (input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")).upper()

    result_transaction = filter_word(result_filter_rub, input_filter_word)

    print("Распечатываю итоговый список транзакций...")
    if result_transaction:
        get_result(result_transaction)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    print(main())
