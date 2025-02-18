import getpass
import pymysql
from utils import *

def get_admin_and_ip_range(section, user):
    """Запрашивает у пользователя имя и пароль администратора, а также диапазон IP-адресов для пользователя."""
    admin = input("Имя администратора (Enter для 'root'): ") or "root"
    admin_password = getpass.getpass(f"Введите пароль администратора для {section}: ")
    range_ip = input(f"Диапазон IP-адресов для {user} (Enter для '%'): ") or "%"
    return admin, admin_password, range_ip

def confirm_and_create_user(section, user, user_password, host, database, create_db):
    """Подтверждает создание пользователя и создает его."""
    choice = input(f"Добавить пользователя {user} на хосте {host}? (Y/n) ").strip().lower()
    if choice == "y":
        admin, admin_password, range_ip = get_admin_and_ip_range(section, user)

        conn = get_connection(host, admin, admin_password)
        if conn:
            create_user(conn, user, user_password, database, range_ip, create_db)
            conn.close()
            check_mysql_connection(section)

def setup_section(section, create_db, database):
    """Настраивает секцию в ~/.my.cnf, создает пользователя и проверяет соединение."""
    section_name = f"client{section}"
    print(f"\n🔹 Пишем данные для секции {section}:\n")

    user, user_password, host = get_or_update_credentials(section_name)

    confirm_and_create_user(section, user, user_password, host, database, create_db)
