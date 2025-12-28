"""
Unit tests for Test Case Generator.
"""

import pytest
from src.generator import TestCaseGenerator

class TestSortingGenerator:
    """Тесты для генератора сортировки."""
    
    def test_sorting_generation_count(self):
        """Проверяет, что генерируется правильное количество тестов."""
        gen = TestCaseGenerator('sorting')
        tests = gen.generate(count=5, include_edge_cases=False)
        assert len(tests) == 5
    
    def test_sorting_has_required_fields(self):
        """Проверяет наличие всех требуемых полей."""
        gen = TestCaseGenerator('sorting')
        tests = gen.generate(count=1, include_edge_cases=False)
        test = tests[0]
        
        assert 'input' in test
        assert 'expected_output' in test
        assert 'description' in test
        assert 'difficulty' in test
    
    def test_sorting_output_is_sorted(self):
        """Проверяет, что ожидаемый результат отсортирован."""
        gen = TestCaseGenerator('sorting')
        tests = gen.generate(count=3, include_edge_cases=False)
        
        for test in tests:
            expected = test['expected_output']
            assert expected == sorted(expected)
    
    def test_sorting_with_edge_cases(self):
        """Проверяет генерирование edge cases."""
        gen = TestCaseGenerator('sorting')
        tests = gen.generate(count=5, include_edge_cases=True)
        
        # Должны быть edge cases
        assert any(t['difficulty'] == 'edge_case' for t in tests)


class TestSearchingGenerator:
    """Тесты для генератора поиска."""
    
    def test_searching_generation_count(self):
        """Проверяет количество тестов."""
        gen = TestCaseGenerator('searching')
        tests = gen.generate(count=3, include_edge_cases=False)
        assert len(tests) == 3
    
    def test_searching_has_required_fields(self):
        """Проверяет наличие требуемых полей."""
        gen = TestCaseGenerator('searching')
        tests = gen.generate(count=1, include_edge_cases=False)
        test = tests[0]
        
        assert 'array' in test
        assert 'target' in test
        assert 'expected_output' in test
    
    def test_searching_target_exists(self):
        """Проверяет, что цель всегда в массиве."""
        gen = TestCaseGenerator('searching')
        tests = gen.generate(count=5, include_edge_cases=False)
        
        for test in tests:
            array = test['array']
            target = test['target']
            expected = test['expected_output']
            
            assert array[expected] == target


class TestDataStructuresGenerator:
    """Тесты для генератора структур данных."""
    
    def test_data_struct_generation_count(self):
        """Проверяет количество тестов."""
        gen = TestCaseGenerator('data_structures')
        tests = gen.generate(count=4, include_edge_cases=False)
        assert len(tests) == 4
    
    def test_data_struct_has_required_fields(self):
        """Проверяет наличие требуемых полей."""
        gen = TestCaseGenerator('data_structures')
        tests = gen.generate(count=1, include_edge_cases=False)
        test = tests[0]
        
        assert 'input' in test
        assert 'expected_output' in test
        assert 'description' in test


class TestMathGenerator:
    """Тесты для генератора математики."""
    
    def test_math_generation_count(self):
        """Проверяет количество тестов."""
        gen = TestCaseGenerator('math')
        tests = gen.generate(count=3, include_edge_cases=False)
        assert len(tests) == 3
    
    def test_math_has_required_fields(self):
        """Проверяет наличие требуемых полей."""
        gen = TestCaseGenerator('math')
        tests = gen.generate(count=1, include_edge_cases=False)
        test = tests[0]
        
        assert 'n' in test
        assert 'expected_output' in test
        assert 'description' in test


class TestCaseGeneratorErrors:
    """Тесты для ошибок генератора."""
    
    def test_invalid_task_type(self):
        """Проверяет обработку неверного типа задачи."""
        with pytest.raises(ValueError):
            TestCaseGenerator('invalid_task')
    
    def test_generator_reproducibility(self):
        """Проверяет воспроизводимость с seed."""
        gen1 = TestCaseGenerator('sorting')
        gen2 = TestCaseGenerator('sorting')
        
        tests1 = gen1.generate(count=3, seed=42)
        tests2 = gen2.generate(count=3, seed=42)
        
        assert tests1[0]['input'] == tests2[0]['input']
        assert tests1[0]['expected_output'] == tests2[0]['expected_output']