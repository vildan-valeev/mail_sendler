# Settings backend
Test project - sending emails


## dev
```sh
$ docker-compose -f docker-compose.dev.yml up -d --build
```


## Enter to container
```sh
$ docker exec -it <id container or name> bash
$ docker exec -it <id container or name> <command>
```
## Database dump/load
```sh
$ python manage.py dumpdata --natural-foreign --natural-primary --exclude=contenttypes --exclude=auth.Permission --indent 4 > default_data.json

$ python manage.py loaddata default_data.json
```


##Description:
1. Подразумевается что загружаемые данные подписчиков(Followers) относятся только к одной группе(FollowerGroup) для рассылки.
2. Допускается Загрузка списка подписчиков без проверок на наличие в бд - bulk_create. 
Если делать проверку(не засорять бд), то необходимо ставить поле M2M в FollowerGroup вместо FK в Followers, переписывать [bulk_create](https://stackoverflow.com/questions/34090582/proper-way-to-bulk-create-for-manytomany-field-django)
3. Распотрошил инлайн [пагинатор](https://github.com/shinneider/django-admin-inline-paginator)
