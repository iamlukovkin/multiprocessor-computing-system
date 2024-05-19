<h1>multiprocessor computing system (MCS)</h1>
<h2>Исследование характеристик многопроцессорных вычислительных систем с общей памятью</h2>
<h3>Цель работы</h3>
<p>Целью данной работы являются определение характеристик многопроцессорных вычислительных систем (МВС) с общей памятью и исследование зависимости этих характеристик от числа процессоров и их быстродействия.</p>
<h3>Структура проекта</h3>

- [Контроллеры](src/main/controllers/__init__.py)
  - [Контроллер МВС](src/main/controllers/mcs_controller.py)
- [Модели](src/main/models/__init__.py)
  - [Составление графиков](src/main/models/graph.py)
  - [Модель МВС](src/main/models/mcs.py)
- [Графический интерфейс](src/main/views/__init__.py)
  - [Представление графиков](src/main/views/graphics_view.py)
  - [Вывод информации о МВС](src/main/views/mcs_view.py)
- [Запуск программы](main.py)
- [Описание приложения](src/application.py)
- [Результаты в таблицах xlsx](res/tables)

<h3>Установка приложения</h3>

Windows
```bash
python3 -m venv venv
pip install -r requirements.txt
venv/Scripts/activate
```

Linux/macOS
```bash
python3 -m venv venv
pip install -r requirements.txt
venv/bin/activate
```

<h3>Запуск приложения</h3>
```bash
python3 main.py
```