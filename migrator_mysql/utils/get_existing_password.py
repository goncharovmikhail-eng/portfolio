import os
import re

def get_existing_password(section):
    """Возвращает пароль пользователя из ~/.my.cnf, если он там есть."""
    config_path = os.path.expanduser("~/.my.cnf")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            match = re.search(rf"\[{section}\]\nuser=.*\npassword=(.*)\n", f.read())
        return match.group(1) if match else None
    return None
