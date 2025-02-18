import string
import secrets
def generate_password(length=12):
    """Генерирует безопасный пароль из букв, цифр и спецсимволов."""
    return ''.join(secrets.choice(string.printable.strip()) for _ in range(length))
