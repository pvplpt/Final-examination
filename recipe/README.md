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
