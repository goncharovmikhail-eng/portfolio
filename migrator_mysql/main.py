from setup_section  import setup_section
from migrate_database import migrate_database

def main():
    try:
        db_A = input("Введите имя базы данных для сервера А: ")
        db_B = input("Введите имя базы данных для сервера B: ")
#        p_num = int(input("Введите номер проекта: "))
#        vm_num = int(input("Введите номер VM в кластере: "))
#        db_B = f"{p_num}_{vm_num}"
        
        setup_section("A", database=db_A, create_db=False)
        setup_section("B", database=db_B, create_db=True)
        print("Старт миграции...\n")
        migrate_database(db_A, db_B)
    except KeyboardInterrupt:
        print("\nAbort!")


if __name__ == "__main__":
    main()
