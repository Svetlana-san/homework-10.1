from datetime import datetime
from typing import Any


def filter_by_state(list_of_dictionaries: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """Фильтруем данные словарей по заданному состоянию"""
    list_state = []

    for item in list_of_dictionaries:
        if item.get("state") == state_id:
            list_state.append(item)
    return list_state


list_of_dictionaries = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "PENDING"},
    {"id": 3, "state": "EXECUTED"},
    {"id": 4, "state": "CANCELLED"},
]
filtered_list = filter_by_state(list_of_dictionaries)
print(filtered_list)


def (list_of_dictionaries: list[dict[str, Any]], revers: bool = True) -> list[dict[str, Any]]:
    """Сортируем список словарей по дате (по возрастанию или убыванию)"""
    sorted_list = sorted(
        list_of_dictionaries, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=revers
    )
    return sorted_list


list_of_dictionaries = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]


sorted_list = sort_by_date(list_of_dictionaries)
print(sorted_list)
