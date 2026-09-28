# Suggested solution for Day 38: Neural-network intuition
    # Do not treat this as the only correct solution.

    import numpy as np
x=np.array([2.,3.]); w=np.array([.5,-.2]); b=.1
z=x@w+b
print('neuron pre-activation:',z,'relu:',max(0,z))
