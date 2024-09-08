def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    return f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    return f"**{account_number.strip()[-4:]}"
