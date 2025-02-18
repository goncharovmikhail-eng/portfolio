import subprocess

def check_mysql_connection(point):
    """Проверяет соединение с MySQL через команду mysql."""
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
