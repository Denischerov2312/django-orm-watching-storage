# django-orm-watching-storage
Пульт охраны банка.

### Настройка
В файле `project\settings.py` укажите параметры вашей базы данных. Пример:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': 'osim5',
    }
}
```
При необходимости измените другие настройки.


### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в  образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
