from setup_section  import get_or_update_credentials, setup_section
from migrate_database import migrate_database

def main():
    db_A = input("Введите имя базы данных для сервера А: ")
    db_B = input("Введите имя базы данных для сервера B: ")
    setup_section("A", database=db_A, create_db=False)
    setup_section("B", database=db_B, create_db=True)
    migrate_database(db_A, db_B)
if __name__ == "__main__":
    main()
