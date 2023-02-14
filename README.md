# django-orm-watching-storage
Пульт управления охраны банка.

### Настройка
Для настройки базы данных создайте файл `.env` рядом с `manage.py`.

Пример `.env`:
```
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_HOST=checkpoint.devman.org
DB_PORT=5534
DB_NAME=checkpoint
DB_USER=guarh
DB_PASSWORD=osim3
DB_DEBUG=false
DB_SECRET_KEY=sdf3fdsf3
DB_ALLOWED_HOSTS=*
```

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить
Сайт запускается командой:
```
python manage.py runserver 0.0.0.0:8000
```
Находится по адресу http://127.0.0.1:8000/
### Цель проекта

Код написан в  образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
