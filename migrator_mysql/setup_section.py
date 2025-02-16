import getpass
from functions import create_user, generate_password, append_mysql_config, check_mysql_connection, get_connection, get_existing_section, get_existing_password

def get_or_update_credentials(section_name):
    """Получает или обновляет учетные данные пользователя MySQL."""
    section_exists = get_existing_section(section_name)

    if section_exists:
        overwrite = input(f"⚠️ Секция [{section_name}] уже существует в ~/.my.cnf. Перезаписать? (y/N): ").strip().lower()
        if overwrite != "y":
            print("Будут использоваться старые креды, указанные в ~/.my.cnf")
            return "sender", get_existing_password(section_name), "localhost"

    # Запрашиваем новые данные
    user = input(f"Введите имя создаваемого юзера на сервере {section_name} (Enter для 'sender'): ") or "sender"
    user_password = generate_password()
    host = input(f"IP адрес сервера {section_name} (Enter для 'localhost'): ") or "localhost"

    append_mysql_config(section_name, user, user_password, host)
    print(f"✅ Данные обновлены и записаны в ~/.my.cnf")

    return user, user_password, host

def setup_section(section, create_db, database):
    """Настраивает секцию в ~/.my.cnf, создает пользователя и проверяет соединение."""
    section_name = f"client{section}"
    print(f"\n🔹 Пишем данные для секции {section}:\n")

    user, user_password, host = get_or_update_credentials(section_name)

    choice = input(f"Добавить пользователя {user} на хосте {host}? (Y/n) ").strip().lower()
    if choice == "y":
        admin = input("Имя администратора (Enter для 'root'): ") or "root"
        admin_password = getpass.getpass(f"Введите пароль администратора для {section}: ")
        range_ip = input(f"Диапазон IP-адресов для {user} (Enter для '%'): ") or "%"

        conn = get_connection(host, admin, admin_password)
        if conn:
            create_user(conn, user, user_password, database, range_ip, create_db)
            conn.close()
            check_mysql_connection(section)
