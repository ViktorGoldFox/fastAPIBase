fastAPIBase - это репозиторий-шаблон для создания fastAPI приложений с использованием SQLAlchemy.

Структура
fastAPIBase
└ ├ app
    ├ __init__.py
    └ V1
        └ crud.py (crud - create, rewritting, update, delete. Содержит взаимодействие с базой данных)
        └ views.py (ендпоинты)
   ├ core
       ├ __init__.py
       └ core_settings.py (содержит найстройки проекта через фраемворк pydantic_settings)
   ├ database
       ├ __init__.py (содержит класс дата базы с функциями взаимодействия)
       └ models.py (содержит таблицы базы данных)
   ├ entities
       └ __init__.py (содержит pydantic модели для fastAPI)
   ├ main.py (основной скрипт. Содержит инициализацию главного приложения fastAPI)
   ├ database.db База данных
