from src.masks import get_mask_card_number, get_mask_account

# Вводим номер карты
card_number = input("Введите номер карты: ")

# Вызываем функцию и выводим замаскированный номер карты
print(get_mask_card_number(card_number))

# Вводим номер счета
account_number = input("Введите номер счета ")
# Вызываем функцию и выводим замаскированный номер счета
print(get_mask_account(account_number))
