import pymysql
import string
import secrets
import pymysql
import os
import subprocess

def create_user(host, admin_user, admin_password, new_user, new_password, database):
    """
    Создает пользователя в MySQL/MariaDB и выдает ему права на указанную базу.
    """
    try:
        # Подключаемся к серверу
        conn = pymysql.connect(
            host=host,
            user=admin_user,
            password=admin_password,
            unix_socket="/var/lib/mysqld/mysqld.sock" or "/var/lib/mysql/mysql.sock"
        )

        with conn.cursor() as cursor:
            # Создаем пользователя (если его нет)
            cursor.execute(f"CREATE USER IF NOT EXISTS '{new_user}'@'%' IDENTIFIED BY '{new_password}';")

            # Даем пользователю права на указанную базу
            cursor.execute(f"GRANT ALL PRIVILEGES ON {database}.* TO '{new_user}'@'%';")

            # Фиксируем изменения
            cursor.execute("FLUSH PRIVILEGES;")

        conn.commit()
        print(f"✅ Пользователь {new_user} успешно создан на сервере {host} с доступом к базе {database} и паролем {new_password}.")

    except pymysql.MySQLError as e:
        print(f"❌ Ошибка при создании пользователя: {e}")

    finally:
        if 'conn' in locals():
            conn.close()

def generate_password(length=12):
    """Генерирует безопасный пароль из букв, цифр и спецсимволов."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def append_mysql_config(section, user, password, host):
    config_path = os.path.expanduser("~/.my.cnf")  # Раскрываем путь к конфигу
    config_entry = f"\n[{section}]\nuser={user}\npassword={password}\nhost={host}\n"

    # Проверяем, существует ли уже этот раздел в конфиге
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            content = f.read()
            if f"[{section}]" in content:
                print(f"⚠️ Раздел [{section}] уже существует в {config_path}.")
                return

    # Дописываем раздел в конец файла
    with open(config_path, "a") as f:
        f.write(config_entry)

    print(f"✅ Раздел [{section}] добавлен в {config_path}.")

def check_mysql_connection(suffix="A"):
    print("Проверяем соединение с MySQL...")

    try:
        result = subprocess.run(
            ["mysql", f"--defaults-group-suffix={suffix}", "-e", "SHOW DATABASES;"],
            capture_output=True, text=True, check=True
        )
        print("Подключение успешно! Доступные базы данных:\n")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Ошибка при подключении к MySQL!")
        print(e.stderr)
