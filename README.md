Запуск проекта:

        - склонируйте репозиторий: 
                git clone https://github.com/Deinekin/drf_cw.git;
        - активируйте poetry и установите зависимости:         
                poetry shell, 
                poetry install;
        - создайте базу данных в pgAdmin и заполните шаблон env.sample;
        - создайте и примените миграции:
                python manage.py makemigrations
                python manage.py migrate
        - запустите сервер:
                python manage.py runserver
