from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_password_hash(password: str):
    """Функция для хеширования пароля"""
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Функция для проверки подлинности пароля"""
    return password_hash.verify(password, hashed_password)
