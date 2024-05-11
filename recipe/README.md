# Дневник разработчика

## 2024-05-04

### День 1.

- На гитхабе создал пустой репозиторий https://github.com/pvplpt/Final-examination.git
- Локально создал папку Final-examination
- Создал README.md файл в папке Final-examination
- Залил первый коммит на github:

```
git init
git add README.md
git commit -m "initial commit"
git branch -M main
git remote add origin git@github.com:pvplpt/Final-examination.git
git push -u origin main
```

- Активировал виртуальное окружение:

```
source ~/.venvDjango/bin/activate
```

- В папке Final-examination создал проект:

```
django-admin startproject recipe
```

- Добавил ip в файл _settings.py_ для тестирования на планшете и смартфоне:

```
ALLOWED_HOSTS = ['127.0.0.1', '192.168.1.5',]
```

- Добавил файл .gitignore

```
__pycache__/
*.log
*.pot
*.pyc
*.sqlite3
media/
```

- Сменил текущую папку на папку проекта:

```
cd recipe
```

- Сохранил список установленных пакетов:

```
pip freeze > requirements.txt

cat requirements.txt
asgiref==3.8.1
Django==5.0.4
pillow==10.3.0
python-dotenv==1.0.1
sqlparse==0.5.0
typing_extensions==4.11.0
```

- Создал приложение:

```
python3 manage.py startapp finalapp
```

- Сразу добавил приложение в файл проекта _settings.py_:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'finalapp',
]
```

- Настроил пути в файле проекта urls.py:

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finalapp.urls')),
]
```

- Создал базаый шаблон в папке _templates/_ проекта
- Добавил путь к шаблону в файл проекта _settings.py_:

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

- Создал шаблон главной страницы в папке _templates/finalapp/_ приложения
- Создал представление главной страницы в приложении в файле views.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

- Создал простенькую иконку favicon.ico на сайте [https://www.favicon.cc](https://www.favicon.cc)
- Сохранил файл favicon.ico в папку приложения _static/finalapp/_

## 2024-05-05

### День 2.

- Создал приложение main:

```
python3 manage.py startapp main
```

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]
```

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

- Создал пустой шаблон главной страницы в папке _templates/main/_ приложения
- Удалил приложение finalapp
- Изменил код языка для вывода системных сообщений и страниц административного сайта - на ru

```
LANGUAGE_CODE = 'ru'
```

- Установил дополнительную библиотеку **django-bootstrap4**:

```
pip install django-bootstrap4
```

- Добавил в список зарегистрированных в проекте приложение _bootstrap4_:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'bootstrap4',
]
```

- Обновил список установленных пакетов:

```
pip freeze > requirements.txt

cat requirements.txt
asgiref==3.8.1
beautifulsoup4==4.12.3
Django==5.0.4
django-bootstrap4==24.3
pillow==10.3.0
python-dotenv==1.0.1
soupsieve==2.5
sqlparse==0.5.0
typing_extensions==4.11.0
```

- Добавил страницу about.html
- Добавил модель пользователя
- Указал ее как модель пользователя, используемую подсистемой разграничения доступа Django

```
AUTH_USER_MODEL = 'main.AdvUser'
```

- Создал миграции:

```
python3 manage.py makemigrations
```

- Выполнил миграции:

```
python3 manage.py migrate
```

- Создал суперпользователя:

```
python3 manage.py createsuperuser
```

- Зарегистрировал модель пользователя в админке

```
from.models import AdvUser
admin.site.register(AdvUser)
```

- Выполнил вход от имени созданного суперпользователя на странице по адресу:
  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Добавил страницу входа
- Добавил страницу профиля
- Добавил страницу выхода
- Добавил страницу правки личных данных
- Добавил страницу правки пароля

## 2024-05-06

### День 3.

- Добавил форму для регистрации нового пользователя
- Добавил страницу регистрации нового пользователя
- Добавил страницу удаления пользователя
- Добавил редактор пользователей в админку
- Установил библиотеку создания миниатюр и удаления выгруженных файлов после удаления записей модели:

```
pip install easy-thumbnails
pip install django-cleanup

```

- Обновил список установленных пакетов:

```
pip freeze > requirements.txt

cat requirements.txt
asgiref==3.8.1
beautifulsoup4==4.12.3
Django==5.0.4
django-bootstrap4==24.3
django-cleanup==8.1.0
easy-thumbnails==2.8.5
pillow==10.3.0
python-dotenv==1.0.1
soupsieve==2.5
sqlparse==0.5.0
typing_extensions==4.11.0
```

- Добавил в список зарегистрированных в проекте приложение _django-cleanup_ и _easy-thumbnails_:

```
INSTALLED_APPS = [
    . . .
    'django_cleanup',
    'easy_thumbnails',
]
```

- Создал папку _media_ в папке проекта
- Создал папку _thumbnails_ в папке _media_
- Создал в пакете приложения модуль _utilities.py_ , в который записал функцию _get_timestamp_path()_ , генерирующую имена выгруженных файлов.

## 2024-05-07

### День 4.

- Добавил модель Категории рецептов
- Выполнил миграции:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

- Добавил редактор категорий в админку
- Добавил список категорй в базовый шаблон
- Добавил модель рецептов
- Выполнил миграции:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

- Добавил редактор рецептов в админку
- Добавил рецепт с фото на административном сайте
- Удалил рецепт. фото удалилось автоматически.

## 2024-05-08

### День 5

- Добавил вывод рецептов по категориям с пагинатором и поиском по имени и описанию
- Добавил просмотр отдельного рецепта
- Добавил вывод 5 рецептов на главную страницу
- Добавил вывод рецептов в профиль пользователя Мои рецепты
- Добавил страницу добавления рецепта
- Добавил страницу редактирования рецепта
- Добавил страницу удаления рецепта

## 2024-05-09

### День 6

- Протестировал уже реализованный бэкенд функционал.
- Устанил ошибку: Не сохраняются фотографии при редактировании рецепта
- Реализовал отключение случайных рецептов для тех зарегистрированных пользователей, которые решили следить за новыми рецептами. Для них выводятся последние добавленные рецепты.
- Добавил страницу все рецепты

## 2024-05-10

### День 7

- Продолжил тестирование реализованного Backend-функционала
- Устранил ошибку: Не сохранется критерий поиска после возврата из детального просмотра
- Начал подготовку к переносу проекта на сервер pythonanywhere.com
- Зарегистрировался на сайте: [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
- Откючил режим дебага в файле проекта _settings.py_

```
DEBUG = False
```

- Добавил две константы для повышения безопасности работы с сессиями и с csrf токенами

```
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

- Изменил параметр SECRET_KEY

```
SECRET_KEY = os.getenv('SECRET_KEY')
```

- Добавил адрес сайта в список доступных хостов в файл _settings.py_ :

```
ALLOWED_HOSTS = ['pvplpt.pythonanywhere.com',]
```

- На сайте https://www.pythonanywhere.com инициализировал базу данных MySQL
- Кликнул по pvplpt$default чтобы открыть консоль MySQL
- Ввел команду для смены кодировки на UTF-8:

```
ALTER DATABASE pvplpt$default CHARACTER SET utf8 COLLATE utf8_general_ci;
```

- Выключил консоль командой exit
- Настроил подключение к MySQL в файле _settings.py_:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pvplpt$default',
        'USER': 'pvplpt',
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': 'pvplpt.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```

- Добавил в конец файла requirements.txt еще одну строку:

```
echo mysqlclient >> requirements.txt
cat requirements.txt
asgiref==3.8.1
beautifulsoup4==4.12.3
Django==5.0.4
django-bootstrap4==24.3
django-cleanup==8.1.0
easy-thumbnails==2.8.5
pillow==10.3.0
python-dotenv==1.0.1
soupsieve==2.5
sqlparse==0.5.0
typing_extensions==4.11.0
mysqlclient
```

- Добавил файл README.md в папку /media/thumbnails/ чтобы перенести ее на сервер
- Закоментировал #media/ в файле .gitignore чтобы залить папку /media/thumbnails/ на гитхаб
- Отпраил код в удаленный репозиторий

```
git add .
git commit -m "added readiness for copying to the site"
git push
```

- Открыл косноль Bash на сайте https://www.pythonanywhere.com и клонировал репозиторий с гитхаба:

```
git clone https://github.com/pvplpt/Final-examination.git
```

- Запустил команду создания виртуального окружения:

```
mkvirtualenv --python=/usr/bin/python3.10 virtualenv
```

- Перешел в папку с проектом:

```
cd Final-examination/recipe/
```

- Установил необходимые пакеты:

```
pip install -r requirements.txt
```

- Создал новое веб-прилодение копкой Add a new web app на вкладке Web:

1. Подтвердил доменное имя для бесплатного профиля кнопкой Next
2. Выбрал пункт Manual configuration (including virtualenvs)
3. Выбираем последнюю из доступных версий Python 3.10
4. Подтвердил выбор очередным нажатием Next
5. All done! Your web app is now set up. Details below.

- Настроил в разделе Virtualenv путь до созданного окружения:

```
/home/pvplpt/.virtualenvs/virtualenv
```

- Настроил в разделе Code путь Source code и Working directory

```
Source code: /home/pvplpt/Final-examination/recipe
Working directory: /home/pvplpt/Final-examination/recipe
```

- Отредактировал файл /var/www/pvplpt_pythonanywhere_com_wsgi.py

```
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

from dotenv import load_dotenv

project_folder = os.path.expanduser('~/Final-examination/recipe')
load_dotenv(os.path.join(project_folder, '.env'))

## assuming your django settings file is at '/home/pvplpt/mysite/mysite/settings.py'
## and your manage.py is is at '/home/pvplpt/mysite/manage.py'
path = '/home/pvplpt/Final-examination/recipe'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'recipe.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

- Сгенерировал токен в консоли

```
python
>>> import secrets
>>> secrets.token_hex()
>>> exit()
```

- Добавил токен в скрытый файл .evn Вместо звездочек вставил сгенерированный токен

```
echo "export SECRET_KEY=****************************************************************" >> .env
```

- Добавил пароль в скрытый файл .evn Вместо звездочек вставил пароль к MySQL

```
echo "export MYSQL_PASSWORD=***************" >> .env
```

- Научил консоль работать с "секретами":

```
echo 'set -a; source ~/Final-examination/recipe/.env; set +a' >> ~/.virtualenvs/virtualenv/bin/postactivate
```

- Настроил папку static и media в разделе Static files:

```
URL 	    Directory
/static/ 	/home/pvplpt/Final-examination/recipe/static
/media/ 	/home/pvplpt/Final-examination/recipe/media
```

- Отключил статику в файле проекта _urls.py_

```
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- Перезапустил консоль
- Выполнил миграции:

```
python manage.py makemigrations
python manage.py migrate
```

- Собрал статические файлы проекта и приложений в одном месте

```
python manage.py collectstatic
```

- Создал суперпользователя:

```
python3 manage.py createsuperuser
```

- Перезапустил сервер

- Зашел в админку https://pvplpt.pythonanywhere.com/admin/

- Создал категории рецептов:

```
Вторые блюда	0
Выпечка	0
Закуски	0
Мясо	0
Напитки	0
Пицца	0
Рыба	0
Салаты	0
Супы	0
Суши	0
Другие  1
```

- Зашел на сайт создал первый рецепт с фото

- Изменил количество записей в части пагинатора категорый рецептов с 2 до 5 в контроллере by_category

```
. . .
    paginator = Paginator(rss, 5)
. . .
```

- Добавил еще 4 рецепта без фото
- скопировал этот файл на сайт в папку с проектом
- Сохранил последние изменения на гитхаб

```
git add .
git commit -m "added the latest changes from the site"
git push
```

## 2024-05-11

### День 8

- Продолжил тестирование реализованного Backend-функционала
- Устранил замечание первых посетителей: Скрыть кнопку регистрации для зарегистрированных пользователей.
- Уменьшил размер шрифта в заголовке для смартфонов.
