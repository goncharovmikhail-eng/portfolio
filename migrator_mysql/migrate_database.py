import subprocess

def migrate_database(db_A,db_B):
    command = f"time mysqldump --defaults-group-suffix=A {db_A} | mysql --defaults-group-suffix=B {db_B}"

    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(f"✅ База {db_A} успешно скопирована в {db_B}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка при переносе базы: {e.stderr}")
