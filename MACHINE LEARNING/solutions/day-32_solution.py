# Suggested solution for Day 32: Cross-validation
    # Do not treat this as the only correct solution.

    from sklearn.model_selection import cross_val_score
scores=cross_val_score(model,X,y,cv=5,scoring='r2')
print(scores.mean(),scores.std())
