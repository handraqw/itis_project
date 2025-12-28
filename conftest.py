"""
Pytest configuration and fixtures.
"""

import sys
from pathlib import Path

# Добавим корнь проекта в sys.path
# Это необходимо для корректного импорта модулей из src/
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
