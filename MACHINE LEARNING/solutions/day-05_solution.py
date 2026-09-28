# Suggested solution for Day 05: NumPy arrays
    # Do not treat this as the only correct solution.

    import numpy as np
x=np.array([1,2,3,4,5], dtype=float)
print((x-x.mean())/x.std())
