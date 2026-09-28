# Suggested solution for Day 31: PCA
    # Do not treat this as the only correct solution.

    from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
X_scaled=StandardScaler().fit_transform(X)
X_pca=PCA(n_components=2).fit_transform(X_scaled)
print(X_pca.shape)
