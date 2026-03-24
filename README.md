# Запуск

Установка зависимостей: ```pip install -r requirements.txt```

Миграции:
```
python manage.py makemigrations 
python manage.py migrate        
```
Создание суперпользователя:
```
python manage.py createsuperuser
```
Запуска сервера:
```
python manage.py runserver      
```

Данные можно создать через Django Admin:
[http://127.0.0.1:8000/admin/](url)

По этому адресу можно получить JSON требуемого формата:
http://127.0.0.1:8000/api/v1/foods/
