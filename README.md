# Settings backend
Test project - sending emails


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


##Description:
1. 
2. Подразумевается что загружаемые данные подписчиков(Followers) относятся только к одной группе(FollowerGroup) для рассылки.
3. Допускается Загрузка списка подписчиков без проверок на наличие в бд - bulk_create. 
Если делать проверку(не засорять бд), то необходимо ставить поле M2M в FollowerGroup вместо FK в Followers, переписывать [bulk_create](https://stackoverflow.com/questions/34090582/proper-way-to-bulk-create-for-manytomany-field-django)
4. Распотрошил инлайн [пагинатор](https://github.com/shinneider/django-admin-inline-paginator), переписал на python2
5. Создал генератор csv на 500000 записей на python3 - 26секунд, на Golang (>>> [репо здесь](https://github.com/vildan-valeev/csv_data_generator) <<<) - 9 секунд
