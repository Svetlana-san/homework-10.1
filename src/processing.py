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
