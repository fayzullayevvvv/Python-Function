def is_strong_password(password: str) -> bool:
    return True if len(password) > 8 else False

print(is_strong_password('python123'))