import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from website import create_app

app = create_app()