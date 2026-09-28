# Suggested solution for Day 19: Overfitting, underfitting and regularization
    # Do not treat this as the only correct solution.

    from sklearn.tree import DecisionTreeClassifier
for depth in [1,3,None]:
    m=DecisionTreeClassifier(max_depth=depth,random_state=42).fit(Xtr,ytr)
    print(depth,m.score(Xtr,ytr),m.score(Xte,yte))
