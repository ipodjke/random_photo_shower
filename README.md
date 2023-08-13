# GetRandomPhoto, «Получи случайную кратинку»

На этом сервисе пользователи могут выбирать случайную картинку принадлежащуюю какой-то категории.

## Суть

Данный проект был разработан в учебных целях, а так же использовать style guide Django.
> [HackSoftware / Django-Styleguide](https://github.com/HackSoftware/Django-Styleguide?ysclid=ll9sdk8slt572212674) - This is the Django Styleguide, created by us, the folks at HackSoft.

### Технологии

Список технологий используемых в проекте:

- [Django](https://www.djangoproject.com/) - Web framework
- [Django Rest FrameWork](https://www.django-rest-framework.org/) - is a powerful and flexible toolkit for building Web APIs
- [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server для UNIX
- [Docker](https://www.docker.com/) - Package Software into Standardized Units for Development, Shipment and Deployment
- [Nginx](https://nginx.org/ru/) - HTTP-сервер и обратный прокси-сервер, почтовый прокси-сервер, а также TCP/UDP прокси-сервер общего назначения
- [PostgreSQL](https://www.postgresql.org/) - база данных
- [ReactJS](https://reactjs.org) - фронтовая часть приложения

## Запуск
Запуск проекта осуществляется только с исопльзованием Docker'а.

Структура env файла бекенда:

[GENERAL]<br>
DEBUG - настройка дебага джанго.<br>
SECRET_KEY - секртеный ключ для запуска Django<br>
DJANGO_ALLOWED_HOSTS<br>
DJANGO_SETTINGS_MODULE=config.settings.dev - указание с какими настройками будет запускаться Django

[DATABASE] - настройки для подключения базы данных.<br>
SQL_ENGINE<br>
SQL_DATABASE<br>
SQL_USER<br>
SQL_PASSWORD<br>
SQL_HOST<br>
SQL_PORT<br>


### Возможны два варианта запуска проекта:

1) Запуск версии для разработки.
    - **Требования к запуску!:**
        - Перед сборкой необходимо создать и заполнить файл /backend/envfiles/.env.dev,
          образец шаблона расположен /backend/envfiles/templates/env_base_template
        - Так же создать в папке /frontend/ файл .env.development с необходимыми 
          для связи фронтенда и бекенда двумя константами:
          1) REACT_APP_API_URL = http://localhost:8080/api
          2) REACT_APP_IMG_URL = http://localhost:8080
    - Особенности:
        - фронт и бэк работают совместно
        - можно отдельно взаимодействовать с фронтом и бекендом

```sh
git clone git@github.com:ipodjke/random_photo_shower.git
cd random_photo_shower/infrastructure
docker compose -f docker-compose.dev.yml up -d --build    
```

2) Запуск продакшен версии.
    - **Требования к запуску!:**
        - Перед сборкой необходимо создать и заполнить файл /backend/envfiles/.env.prod,
          образец шаблона расположен /backend/envfiles/templates/env_base_template
        - Так же создать в папке /frontend/ файл .env.production с необходимыми 
          для связи фронтенда и бекенда двумя константами:
          1) REACT_APP_API_URL = http://localhost/api
          2) REACT_APP_IMG_URL = http://localhost

    - Особенности:
        - фронт и бэк работают совместно
        - запускается nginx которые осуществляет менеджмент запросов
          и раздачу статики

```sh
git clone git@github.com:ipodjke/random_photo_shower.git
cd random_photo_shower/infrastructure
docker compose -f docker-compose.prod.yml up -d --build    
```

## License
MIT<br>
**Free Software, Hell Yeah!**

## Автор

[Андрей Белов](https://github.com/ipodjke)