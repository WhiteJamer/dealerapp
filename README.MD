# Dealerapp
Это мой домашний проект, целью которого было - Продемострировать мои навыки и показать что я способен справляться с полным циклом разработки.

### Features
- Проект написан на [Django Framework](https://www.djangoproject.com/ "Django Framework") v2.2.7
- Для упрощения стилизации форм используется [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms "django-crispy-forms")
- Для API использован [Django Rest Framework](https://www.django-rest-framework.org// "Django Rest Framework") v3.11.0
### QuickStart
Вам нужен Python 3.6 и выше.

#### Windows:
	
    git clone https://github.com/WhiteJamer/dealerapp
В репозитории:


    pip install -r requirements.txt

Настройте параметры базы данных PostgreSQL под свои в settings.py:
````
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{YOUR DATABASE NAME}',
        'USER': '{YOUR DATABASE USERNAME}',
        'PASSWORD': '{YOUR DATABASE PASSWORD}',
        'HOST': '{YOUR HOST NAME}',
        'PORT': '{YOUR DATABASE PORT}',
    }
}
```` 
Запустите:


    python manage.py makemigrations
    python manage.py migrate
Создайте суперюзера:


    python manage.py createsuperuser
Запустите дев-сервер:


    python manage.py runserver
### Linux:
	
    git clone https://github.com/WhiteJamer/dealerapp
В репозитории:


    pip install -r requirements.txt
Выберите базу данных и запустите:


    manage.py makemigrations
    manage.py migrate
Создайте суперюзера:


    manage.py createsuperuser
Запустите дев-сервер:


    manage.py runserver
    
### API документация:

#### Дилеры:
Получить всех дилеров - `GET /api/dealers/`

Получить информацию о конкретном дилере - `GET /api/dealers/{ID}`

#### Дилерcкие центры:
Получить все дилерские центры - `GET /api/dealerships/`

Получить информацию о конкретном дилерском центре - `GET /api/dealerships/{ID}`

#### Автомобили:
Получить все автомобили - `GET /api/cars/`

Получить информацию о конкретном автомобиле - `GET /api/cars/{ID}`


![Users list photo](https://i.imgur.com/VdDe9QW.png?1)

