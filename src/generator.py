"""
Test Generator - Main module for generating test cases.
"""

import random
from typing import List, Dict, Any, Optional


class TestCaseGenerator:
    """
    Генератор тестовых случаев для различных типов задач.
    
    Поддерживаемые типы задач:
    - 'sorting': сортировка массивов
    - 'searching': поиск в массиве
    - 'data_structures': работа со структурами данных
    - 'math': математические вычисления
    """
    
    def __init__(self, task_type: str):
        """
        Инициализация генератора.
        
        Args:
            task_type: тип задачи ('sorting', 'searching', 'data_structures', 'math')
        """
        self.task_type = task_type
        self.supported_tasks = {
            'sorting': self._generate_sorting_test,
            'searching': self._generate_searching_test,
            'data_structures': self._generate_data_struct_test,
            'math': self._generate_math_test
        }
        
        if task_type not in self.supported_tasks:
            raise ValueError(f"Unsupported task type: {task_type}")
    
    def generate(
        self,
        count: int = 5,
        include_edge_cases: bool = True,
        seed: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Генерирует тестовые случаи.
        
        Args:
            count: количество тестов
            include_edge_cases: включать ли граничные случаи
            seed: seed для воспроизводимости
            
        Returns:
            Список тестовых случаев
        """
        if seed is not None:
            random.seed(seed)
        
        test_cases = []
        generator_func = self.supported_tasks[self.task_type]
        
        # Генерируем обычные тесты
        regular_count = count - 2 if include_edge_cases else count
        for _ in range(regular_count):
            test_cases.append(generator_func())
        
        # Добавляем edge cases
        if include_edge_cases and count > 2:
            test_cases.extend(self._generate_edge_cases())
        
        return test_cases[:count]
    
    def _generate_sorting_test(self) -> Dict[str, Any]:
        """Генерирует тест для задачи сортировки."""
        size = random.randint(5, 20)
        arr = [random.randint(-100, 100) for _ in range(size)]
        
        return {
            'input': arr,
            'expected_output': sorted(arr),
            'difficulty': 'medium',
            'description': f'Array with {size} elements (random order)'
        }
    
    def _generate_searching_test(self) -> Dict[str, Any]:
        """Генерирует тест для задачи поиска."""
        size = random.randint(5, 20)
        arr = sorted([random.randint(1, 100) for _ in range(size)])
        target = arr[random.randint(0, len(arr) - 1)]
        
        return {
            'array': arr,
            'target': target,
            'expected_output': arr.index(target),
            'difficulty': 'medium',
            'description': 'Binary search in sorted array'
        }
    
    def _generate_data_struct_test(self) -> Dict[str, Any]:
        """Генерирует тест для задачи со структурами данных."""
        test_type = random.choice(['list_sum', 'unique_elements', 'max_element'])
        
        if test_type == 'list_sum':
            arr = [random.randint(1, 50) for _ in range(random.randint(3, 10))]
            return {
                'input': arr,
                'expected_output': sum(arr),
                'difficulty': 'easy',
                'description': 'Sum of array elements'
            }
        elif test_type == 'unique_elements':
            arr = [random.randint(1, 10) for _ in range(random.randint(5, 15))]
            return {
                'input': arr,
                'expected_output': len(set(arr)),
                'difficulty': 'easy',
                'description': 'Count unique elements'
            }
        else:  # max_element
            arr = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
            return {
                'input': arr,
                'expected_output': max(arr),
                'difficulty': 'easy',
                'description': 'Find maximum element'
            }
    
    def _generate_math_test(self) -> Dict[str, Any]:
        """Генерирует тест для математической задачи."""
        test_type = random.choice(['fibonacci', 'factorial', 'prime_check'])
        
        if test_type == 'fibonacci':
            n = random.randint(5, 10)
            return {
                'n': n,
                'expected_output': self._fibonacci(n),
                'difficulty': 'medium',
                'description': f'Fibonacci number at position {n}'
            }
        elif test_type == 'factorial':
            n = random.randint(3, 10)
            return {
                'n': n,
                'expected_output': self._factorial(n),
                'difficulty': 'easy',
                'description': f'Factorial of {n}'
            }
        else:  # prime_check
            num = random.randint(2, 100)
            return {
                'n': num,
                'expected_output': self._is_prime(num),
                'difficulty': 'medium',
                'description': f'Check if {num} is prime'
            }
    
    def _generate_edge_cases(self) -> List[Dict[str, Any]]:
        """Генерирует граничные случаи."""
        if self.task_type == 'sorting':
            return [
                {
                    'input': [],
                    'expected_output': [],
                    'difficulty': 'edge_case',
                    'description': 'Empty array'
                },
                {
                    'input': [1],
                    'expected_output': [1],
                    'difficulty': 'edge_case',
                    'description': 'Single element'
                }
            ]
        elif self.task_type == 'searching':
            return [
                {
                    'array': [],
                    'target': 1,
                    'expected_output': -1,
                    'difficulty': 'edge_case',
                    'description': 'Empty array'
                },
                {
                    'array': [5],
                    'target': 5,
                    'expected_output': 0,
                    'difficulty': 'edge_case',
                    'description': 'Single element (found)'
                }
            ]
        else:
            return []
    
    @staticmethod
    def _fibonacci(n: int) -> int:
        """Вычисляет n-е число Фибоначчи."""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def _factorial(n: int) -> int:
        """Вычисляет факториал n."""
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def _is_prime(n: int) -> bool:
        """Проверяет, является ли число простым."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True