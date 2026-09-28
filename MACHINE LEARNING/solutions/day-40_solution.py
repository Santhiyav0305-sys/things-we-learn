# Suggested solution for Day 40: Build a tiny neural network with NumPy
    # Do not treat this as the only correct solution.

    import numpy as np
rng=np.random.default_rng(0)
X=rng.normal(size=(100,2)); y=(X[:,0]+X[:,1]>0).astype(int)
W=rng.normal(size=(2,1)); b=0.0
for _ in range(1000):
    z=X@W+b; p=1/(1+np.exp(-z))
    gradW=X.T@(p-y[:,None])/len(y); gradb=(p-y[:,None]).mean()
    W-=0.1*gradW; b-=0.1*gradb
print('trained')
