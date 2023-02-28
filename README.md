# api_final
### api final yatube

## Описание:
Проект YaTube - это социальная сеть, функционал которой не отличается от привычных и известных нам аналогов. Создан в образовательных целях.
Любой пользователь может просматривать интересующиейся группы, посты. Последние в свою очередь могут быть разделены по категориям групп. Изменять или удалять записи имеет право лишь автор. Чтобы оставлять комментарии и подписываться на других пользователей, нужно пройти аутентификацию. Кстати о ней.

Аутентификация происходит по JWT-токену, с использованием библиотеки djoser. Поддерживает методы GET, POST, PUT, PATCH, DELETE. Предоставляет данные в формате JSON.

## Установка:
1. Клонировать репозиторий и перейти в него в командной строке:
    ```
    cd api_final_yatube
    ```
2. Cоздать и активировать виртуальное окружение:
    ```
    python3 -m venv env 
    ```
    ```
    source env/bin/activate
    ```
3. Установить зависимости из файла requirements.txt:
    ```
    python3 -m pip install --upgrade pip
    ```
    ```
    pip install -r requirements.txt
    ```
4. Выполнить миграции:
    ```
    python3 manage.py migrate
    ```
5. Создайте суперпользователя:
    ```
    python3 manage.py createsuperuser
    ```
6. Запустить проект:
    ```
    python3 manage.py runserver
    ```

## Примеры:
1. Создаём пост, предварительно пройдя аутентификацию.
    HTTP-запрос: http://127.0.0.1:8000/api/v1/posts/
    data = {"text": "Infinity is not the limit"}

Ответ API:
{
    "id": 11,
    "author": "me",
    "text": "Infinity is not the limit",
    "pub_date": "2023-02-27T11:42:56.957213Z",
    "image": null,
    "group": null
}
    Status: 201 Created

2. Удаляем пост.
    HTTP-запрос: http://127.0.0.1:8000/api/v1/posts/11/

Ответ API:
    Status: 204 No Content

3. Подписываемся на другого пользователя.
    HTTP-запрос: http://127.0.0.1:8000/api/v1/follow/
    data = {"following": "max"}

Ответ API:
{
    "id": 2,
    "user": "me",
    "following": "max"
}
    Status: 201 Created

## Использованные технологии:
![Django Rest Framework](https://media.slid.es/uploads/708405/images/4005243/django_rest_500x500.png)
#  Django REST Framework.
# библиотека Simple JWT + Djoser
# библиотека django-filter 
# БД SQLite
# Система управления версиями - Git

    

    


 
