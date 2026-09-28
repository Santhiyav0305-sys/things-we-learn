from src.metrics import accuracy, mean_absolute_error, mean_squared_error

def test_accuracy():
    assert accuracy([1, 0, 1], [1, 1, 1]) == 2/3

def test_mae():
    assert mean_absolute_error([1, 2, 3], [2, 2, 5]) == 1

def test_mse():
    assert mean_squared_error([1, 2], [2, 4]) == 2.5
