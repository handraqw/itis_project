"""
Utility functions for Test Case Generator.
"""

import json
from typing import List, Dict, Any


def export_to_json(
    test_cases: List[Dict[str, Any]],
    filename: str = 'test_cases.json'
) -> None:
    """
    Экспортирует тестовые случаи в JSON файл.
    
    Args:
        test_cases: список тестовых случаев
        filename: имя файла для сохранения
    """
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=2)
    print(f"✓ Exported {len(test_cases)} test cases to {filename}")


def load_from_json(filename: str) -> List[Dict[str, Any]]:
    """
    Загружает тестовые случаи из JSON файла.
    
    Args:
        filename: имя файла для загрузки
        
    Returns:
        Список тестовых случаев
    """
    with open(filename, 'r') as f:
        test_cases = json.load(f)
    print(f"✓ Loaded {len(test_cases)} test cases from {filename}")
    return test_cases


def print_test_case(test_case: Dict[str, Any], index: int = 0) -> None:
    """
    Красиво выводит тестовый случай.
    
    Args:
        test_case: тестовый случай
        index: номер тестового случая
    """
    print(f"\n{'='*50}")
    print(f"Test Case #{index + 1}")
    print(f"{'='*50}")
    for key, value in test_case.items():
        print(f"{key:20s}: {value}")


def validate_test_cases(
    test_cases: List[Dict[str, Any]],
    required_fields: List[str]
) -> bool:
    """
    Проверяет, что все тестовые случаи содержат требуемые поля.
    
    Args:
        test_cases: список тестовых случаев
        required_fields: список требуемых полей
        
    Returns:
        True, если все тесты валидны
    """
    for i, test in enumerate(test_cases):
        for field in required_fields:
            if field not in test:
                print(f"✗ Test case #{i + 1} missing field: {field}")
                return False
    print(f"✓ All {len(test_cases)} test cases are valid")
    return True