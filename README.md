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
