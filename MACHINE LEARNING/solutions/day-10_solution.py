# Suggested solution for Day 10: Normalization and scaling
    # Do not treat this as the only correct solution.

    from sklearn.preprocessing import StandardScaler, MinMaxScaler
X=[[1,10],[2,20],[3,30]]
print(StandardScaler().fit_transform(X))
print(MinMaxScaler().fit_transform(X))
