import pymysql

def create_user_in_db(cursor, user, range_ip, new_password):
    """Создаёт пользователя в MySQL/MariaDB."""
    cursor.execute("CREATE USER IF NOT EXISTS %s@%s IDENTIFIED BY %s;", (user, range_ip, new_password))

def create_database_if_needed(cursor, database, create_db):
    """Создаёт базу данных, если это необходимо."""
    if create_db:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database}`;")

def grant_privileges(cursor, user, range_ip):
    """Назначает привилегии пользователю и обновляет их."""
    cursor.executemany(
        "GRANT %s ON *.* TO %s@%s;",
        [("ALL PRIVILEGES", user, range_ip), ("PROCESS", user, range_ip)]
    )
    cursor.execute("FLUSH PRIVILEGES;")

def create_user(conn, user, new_password, database, range_ip, create_db=True):
    """Создаёт пользователя в MySQL/MariaDB и (если нужно) базу данных."""
    try:
        with conn.cursor() as cursor:
            create_user_in_db(cursor, user, range_ip, new_password)
            create_database_if_needed(cursor, database, create_db)
            grant_privileges(cursor, user, range_ip)

        conn.commit()
        print(f"✅ Пользователь {user} создан, доступ к базе {database}.")
    except pymysql.MySQLError as e:
        print(f"❌ Ошибка: {e}")
