# Mail sendler backend
Test project - sending emails

### Условия
Написать на Python небольшой сервис отправки имейл рассылок.
Возможности сервиса:
1. Отправка рассылок с использованием html макета и списка подписчиков.
2. Отправка отложенных рассылок.
3. Использование переменных в макете рассылки. (Пример: имя, фамилия, день рождения из списка подписчиков)
4. Отслеживание открытий писем.
Отложенные отправки реализовать при помощи Celery.

## dev
```sh
$ docker-compose -f docker-compose.dev.yml up -d --build
```


## Enter to container
```sh
$ docker exec -it <id container or name> bash
$ docker exec -it <id container or name> poetry run <command>
```
## Database dump/load
```sh
$ docker exec -it backend python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --exclude=admin.logentry --exclude=sessions.session --indent 4 > default_data.json

$ python manage.py loaddata default_data.json
```


## Description:
1. Подразумевается что загружаемые данные подписчиков(Followers) относятся только к одной группе(FollowerGroup) для рассылки.
2. Допускается Загрузка списка подписчиков без проверок на наличие в бд - bulk_create. 
Если делать проверку(не засорять бд), то необходимо ставить поле M2M в FollowerGroup вместо FK в Followers, переписывать [bulk_create](https://stackoverflow.com/questions/34090582/proper-way-to-bulk-create-for-manytomany-field-django)
3. Распотрошил инлайн [пагинатор](https://github.com/shinneider/django-admin-inline-paginator), переписал на python2
4. Создал генератор csv на 500000 записей на python3 - 26секунд, на Golang (>>> [репо здесь](https://github.com/vildan-valeev/csv_data_generator) <<<) - 9 секунд
5. настройка батчей вручную в коде
6. 
