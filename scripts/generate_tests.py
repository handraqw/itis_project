"""
Script for generating test cases during CI/CD.
"""
import sys
from pathlib import Path
from datetime import datetime

# Определяем путь к корню проекта
# Если скрипт лежит в project/scripts/generate_tests.py, то корень - это project/
BASE_DIR = Path(__file__).resolve().parent.parent

# Добавляем путь к корню проекта в sys.path ПЕРЕД импортом
sys.path.insert(0, str(BASE_DIR))

try:
    from src.generator import TestCaseGenerator
    from src.utils import export_to_json
except ImportError as e:
    print(f"❌ Error importing modules: {e}")
    print(f"Current sys.path: {sys.path}")
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"Contents of BASE_DIR: {list(BASE_DIR.iterdir())}")
    sys.exit(1)

def generate_all_test_sets():
    """Генерирует полные наборы тестов для всех типов задач."""
    # Путь для сохранения данных
    data_dir = BASE_DIR / 'data' / 'generated_tests'
    data_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    task_types = ['sorting', 'searching', 'data_structures', 'math']
    
    for task_type in task_types:
        print(f"\n{'='*50}")
        print(f"Generating tests for: {task_type}")
        print(f"{'='*50}")
        
        try:
            gen = TestCaseGenerator(task_type)
            test_cases = gen.generate(count=10, include_edge_cases=True)
            
            filename = data_dir / f'{task_type}_{timestamp}.json'
            export_to_json(test_cases, str(filename))
            
            print(f"✓ Generated {len(test_cases)} test cases for {task_type}")
            print(f"  Saved to: {filename}")
        except Exception as e:
            print(f"⚠️ Failed to generate tests for {task_type}: {e}")

if __name__ == '__main__':
    print("🚀 Starting Test Case Generation")
    print(f"  Time: {datetime.now()}")
    print(f"  Project Root: {BASE_DIR}")
    
    try:
        generate_all_test_sets()
        print("\n✅ Test generation completed successfully!")
    except Exception as e:
        print(f"\n❌ Critical error during test generation: {e}")
        sys.exit(1)
