import pymysql
import string
import secrets
import os
import subprocess
import re
import getpass

def get_existing_password(section):
    """Читает пароль пользователя из ~/.my.cnf, если он там есть."""
    config_path = os.path.expanduser("~/.my.cnf")
    if not os.path.exists(config_path):
        return None

    with open(config_path, "r") as f:
        content = f.read()

    match = re.search(rf"\[{section}\]\nuser=.*\npassword=(.*)\n", content)
    return match.group(1) if match else None

def get_existing_section(section):
    """Проверяет, есть ли секция в ~/.my.cnf."""
    config_path = os.path.expanduser("~/.my.cnf")
    if not os.path.exists(config_path):
        return False  # Файла нет — секции нет

    with open(config_path, "r") as f:
        content = f.read()

    return bool(re.search(rf"\[{section}\]", content))  # True, если секция найдена

def get_connection(host, user, password):
    """Создаёт соединение с MySQL и возвращает его"""
    try:
        use_socket = host in ('localhost', '127.0.0.1')
        return pymysql.connect(
            host=host,
            user=user,
            password=password,
            unix_socket="/var/lib/mysqld/mysqld.sock" if use_socket else None
        )
    except pymysql.OperationalError as e:
        print(f"❌ Ошибка подключения к серверу {host}: {e}")
        return None

def create_user(conn, user, new_password, database, range_ip, create_db=True):
    """Создаёт пользователя в MySQL/MariaDB и (если нужно) базу данных."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("CREATE USER IF NOT EXISTS %s@%s IDENTIFIED BY %s;", (user, range_ip, new_password))

            if create_db:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}`;")
            cursor.execute("GRANT ALL PRIVILEGES ON {}.* TO %s@%s;".format(database), (user, range_ip))
            cursor.execute("GRANT PROCESS ON *.* TO %s@%s;", (user, range_ip))
            cursor.execute("FLUSH PRIVILEGES;")

        conn.commit()
        print(f"✅ Пользователь {user} успешно создан с доступом к базе {database}.")

    except pymysql.MySQLError as e:
        print(f"❌ Ошибка при создании пользователя: {e}")

def generate_password(length=12):
    """Генерирует безопасный пароль из букв, цифр и спецсимволов."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def append_mysql_config(section, user, password, host):
    """Добавляет или обновляет креды в ~/.my.cnf"""
    config_path = os.path.expanduser("~/.my.cnf")
    config_entry = f"\n[{section}]\nuser={user}\npassword={password}\nhost={host}\n"

    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            content = f.readlines()

        new_content = []
        inside_section = False

        for line in content:
            if line.strip().startswith("["):
                inside_section = line.strip() == f"[{section}]"

            if inside_section:
                continue  # Пропускаем строки внутри удаляемой секции

            new_content.append(line)

        # Добавляем новую секцию в конец файла
        new_content.append(config_entry)

        with open(config_path, "w") as f:
            f.writelines(new_content)

        print(f"✅ Раздел [{section}] обновлён в {config_path}.")
    else:
        with open(config_path, "w") as f:
            f.write(config_entry)

        print(f"✅ Файл {config_path} создан и раздел [{section}] добавлен.")

def check_mysql_connection(point):
    """Проверяет соединение с MySQL"""
    print("Проверяем соединение с MySQL...")

    try:
        result = subprocess.run(
            ["mysql", f"--defaults-group-suffix={point}", "-e", "SHOW DATABASES;"],
            capture_output=True, text=True, check=True
        )
        print("Подключение успешно! Доступные базы данных:\n")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Ошибка при подключении к MySQL!")
        print(e.stderr)
