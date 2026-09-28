# Suggested solution for Day 16: Decision trees
    # Do not treat this as the only correct solution.

    from sklearn.tree import DecisionTreeClassifier
m=DecisionTreeClassifier(max_depth=3,random_state=42).fit(Xtr,ytr)
print(m.score(Xte,yte))
