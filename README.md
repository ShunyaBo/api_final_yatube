# API для Yatube

[![Python](https://img.shields.io/badge/-Python-lightgrey)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-lightgrey)](https://www.djangoproject.com/) [![Django REST framework](https://img.shields.io/badge/-Django%20REST%20framework-lightgrey)](https://www.django-rest-framework.org/) [![Pytest](https://img.shields.io/badge/-Pytest-lightgrey)](https://docs.pytest.org/en/6.2.x/)[![Postman](https://img.shields.io/badge/-Postman-lightgrey)](https://www.postman.com/) [![JWT + Djoser](https://img.shields.io/badge/-JWT%20%2B%20Djoser-lightgrey)](https://djoser.readthedocs.io/en/latest/introduction.html)
___
## Оглавление <a id="Content"></a>
1. [Описание](#Description)
2. [Установка](#Installation)
3. [Регистрация нового пользователя и получение токена](#Registration)
3. [Примеры запросов и ответов к API](#Examples)
4. [Документация к API](#Documentation)
5. [Автор](#Author)
___
## Описание <a id="Description"></a>

API для проекта социальной сети Yatube,позволяет осуществлять: 
* Подписку на пользователей.
* Просмотр, создание, изменение и удаление публикаций.
* Просмотр списка групп и информации о группе по её id.
* Возможность добавления, редактирования, удаления своих комментариев и просмотр чужих.
* Фильтрацию по полям.
* Создание групп через админ-зону.

Проект реализован с помощью DRF.


#### Доступный функционал
* Для аутентификации используются JWT-токены.
* У неаутентифицированных пользователей доступ к API должен быть только на чтение. Исключение — эндпоинт ```/follow/```: доступ к нему должен предоставляться только аутентифицированным пользователям.
* Аутентифицированным пользователям разрешено изменение и удаление своего контента, в остальных случаях доступ предоставляется только для чтения.


[*Оглавление*](#Content)
___
##  Установка <a id="Installation"></a>
### Как запустить проект:

1.Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ShunyaBo/api_final_yatube.git
```

```
cd api_final_yatube
```

2.Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
# для OS Lunix и MacOS
source venv/bin/activate

# для OS Windows
source venv/Scripts/activate
```

3.Обновить pip:

```
python3 -m pip install --upgrade pip
```

4.Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

5.Выполнить миграции на уровне проекта:

```
python3 manage.py makemigrations
python3 manage.py migrate
```
6.Запустить проект, находясь в директории yatube_api, где расположен файл manage.py
```
python3 manage.py runserver
```
7.Создаем суперпользователя:
```
python3 manage.py createsuperuser
```
8.Сам проект располагается по адреcу:
```
http://127.0.0.1:8000
```
9.Админ-панель находится по адресу: ```http://127.0.0.1:8000/admin```, через неё необходимо будет создать группы постов.

[*Оглавление*](#Content)
___
## Регистрация нового пользователя и получение токена<a id="Registration"></a>
Для регистрации нового пользователя необходимо сделать запрос на эндпоинт ```http://127.0.0.1:8000/api/v1/users/``` в теле запроса указать следующее:
```
{
"username": "string",
"password": "string",
"email": "string"
}
```
Если Вы сделали все правильно, то получите HTTP-ответ со статус-кодом 201 Created::
```
{
"email": "string",
"username": "string",
"id": "integer"
}
```
После успешной регистрации, необходимо получить токен, отправив POST-запрос на эндпоинт ```http://127.0.0.1:8000/api/v1/jwt/create/```, передав действующий логин и пароль в полях **username** и **password**:
```
{
"username": "string",
"password": "string",
}
```
API вернёт JWT-токен:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMDk0MTQ3NywianRpIjoiODUzYzE5MTg5NzMwNDQwNTk1ZjI3ZTBmOTAzZDcxZDEiLCJ1c2VyX2lkIjoxfQ.0vJBPIUZG4MjeU_Q-mhr5Gqjx7sFlO6AShlfeINK8nA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwODU1Mzc3LCJqdGkiOiJkY2EwNmRiYTEzNWQ0ZjNiODdiZmQ3YzU2Y2ZjNGE0YiIsInVzZXJfaWQiOjF9.eZfkpeNVfKLzBY7U0h5gMdTwUnGP3LjRn5g8EIvWlVg"
} 
```
Токен вернётся в поле **access**, а данные из поля **refresh** пригодятся для обновления токена. 
В дальнейшем нам понадобится **access** для работа как аутентифицированный пользователь, его надо будет передавать в заголовке каждого запроса, в поле **Authorization**. Перед самим токеном должно стоять ключевое слово **Bearer** и **пробел**: ```Bearer <токен>```.

[*Оглавление*](#Content)
___
## Примеры запросов и ответов к API<a id="Examples"></a>
* Создание поста

Отправляем POST-запрос на адрес ```http://127.0.0.1:8000/api/v1/posts/``` и передаём обязательное поле text, в заголовке указываем ```Authorization:Bearer <токен>```.
Пример запроса:
```
{
  "text": "Тестовый пост."
}
```
Пример ответа:
```
{
    "id": 1,
    "author": "user",
    "text": "Тестовый пост.",
    "pub_date": "2023-03-19T11:12:38.848100Z",
    "image": null,
    "group": null
}
```
* В проекте API реализована пагинация (LimitOffsetPagination):
```
GET /api/v1/posts/?limit=2&offset=6
```
Такой GET-запрос вернёт два объекта, с пятого по шестой (или меньше, если в результате запроса менее 6 объектов).

#### Примеры запросов для неавторизованных пользователей
Неавторизованные пользователи работают с API только в режиме чтения, создать, изменить или удалить что-либо они не могут. Им доступны не все эндпоинты.
```
1. GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией.
limit - Количество публикаций на страницу.
offset - Номер страницы после которой начинать выдачу.
2. GET api/v1/posts/{id}/ - получение публикации по id.
3. GET api/v1/groups/ - получение списка доступных сообществ.
4. GET api/v1/groups/{id}/ - получение информации о сообществе по id.
5. GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации.
6. GET api/v1/{post_id}/comments/{id}/ - получение комментария к публикации по id.
```
##### Полный список запросов API находятся в документации.

[*Оглавление*](#Content)
___
## Документация к API<a id="Documentation"></a>
Когда вы запустите проект, по адресу ```http://127.0.0.1:8000/redoc/``` будет доступна документация для API Yatube.
[*Оглавление*](#Content)
___
## Автор<a id="Author"></a>
[Mariya - ShunyaBo](https://github.com/ShunyaBo)
___
[*Вверх*](#Content)