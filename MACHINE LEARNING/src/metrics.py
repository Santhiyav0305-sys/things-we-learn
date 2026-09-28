def accuracy(y_true, y_pred):
    correct = sum(a == b for a, b in zip(y_true, y_pred))
    return correct / len(y_true)

def mean_absolute_error(y_true, y_pred):
    return sum(abs(a-b) for a, b in zip(y_true, y_pred)) / len(y_true)

def mean_squared_error(y_true, y_pred):
    return sum((a-b)**2 for a, b in zip(y_true, y_pred)) / len(y_true)
