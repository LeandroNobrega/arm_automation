from .sort_package import sort
from .constants import REJECTED, SPECIAL, STANDARD

def test_standard_package():
    assert sort(50, 50, 50, 10) == STANDARD

def test_bulky_by_volume():
    assert sort(90, 120, 100, 10) == SPECIAL

def test_bulky_by_dimension():
    assert sort(150, 20, 20, 10) == SPECIAL

def test_heavy_package():
    assert sort(50, 50, 50, 20) == SPECIAL

def test_rejected_package():
    assert sort(200, 200, 200, 25) == REJECTED

def test_edge_mass_exact_limit():
    assert sort(10, 10, 10, 20) == SPECIAL

def test_bulky_exact_limit():
    assert sort(100, 100, 100, 10) == SPECIAL

def test_null_value():
    try:
        sort(0, 100, 100, 10)
    except ValueError:
        pass

def test_negavtive_value():
    try:
        sort(-10, 100, 100, 10)
    except ValueError:
        pass

def test_wrong_input():
    try:
        sort("0", 100, 100, 10)
    except TypeError:
        pass
