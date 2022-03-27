Generic single-database configuration.


Если вы создали новую модель в `./parser/app/models/`, обязательно импортируйте
ее в `./parser/app/db/base.py`. Модели в этом файле (`base.py`) будут 
использоваться Alembic.

После изменения модели (например, добавления столбца) создайте ревизию:

```console
$ alembic revision --autogenerate -m "Add column last_name to User model"
```

Зафиксировать в репозитории git файлы, сгенерированные в директории
`./parser/alembic/versions/`

После создания ревизии запустите миграции в базе данных 
(это то, что собственно изменит базу данных):

```console
$ alembic upgrade head
``
