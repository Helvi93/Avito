# Python

Перед запуском тестов необходимо установить библиотеки. Сделать это можно при помощи команды

    pip install -r requirements.txt    


---


Для запуск тестов с помощью Pytest необходимо ввести команду

    python -m pytest -sv


Для запуска определенного теста необходимо ввести путь к файлу с тестом. Например:

    python -m pytest -sv .\Ecercise_2\tests\zero_value\test_zero_value.py
