import pymysql
import string
import secrets

def create_user(host, admin_user, admin_password, new_user, new_password, database):
    """
    Создает пользователя в MySQL/MariaDB и выдает ему права на указанную базу.
    
    :param host: Хост сервера
    :param admin_user: Имя администратора (обычно root)
    :param admin_password: Пароль администратора
    :param new_user: Имя нового пользователя
    :param new_password: Пароль нового пользователя
    :param database: Имя базы данных, к которой выдаются права
    """
    try:
        # Подключаемся к серверу
        conn = pymysql.connect(
            host=host,
            user=admin_user,
            password=admin_password
        )
        
        with conn.cursor() as cursor:
            # Создаем пользователя (если его нет)
            cursor.execute(f"CREATE USER IF NOT EXISTS '{new_user}'@'%' IDENTIFIED BY '{new_password}';")
            
            # Даем пользователю права на указанную базу
            cursor.execute(f"GRANT ALL PRIVILEGES ON {database}.* TO '{new_user}'@'%';")
            
            # Фиксируем изменения
            cursor.execute("FLUSH PRIVILEGES;")
        
        conn.commit()
        print(f"✅ Пользователь {new_user} успешно создан на сервере {host} с доступом к базе {database}.")
    
    except pymysql.MySQLError as e:
        print(f"❌ Ошибка при создании пользователя: {e}")
    
    finally:
        if 'conn' in locals():
            conn.close()

def generate_password(length=12):
    """Генерирует безопасный пароль из букв, цифр и спецсимволов."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))
