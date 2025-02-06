import getpass
from functions  import create_user
from functions import generate_password  # Импортируем функцию генерации пароля

def main():
    print("⚙️  ВНИМАНИЕ! Если проигрывайте этот скрипт локально, то помните, что на сервере А и Б уже должен быть root c % 10.0.0.0/255.0.0.0")

    # Сервер А (источник данных)
    host_a = input("Введите хост сервера A (источник): ")
    admin_user_a = input("Имя администратора (Enter для 'root'): ") or "root"
    admin_password_a = getpass.getpass("Введите пароль администратора сервера A: ")
    database_a = input("Введите имя базы данных на сервере A: ")

    # Создаем пользователя sender на сервере A
    sender_password = "StaticPassword123!"
    create_user(host_a, admin_user_a, admin_password_a, "sender", sender_password, database_a)
    print("Пользователь sender на сервере А создан")

if __name__ == "__main__":
    main()
