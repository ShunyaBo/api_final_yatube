# API для Yatube

[![Python](https://img.shields.io/badge/-Python-lightgrey)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-lightgrey)](https://www.djangoproject.com/) [![Django REST framework](https://img.shields.io/badge/-Django%20REST%20framework-lightgrey)](https://www.django-rest-framework.org/) [![Pytest](https://img.shields.io/badge/-Pytest-lightgrey)](https://docs.pytest.org/en/6.2.x/)[![Postman](https://img.shields.io/badge/-Postman-lightgrey)](https://www.postman.com/) [![JWT + Djoser](https://img.shields.io/badge/-JWT%20%2B%20Djoser-lightgrey)](https://djoser.readthedocs.io/en/latest/introduction.html)

Финальный проект 9 спринта Яндекс Практикум - API для Yatube.
___
## Оглавление <a id="Content"></a>
1. [Описание](#Description)
2. [Установка](#Installation)
3. [Примеры запросов к API](#Examples)
4. [Документация к API](#Documentation)
___
## Описание <a id="Description"></a>

API для проекта социальной сети Yatube. Проект реализован с помощью DRF.
####Доступный функционал
* Для аутентификации используются JWT-токены.
* У неаутентифицированных пользователей доступ к API должен быть только на чтение. Исключение — эндпоинт ```/follow/```: доступ к нему должен предоставляться только аутентифицированным пользователям.
* Аутентифицированным пользователям разрешено изменение и удаление своего контента, в остальных случаях доступ предоставляется только для чтения.
* API позволяет осуществлять: 
    * подписку на пользователей;
    * просмотр, создание, изменение и удаление публикаций;
    * просмотр списка групп и информации о группе по её id;
    * возможность добавления, редактирования, удаления своих комментариев и просмотр чужих.
* Создана фильтрация по полям.
* Cоздать группу можно через админ-зону.

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
[*Оглавление*](#Content)
___
## Примеры запросов к API.<a id="Examples"></a>
Неавторизованные пользователи работают с API только в режиме чтения, создать, изменить или удалить что-либо они не могут. Им доступны не все эндпоинты.

###Примеры запросов для неавторизованных пользователей:
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
#####Полный список запросов API находятся в документации.

[*Оглавление*](#Content)
___
# Документация к API.<a id="Documentation"></a>
Когда вы запустите проект, по адресу ```http://127.0.0.1:8000/redoc/``` будет доступна документация для API Yatube. 
[*Оглавление*](#Content)