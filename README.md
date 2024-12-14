# Іструкція по розгортанню
скачати репозиторій 

встановити **Django**
```shell
pip install -r requirement.txt
```
перейти в терміналі у папку `sky_watch`
```shell
cd ./sky_watch
```
запустити **міграцію**, створить базу даних
```shell
./manage.py migrate
```
створити **супер юзера** із **логіном** `admin` та **паролем** `admin`, **email** не вказувати
```shell
./manage.py createsuperuser
```
замустити **сервер**
```shell
./manage.py runserver
```
відкрити сайт за **адресою** [http://127.0.0.1:8000](http://127.0.0.1:8000)