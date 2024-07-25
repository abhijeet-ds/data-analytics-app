import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.analysis import run_analysis

def test_run_analysis():
    results = run_analysis()
    assert 'mean' in results
    assert results['mean'] > 0
