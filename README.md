<h1>multiprocessor computing system (MCS)</h1>
<h2>Исследование характеристик многопроцессорных вычислительных систем с общей памятью</h2>
<h3>Цель работы</h3>
<p>Целью данной работы являются определение характеристик многопроцессорных вычислительных систем (МВС) с общей памятью и исследование зависимости этих характеристик от числа процессоров и их быстродействия.</p>
<h3>Структура проекта</h3>

- [Контроллеры](src/controllers/__init__.py)
  - [Контроллер МВС](src/controllers/mcs_controller.py)
- [Модели](src/models/__init__.py)
  - [Составление графиков](src/models/graph.py)
  - [Модель МВС](src/models/mcs.py)
- [Графический интерфейс](src/views/__init__.py)
  - [Представление графиков](src/views/graphics_view.py)
  - [Вывод информации о МВС](src/views/mcs_view.py)
- [Запуск программы](main.py)
- [Описание приложения](src/application.py)

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