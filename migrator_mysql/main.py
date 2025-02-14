import getpass
from functions import create_user, generate_password, append_mysql_config, check_mysql_connection

def main():
    print("Миграция бд.\nДанные для хоста A:")
    host_a = "localhost"
    user_a = "sender"
    range_ip = "%"
#    admin_user_a = input("Имя администратора (Enter для 'root'): ") or "root"
#    admin_password_a = getpass.getpass("Введите пароль администратора сервера A: ")
#    database_a = input("Введите имя базы данных на сервере A: ")
    # Создаем пользователя sender на сервере A
#    sender_password = "StaticPassword123!"
#    create_user(host_a, admin_user_a, admin_password_a, user_a, sender_password, database_a, range_ip)
#    print(f"Пользователь {user_a} на сервере А создан")
    # Добавляем креды от юзера в ~/.my.cnf
#    append_mysql_config("clientA", user_a, sender_password, host_a)
#    print("Конфигурация clientA добавлена в ~/.my.cnf")
#    print("Проверка группы А:\n")
#    check_mysql_connection("A")

    print("Данные для хоста B:\n")
    host_b = input("Введите IP удаленного MySQL сервера: ")
#    admin_user = input("Введите имя администратора (Enter для 'root'): ") or "root"
#    admin_password = getpass.getpass("Введите пароль администратора: ")
#    database_b = input("Введите имя базы данных: ")
    user_b = input("Введите имя нового пользователя: ")
    user_b_password = generate_password()
#    create_user(host_b, admin_user, admin_password, user_b, user_b_password, database_b, range_ip)
#    print(f"Пользователь {user_b} на сервере B создан")
    # Добавляем креды от юзера в ~/.my.cnf
    append_mysql_config("clientB", user_b, user_b_password, host_b)
    print("Конфигурация clientB добавлена в ~/.my.cnf")
    print("Проверка группы B:\n")
    check_mysql_connection("B")

if __name__ == "__main__":
    main()
