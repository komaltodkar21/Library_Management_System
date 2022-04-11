# Library_Management_System

Create Virtual Environment in powershell:
       * python -m venv env

In Command Prompt:
.\env\Scripts\activate

Required Installations:
* pip install django

Required Commands:
django-admin startproject MyApi --> <to start new project>
cd MyApi
django-admin startapp firstapp --> <to start new application>

-- In settings.py --INSTALLED_APPS include:
'book'

-- Create models.py and admin.py:

Required Commands:
* pip manage.py makemigrations
* pip manage.py migrate
* pip manage.py createsuperuser
* pip manage.py runserver


Requirements for frontend:
HTML, CSS, Bootstrap, Django Templating Language

-- Create template files and static files
-- Create views.py file and MyApi/urls.py:

# In order to see Library Management System using Django:
Required Command:
* pip manage.py runserver


Required Installations for Django Rest API Implementation:
* pip install djangorestframework

-- In settings.py --INSTALLED_APPS include:
'rest_framework'

-- Create serializers.py and views.py and urls.py:


-- In settings.py:
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES':[
        # 'rest_framework.permissions.AllowAny'
        # 'rest_framework.permissions.IsAuthenticated'
        'rest_framework.permissions.IsAdminUser'
    ]
}

# In order to see Rest framework for Library Management System:
In MyApi/urls.py run these two urlpatterns and comment others-
path('admin/', admin.site.urls),
path('', include('book.urls')),



Required Installations to store data in MySql database:
pip install mysqlclient

-- In settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_library',
        'USER': 'root',  
        'PASSWORD': 'root',  
        'HOST': '127.0.0.1',  
        'PORT': '3306'
    }
}
    
Required Commands:
* pip manage.py makemigrations
* pip manage.py migrate
* pip manage.py createsuperuser
* pip manage.py runserver

## In MySql Commandline client run following queries:
1. CREATE DATABASE my_library;
2. SHOW DATABASES;
3. USE my_libray;
4. SHOW TABLES;
5. SELECT * FROM auth_user;
6. INSERT INTO auth_user VALUES(1,'admin1234',null,true,"komal","Komal","Todkar","komal@gmail.com",true,true,"2022-04-09");
7. SELECT * FROM book_book;
8. INSERT INTO book_book VALUES(1,'Good Life Good Vibes','Vex King','Self-help book');
9. INSERT INTO book_book VALUES(2,'Becoming','Michelle Obama','Biography');
10. INSERT INTO book_book VALUES(3,'The Lost City','Amanda Hocking','Non-friction');
