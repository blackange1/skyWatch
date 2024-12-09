# Головні команди

## Створення супер користувача

```shell
./manage.py createsuperuser
```

## Дані дял входу в адмін панель

* url: `http://127.0.0.1:8000/admin/login/?next=/admin/`
* login: `admin`
* password: `admin`

## Запуск сервера

```shell
./manage.py runserver
```

## Створення міграці бази даних

```shell
./manage.py makemigrations
```

## Міграці бази даних

```shell
./manage.py migrate
```

## URL адреси застосунку

* Посилання на radar: `http://localhost:8000/radar/<str:channel>`
* Приклад посилання на radar: `http://localhost:8000/radar/poltava`

## [UML діаграма](https://drive.google.com/file/d/1BDjQ-Q8GfcWHc222fXKkdZRElMeQ1ESU/view?usp=sharing)

Оновлення дахих відбувається через 2 секунди

```js
setTimeout(() => {
    window.location.reload();
}, 2000)
```