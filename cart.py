def validate_quantity(value):
    """
    購物車數量檢查：只接受整數 1~99
    合法回傳 True，不合法回傳 False
    """
    if not isinstance(value, int):
        return False
    if value >= 1 and value <= 99:
        return True
    return False