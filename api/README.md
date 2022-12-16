## Пометка для разработчиков

При создании нового приложения, нужно будет указать в файле `src/alembic.ini` в переменной `version_locations` путь,
где будут хранится ваши версии миграций.

Для создания новой миграции нужно импортировать модельку в src/\_\_init\_\_.py и ввести команду:
```bash
alembic revision -m <massage> --version-path=<path_to_version_file> --autogenerate
```
Для применение миграций нужно ввести команду:
```bash
alembic upgrade head
```
