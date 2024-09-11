from src.masks import get_mask_account, get_mask_card_number

from src.widget import mask_account_card

from src.widget import get_date



# Вводим номер карты
card_number = input("Введите номер карты: ")

# Вызываем функцию и выводим замаскированный номер карты
print(get_mask_card_number(card_number))

# Вводим номер счета
account_number = input("Введите номер счета ")
# Вызываем функцию и выводим замаскированный номер счета
print(get_mask_account(account_number))

input_data = input("Введите информацию о карте или счете: ")
# Вводим информацию о карте или счете
print(mask_account_card(input_data))

date_input = "2024-09-11T02:26:18.671407"
formatted_date = get_date(date_input)
print(formatted_date)
