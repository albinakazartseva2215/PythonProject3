import typing
def filter_by_state(data_list: list[dict], state="EXECUTED") -> list[dict]:
    """Функция filter_by_state принимает список словарей и опционально значение для ключа state
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    if state:
        return [i for i in data_list if i["state"] == state]
    raise TypeError("Нет такого state в списке словарей")


def sort_by_date(datе_list: list[dict], revers:bool=True) -> list[dict]:
    """функцию sort_by_date принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date)"""
    if not datе_list:
        raise ValueError("Данные не введены")
    else:
        for i in datе_list:
            if i["date"]:
                sorted_date = sorted(datе_list, key=lambda x: x["date"], reverse=revers)
                return sorted_date

            raise TypeError("Неправильный формат даты")


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
             ],
            "EXECUTED",
        )
    )

    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                },
            ]
        )
    )
