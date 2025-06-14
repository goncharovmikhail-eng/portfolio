# 🛠  Портфолио

Этот репозиторий содержит удобные скрипты и функции для DevOps-задач, автоматизации, мониторинга и работы с инфраструктурой.

## 🔄 migrator_mysql
Мигратор БД для **MySQL / MariaDB**, запускаемый через **Docker Compose**.
**Требование**: сетевая связанность между контейнером и базами.

## ☁ yandex-cloud
- Скрипт для перемещения **снимков, образов и VM** в **Yandex Cloud**.
- Дополнительные удобные функции для работы с **YC CLI**.

## ansible
Короткая ансибл-роль, которая:
- Меняет hostname и создает notify-записку, которая включается перед каждой новой сессией - точно не ошибетесь сервером
- Настройка времени. По дефолту Московское.
- Устанавливает набор most have утилит.
- Пробрасывает алиасы в .bashrc
## docker-ansible-role
- Установка docker, docker compose.
- Функции очистки неработающих контейнеров и старых образов, если это необходимо для ресурсов системы.
- Функия "бекапирования" работающих контейнеров. 
(Выполнение всех функций ставится на крон и выполняется раз в неделю).

## 🔐 form_for_passwords
Менеджер паролей, использующий зашифрованный **GPG**-файл.  
**Проблема**: Был неудобный доступ к кредам в базе знаний из этого следовало - хранение в `.txt` -  небезопасно.  
**Решение**: Удобная форма с функциями для взаимодействия с ней и с настройкой кеширования пароля для расшифровки.

## 📡 monitoring
Скрипт `ii` предоставляет расширенную информацию о системе:
- 📊 Аппаратные характеристики
- 🚀 Загрузка CPU
- 💾 Память, диски
- 🌐 Сетевые интерфейсы, порты
⚡ В будущем адоптация для  `node_exporter`.

## monitoring.zabbix
Ansible role формирует и запускает 3 docker-контейнера. psql v14, zabbix-server, и nginx. 
Важно подложить цепочку сертификатов и root сертификат для успешного завершения сценария.
Для генерации сертификатов обратите внимание на единый центр выдачи тестовых сертификатов в портфолио.

## monitoring.cacti
Ansible-role запускает 3 контейнера. MariaDB, cacti и nginx. Роль запускает контейнер с базой с cacti.sql. Также по дефолту увеличиное место под php в оперативной памяти.
Работает на https.

Важно, если исповали ansible role docker в портфолио, то не забывайте прогонять ее заново, после запуска нового контейнера(ов). Это обновляет скрипт бекапирования контейнеров.
## 🛠 git
Функции для упрощения работы с **Git**:
- 🗑 Удаление локальных и удалённых веток.
- 🔄 Автокоммит и пуш незакомиченных изменений во всех папках где есть `.git`.
- ⚡ Упрощённая инициализация репозитория (`git init + add remote`).
- 📥 Массовое обновление (`git fetch && git pull`) для всех репозиториев.
- 🚀 В будущем – пайплайны.

## Полезные shell-скрипты общего назначения.
Скрипт user.sh предназначен для прокидывания публичных ssh ключей, настроки службы ssh, и отключения пароля для пользователя.
Очень удобен для начала работы на пустой машине.
Логика:
- -U [name_user] - если пользователя не существует, то скрипт создает его без пароля.
- Создает папку .ssh(если не создана) и authorized_keys, если не создан. Назначает им права 700 и владельца в зависимости от пункта выше.
- В файле /etc/ssh/sshd_config отключает вход по паролю, активирует вход через публичный ssh ключ, и назначает порт 22. Перезагружает службу.
- Редактирует политики visudo. Добавляет пользователя в группу wheel и отключает ввод пароля.
- Переводит политику SElinux в режим предупреждения.
**Важно** Запускать только от root. Внутри скрипта есть проверка.

## 📤 google_service
Скрипты на **Google Apps Script**:
- 🧹 Очистка всех входящих сообщений в Gmail.

## C_CICD
Учебный проект, где:
- утилиты cat и grep написаны на чистом си
- unit-тесты на bash
- cicd настроен для gitlab
- телеграм бот с оповещением о результате cicd выполнен в bash
