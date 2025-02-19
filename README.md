# 🛠 Мой набор утилит

Этот репозиторий содержит удобные скрипты и функции для DevOps-задач, автоматизации, мониторинга и работы с инфраструктурой.

## 🔐 form_for_passwords
Менеджер паролей, использующий зашифрованный **GPG**-файл.  
**Проблема**: неудобный доступ к кредам в базе знаний, хранение в `.txt` небезопасно.  
**Решение**: удобная форма с настройкой кеширования пароля.

## 🛠 git
Функции для упрощения работы с **Git**:
- 🗑 Удаление локальных и удалённых веток.
- 🔄 Автокоммит и пуш незакомиченных изменений во всех `.git`-папках.
- ⚡ Упрощённая инициализация репозитория (`git init + add remote`).
- 📥 Массовое обновление (`git fetch && git pull`) для всех репозиториев.
- 🚀 В будущем – пайплайны.

## 📤 google_service
Скрипты на **Google Apps Script**:
- 🧹 Очистка всех входящих сообщений в Gmail.

## 🔄 migrator_mysql
Мигратор БД для **MySQL / MariaDB**, запускаемый через **Docker Compose**.  
**Требование**: сетевая связанность между контейнером и базами.

## 📡 monitoring
Скрипт `ii` предоставляет расширенную информацию о системе:
- 📊 Аппаратные характеристики
- 🚀 Загрузка CPU
- 💾 Память, диски
- 🌐 Сетевые интерфейсы, порты  
⚡ В будущем адоптация для  `node_exporter`.

## ☁ yandex-cloud
- Скрипт для перемещения **снимков, образов и VM** в **Yandex Cloud**.  
- Дополнительные удобные функции для работы с **YC CLI**.
