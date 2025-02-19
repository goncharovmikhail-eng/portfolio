# Мигратор БД для MySQL и MariaDB

Этот скрипт предназначен для миграции данных между серверами (MySQL и MariaDB).

## Важные моменты

- Внутри контейнера используется клиент MariaDB.
- Для корректной работы мигратора на серверах **A** и **B** должен быть создан пользователь исполняющий функции администратора, доступный с любых хостов через `"%"`.
Это единственное, что придется сделать руками.
## Настройка пользователя на сервере A

Если вы создаете нового администратора, чтобы был доступен со всех хостов '%', рекомендуется выдать ему права как у root:

```sql
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, 
REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, 
EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, 
ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE
ON *.* TO 'test'@'%' WITH GRANT OPTION;

GRANT APPLICATION_PASSWORD_ADMIN, AUDIT_ABORT_EXEMPT, AUDIT_ADMIN, 
AUTHENTICATION_POLICY_ADMIN, BACKUP_ADMIN, BINLOG_ADMIN, BINLOG_ENCRYPTION_ADMIN, 
CLONE_ADMIN, CONNECTION_ADMIN, ENCRYPTION_KEY_ADMIN, FIREWALL_EXEMPT, 
FLUSH_OPTIMIZER_COSTS, FLUSH_STATUS, FLUSH_TABLES, FLUSH_USER_RESOURCES, 
GROUP_REPLICATION_ADMIN, GROUP_REPLICATION_STREAM, INNODB_REDO_LOG_ARCHIVE, 
INNODB_REDO_LOG_ENABLE, PASSWORDLESS_USER_ADMIN, PERSIST_RO_VARIABLES_ADMIN, 
REPLICATION_APPLIER, REPLICATION_SLAVE_ADMIN, RESOURCE_GROUP_ADMIN, RESOURCE_GROUP_USER, 
ROLE_ADMIN, SENSITIVE_VARIABLES_OBSERVER, SERVICE_CONNECTION_ADMIN, 
SESSION_VARIABLES_ADMIN, SET_USER_ID, SHOW_ROUTINE, SYSTEM_USER, SYSTEM_VARIABLES_ADMIN, 
TABLE_ENCRYPTION_ADMIN, TELEMETRY_LOG_ADMIN, XA_RECOVER_ADMIN
ON *.* TO 'test'@'%' WITH GRANT OPTION;

GRANT PROXY ON ``@`` TO 'test'@'%' WITH GRANT OPTION;
```

### Важно: 
Вы можете не использовать команду FLUSH PRIVILEGES;, чтобы изменения не сохранялись после работы скрипта.
## Примечание
Как показала практика, даже если вы даете пользователю 'test'@'%' все права на уже созданную базу, она может остаться недоступной. Поэтому рекомендую применить права описанные выше.

Скрипт подразумивает, что на сервере А новая база не создается. На сервере B создается пустая БД, в которую и будет происходить восстановление из сервера А.

## Перед запуском скрипта:
- Убедитесь, что все инстансы находятся в одной сети.
- Скрипт создаст конфигурационный файл .my.cnf локально или внутри контейнера.
- Этот файл будет автоматически заполнен необходимыми данными для подключения.
- Генерируются пароли для пользователей clientA и clientB, которые будут отображены в консоли после создания.
- Скрипт создаст пользователей в БД (в следующих версиях будет добавлена возможность выбора, так как, возможно, пользователь root уже обладает всеми правами для миграции).
- Присваиваются все права на таблицы и процессы для новых пользователей.
- Скрипт выполняет прямое восстановление БД с clientA на clientB, минуя этап dump.

## Ограничения и особенности
На данный момент в docker-compose невозможно передать переменные окружения напрямую, но эта функция будет добавлена в следующих версиях.
Также, если созданные новый пользователь больше не нужен, его следует удалить вручную.

## Как использовать с Docker:
```bash
docker-compose up -d
docker-compose run --rm my_migrator
```
```bash
docker compose down
```
