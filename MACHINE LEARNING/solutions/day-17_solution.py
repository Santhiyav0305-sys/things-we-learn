# Suggested solution for Day 17: K-nearest neighbors
    # Do not treat this as the only correct solution.

    from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
m=make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors=5)).fit(Xtr,ytr)
print(m.score(Xte,yte))
