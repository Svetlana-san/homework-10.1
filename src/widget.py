from src.masks import get_mask_card_number


def mask_account_card(data_card: str) -> str:
    """Фильтрует данные, оставляя только цифры"""
    number_card = "".join(el for el in data_card if el.isdigit())
    # Определение ввода - карта или счет
    if "Visa" in data_card or "MasterCard" in data_card or "Maestro" in data_card:
        # Если это карта
        number_card_mask = get_mask_card_number(number_card)
    elif "Счет" in data_card:
        # Если это счет
        number_card_mask = "**" + number_card[-4:]

    # Извлечение имени карты/счета
    name_card = "".join(el if not el.isdigit() else "" for el in data_card).strip()
    data_card_mask = name_card + " " + number_card_mask
    return data_card_mask


def get_date(date_string: str) -> str:
    """Функция, преобразовывающая вывод даты"""
    # Разделяем строку на компоненты
    date_part = date_string.split("T")[0]
    # Извлекаем только дату (до 'T')
    year, month, day = date_part.split("-")
    # Разделяем дату на год, месяц и день

    # Форматируем в нужный вид "ДД.ММ.ГГГГ"
    formatted_date = f"{day}.{month}.{year}"

    return formatted_date


if __name__ == "__main__":
    date_input = "2024-09-11T02:26:18.671407"
    formatted_date = get_date(date_input)
    print(formatted_date)
