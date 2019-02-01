
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades) == 0
