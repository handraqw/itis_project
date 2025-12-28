"""
Script for generating test cases during CI/CD.
"""

import sys
sys.path.insert(0, '.')

from generator import TestCaseGenerator
from utils import export_to_json
import os
from datetime import datetime


def generate_all_test_sets():
    """Генерирует полные наборы тестов для всех типов задач."""
    
    os.makedirs('data/generated_tests', exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    task_types = ['sorting', 'searching', 'data_structures', 'math']
    
    for task_type in task_types:
        print(f"\n{'='*50}")
        print(f"Generating tests for: {task_type}")
        print(f"{'='*50}")
        
        gen = TestCaseGenerator(task_type)
        test_cases = gen.generate(count=10, include_edge_cases=True)
        
        filename = f'data/generated_tests/{task_type}_{timestamp}.json'
        export_to_json(test_cases, filename)
        
        print(f"✓ Generated {len(test_cases)} test cases for {task_type}")
        print(f"  Saved to: {filename}")


if __name__ == '__main__':
    print("🚀 Starting Test Case Generation")
    print(f"   Time: {datetime.now()}")
    
    try:
        generate_all_test_sets()
        print("\n✅ Test generation completed successfully!")
    except Exception as e:
        print(f"\n❌ Error during test generation: {e}")
        sys.exit(1)