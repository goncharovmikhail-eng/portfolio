from .get_existing_section import get_existing_section
from .get_existing_password import get_existing_password
from .generate_password import generate_password
from .append_mysql_config import append_mysql_config

def check_and_prompt_overwrite(section_name):
    """Проверяет существование секции и запрашивает перезапись данных."""
    section_exists = get_existing_section(section_name)
    
    if section_exists:
        overwrite = input(f"⚠️ Секция [{section_name}] уже существует в ~/.my.cnf. Перезаписать? (y/N): ").strip().lower()
        if overwrite != "y":
            print("Будут использоваться старые креды, указанные в ~/.my.cnf")
            return False
    return True

def get_user_input(section_name):
    """Запрашивает у пользователя имя, пароль и хост для новой конфигурации."""
#   для использования данного шаблона, передайте аргументы в функицию.
#    user = f"{p_num}_{vm_num}_user"
    user = input(f"Введите имя создаваемого юзера на сервере {section_name} (Enter для 'sender'): ") or "sender"
    user_password = generate_password()
    host = input(f"IP адрес сервера {section_name} (Enter для 'localhost'): ") or "localhost"
    return user, user_password, host

def get_or_update_credentials(section_name):
    """Получает или обновляет учетные данные пользователя MySQL."""
    if check_and_prompt_overwrite(section_name):
        user, user_password, host = get_user_input(section_name)
        append_mysql_config(section_name, user, user_password, host)  # без лишней функции
        print(f"✅ Данные обновлены и записаны в ~/.my.cnf")
    else:
        user = "sender"
        user_password = get_existing_password(section_name)
        host = "localhost"

    return user, user_password, host
