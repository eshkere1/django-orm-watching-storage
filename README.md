# Пульт охраны банка

Используя этот пульт-сайт, охранник банка :sunglasses: сможет видеть посещения хранилища, все активные карты доступа и их владельцев.

## Как установить

Python3.11 должен быть уже установлен. Если вас его нет, то следуйте рекомендациям [статьи по установке Python для Windows](https://docs.microsoft.com/ru-ru/windows/python/beginners#install-python).
Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```

## Переменные окружения

Создайте файл .env и добавте в него эти переменные со своими значениями:
SECRET_KEY="" (Секретный ключ для конкретной установки Django. Используется для обеспечения криптографической подписи, и его значение должно быть уникальным и непредсказуемым.)
DB_HOST="" (Список строк, представляющих имена хостов/доменов, которые может обслуживать этот сайт на Django. Это мера безопасности для предотвращения атак на заголовки HTTP-хостов, которые возможны даже при многих, казалось бы, безопасных конфигурациях веб-серверов.)
PASSWORD="пароль" 
DEBUG= true/false (Логическое значение, которое включает/выключает режим отладки. Если в вашем приложении возникает исключение, когда значение DEBUG равно True, Django отобразит подробную обратную трассировку, включающую множество метаданных о вашей среде, таких как все текущие настройки Django (из settings.py).)
DB_PORT="" (Порт, используется при подключении к базе данных. Пустая строка означает порт по умолчанию. Не используется с SQLite.)
DB_USER="" (Имя пользователя, используемое при подключении к базе данных. Не используется в SQLite.)
DB_NAME="" (имя используемой базы данных. Для SQLite это полный путь к файлу базы данных. При указании пути всегда используйте косую черту, даже в Windows (например, C:/homes/user/mysite/sqlite3.db).)
ALLOWED_HOSTS="" (Список строк, представляющих имена хостов/доменов, которые может обслуживать этот сайт Django. Это мера безопасности, предотвращающая атаки с использованием заголовка HTTP Host, которые возможны даже при многих, казалось бы, безопасных конфигурациях веб-серверов.)

## Запуск

Для запуска сервера используйте команду в папке проекта:
```
python manage.py runserver 127.0.0.1:8000
```
Вы увидите сообщение о том, что сервер запущен.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).