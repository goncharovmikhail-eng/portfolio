import getpass
from functions import create_user, generate_password, append_mysql_config, check_mysql_connection

def main():
    print("⚙️  Начало настройки миграции пользователей MySQL/MariaDB\n")

    # Сервер A (локальный)
    host_a = "localhost"
    admin_user_a = input("Имя администратора (Enter для 'root'): ") or "root"
    admin_password_a = getpass.getpass("Введите пароль администратора сервера A: ")
    database_a = input("Введите имя базы данных на сервере A: ")

    # Создаем пользователя sender на сервере A
    sender_password = "StaticPassword123!"
    create_user(host_a, admin_user_a, admin_password_a, "sender", sender_password, database_a)
    print("Пользователь sender на сервере А создан")

    # Дополняем ~/.my.cnf для удобного подключения
    append_mysql_config("clientA", "sender", sender_password, host_a)
    print("Конфигурация clientA добавлена в ~/.my.cnf")

    check_mysql_connection("A")

if __name__ == "__main__":
    main()
