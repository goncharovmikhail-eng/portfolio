import pymysql

def get_connection(host, user, password, port=3306):
    """Создаёт соединение с MySQL и возвращает его"""
    try:
        conn_params = {
            "host": host,
            "user": user,
            "password": password,
            "port": port,
        }
        if host in ("localhost", "127.0.0.1"):
            conn_params["unix_socket"] = "/var/lib/mysqld/mysqld.sock"

        return pymysql.connect(**conn_params)
    except pymysql.OperationalError as e:
        print(f"❌ Ошибка подключения к серверу {host}: {e}")
        return None
