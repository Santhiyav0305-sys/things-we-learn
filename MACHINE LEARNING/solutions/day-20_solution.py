# Suggested solution for Day 20: Metrics and model comparison
    # Do not treat this as the only correct solution.

    from sklearn.metrics import mean_absolute_error, mean_squared_error
import math
print(mean_absolute_error([1,2,3],[2,2,5]))
print(math.sqrt(mean_squared_error([1,2,3],[2,2,5])))
