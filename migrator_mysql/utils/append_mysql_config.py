import os

def read_config_file(config_path):
    """Читает конфигурационный файл и возвращает его содержимое."""
    with open(config_path, "r") as f:
        return f.readlines()

def write_config_file(config_path, content):
    """Записывает обновленный контент в конфигурационный файл."""
    with open(config_path, "w") as f:
        f.writelines(content)

def update_config_with_section(content, section, config_entry):
    """Обновляет содержимое конфигурационного файла новой секцией."""
    new_content = []
    inside_section = False
    for line in content:
        if line.strip().startswith("["):
            inside_section = line.strip() == f"[{section}]"
        if inside_section:
            continue
        new_content.append(line)
    new_content.append(config_entry)
    return new_content

def append_mysql_config(section, user, password, host):
    """Добавляет или обновляет креды в ~/.my.cnf"""
    config_path = os.path.expanduser("~/.my.cnf")
    config_entry = f"\n[{section}]\nuser={user}\npassword={password}\nhost={host}\n"

    if os.path.exists(config_path):
        content = read_config_file(config_path)
        new_content = update_config_with_section(content, section, config_entry)
        write_config_file(config_path, new_content)
        print(f"✅ Раздел [{section}] обновлён в {config_path}.")
    else:
        write_config_file(config_path, [config_entry])
        print(f"✅ Файл {config_path} создан и раздел [{section}] добавлен.")
