# Test Case Generator

![Build Status](https://github.com/your-username/test-case-generator/workflows/Tests%20and%20Code%20Quality/badge.svg)

## 📋 Description

**Test Case Generator** — это инструмент для автоматического генерирования тестовых случаев для различных типов заданий по программированию.

### Проблема
Преподавателям часто требуется создавать множество разнообразных тестовых случаев для проверки решений студентов. Это требует много времени и подвержено ошибкам.

### Решение
Этот инструмент позволяет:
- 🎯 Автоматически генерировать тестовые случаи для типичных алгоритмических задач
- ⚡ Создавать edge cases (граничные случаи)
- 📝 Экспортировать результаты в JSON формат для использования в фреймворках тестирования
- 🔄 Использовать с CI/CD для автоматической генерации тестов

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip или conda

### Setup

```bash
# Клонируйте репозиторий
git clone https://github.com/your-username/test-case-generator.git
cd test-case-generator

# Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Установите зависимости
pip install -r requirements.txt
```

## 💻 Usage

### Базовый пример: Генерация тестов для сортировки

```python
from src.generator import TestCaseGenerator

# Создаем генератор
gen = TestCaseGenerator(task_type='sorting')

# Генерируем 5 тестовых случаев
test_cases = gen.generate(count=5, include_edge_cases=True)

# Вывод первого теста
print(test_cases[0])
# Output:
# {
#     'input': [3, 1, 4, 1, 5, 9, 2, 6],
#     'expected_output': [1, 1, 2, 3, 4, 5, 6, 9],
#     'description': 'Array with 8 elements'
# }
```

### Расширенный пример: Генерация для поиска в массиве

```python
from src.generator import TestCaseGenerator
from src.utils import export_to_json

# Генератор для задачи поиска
gen = TestCaseGenerator(task_type='searching')

# Генерируем 10 тестов, включая edge cases
test_cases = gen.generate(count=10, include_edge_cases=True)

# Экспортируем в JSON
export_to_json(test_cases, 'test_cases_search.json')

print(f"Сгенерировано {len(test_cases)} тестовых случаев")
```

### Поддерживаемые типы задач

```python
# Сортировка
gen = TestCaseGenerator('sorting')

# Поиск в массиве
gen = TestCaseGenerator('searching')

# Работа с данными (структуры)
gen = TestCaseGenerator('data_structures')

# Математические вычисления
gen = TestCaseGenerator('math')
```

### Примеры вывода

**Пример 1: Сортировка (Sorting)**
```json
{
  "input": [64, 34, 25, 12, 22, 11, 90],
  "expected_output": [11, 12, 22, 25, 34, 64, 90],
  "difficulty": "medium",
  "description": "Random unsorted array"
}
```

**Пример 2: Поиск (Searching)**
```json
{
  "array": [1, 3, 5, 7, 9, 11, 13],
  "target": 7,
  "expected_output": 3,
  "difficulty": "easy",
  "description": "Binary search in sorted array"
}
```

**Пример 3: Edge Case (Граничный случай)**
```json
{
  "input": [],
  "expected_output": [],
  "difficulty": "edge_case",
  "description": "Empty array"
}
```

## 📁 Project Structure

```
test-case-generator/
├── src/
│   ├── __init__.py
│   ├── generator.py       # Основной генератор
│   ├── utils.py           # Утилиты для экспорта
│   └── templates/
│       ├── sorting.py     # Шаблоны для сортировки
│       ├── searching.py   # Шаблоны для поиска
│       └── math.py        # Шаблоны для математики
├── tests/
│   ├── __init__.py
│   ├── test_generator.py  # Тесты генератора
│   └── test_utils.py      # Тесты утилит
├── data/
│   └── sample_output.json # Пример выходных данных
├── docs/
│   └── EXAMPLES.md        # Расширенные примеры
├── .github/workflows/
│   └── generate-tests.yml # CI/CD workflow
├── requirements.txt
├── .gitignore
└── README.md
```

## 🧪 Testing

Запустить тесты:
```bash
pytest
```

Запустить с покрытием:
```bash
pytest --cov=src tests/
```

Результат:
```
========================= test session starts =========================
collected 12 items

tests/test_generator.py::test_sorting_generator PASSED         [ 8%]
tests/test_generator.py::test_searching_generator PASSED       [16%]
tests/test_generator.py::test_edge_cases PASSED                [25%]
tests/test_utils.py::test_export_json PASSED                   [33%]

========================= 12 passed in 0.45s =========================
```

## 📦 Requirements

- Python >= 3.8
- pytest >= 7.0.0
- pytest-cov >= 3.0.0
- flake8 >= 4.0.0
- black >= 22.0.0

## 🔄 CI/CD Pipeline

Этот проект использует **GitHub Actions** для автоматизации:

### Что делает pipeline:
✅ Запускает unit тесты на каждый push  
✅ Проверяет код на соответствие PEP 8 (flake8)  
✅ Генерирует отчет о покрытии (coverage)  
✅ **Ежедневно** генерирует свежие тестовые наборы в `data/generated_tests/`  
✅ Автоматически коммитит новые тесты обратно в репозиторий

### Как использовать:
- Push в `main` → автоматически запускаются тесты ✅
- Pull request → тесты и проверки качества обязательны ✓
- Каждый день в 6:00 UTC → генерируются новые наборы тестов 📅

Статус можно увидеть в **Actions** табе на GitHub.

## 💡 Примеры использования в реальных сценариях

### Сценарий 1: Проверка решений студентов
```python
# generate_for_student.py
from src.generator import TestCaseGenerator

def generate_student_tests(problem_type, student_id):
    """Генерирует уникальные тесты для каждого студента"""
    gen = TestCaseGenerator(problem_type)
    
    # Используем student_id как seed для воспроизводимости
    tests = gen.generate(count=5, seed=student_id)
    
    return tests

# Использование
tests = generate_student_tests('sorting', student_id=12345)
```

### Сценарий 2: Интеграция с тестовым фреймворком
```python
import json
from src.generator import TestCaseGenerator
from src.utils import export_to_json

def setup_test_suite():
    """Подготавливает полный набор тестов для CI/CD"""
    gen = TestCaseGenerator('searching')
    tests = gen.generate(count=15, include_edge_cases=True)
    
    # Экспортируем для использования в pytest
    export_to_json(tests, 'tests/test_data.json')
    
    return tests

setup_test_suite()
```

## 📊 Статистика проекта

- **Типы задач**: 4 (сортировка, поиск, структуры данных, математика)
- **Edge cases**: 6+ типов (пустой массив, один элемент, большие числа и т.д.)
- **Максимум тестов**: 1000+ за раз
- **Форматы экспорта**: JSON, YAML (планируется)

## 🤝 Contributing

Если вы хотите добавить новый тип задач:

1. Создайте новый файл в `src/templates/`
2. Реализуйте класс `TemplateGenerator`
3. Добавьте тесты в `tests/`
4. Обновите README

## 📝 License

MIT License - см. LICENSE файл

## 👤 Author

Студент, год 2025

## 📞 Support

Для вопросов создавайте Issues на GitHub.

---

**Последнее обновление**: 28.12.2025  
**Статус**: ✅ Production Ready