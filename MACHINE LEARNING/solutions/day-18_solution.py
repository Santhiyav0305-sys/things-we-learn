# Suggested solution for Day 18: K-Means clustering
    # Do not treat this as the only correct solution.

    from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
X=df[['annual_income','spend_score']]
labels=KMeans(n_clusters=3,n_init=10,random_state=42).fit_predict(StandardScaler().fit_transform(X))
print(labels)
