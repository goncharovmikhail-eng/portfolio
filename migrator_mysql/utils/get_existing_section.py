import os
import re

def get_existing_section(section):
    """Проверяет, есть ли секция в ~/.my.cnf."""
    config_path = os.path.expanduser("~/.my.cnf")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return bool(re.search(rf"\[{section}\]", f.read()))
    return False
