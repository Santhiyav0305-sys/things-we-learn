# Suggested solution for Day 30: Feature selection and importance
    # Do not treat this as the only correct solution.

    from sklearn.inspection import permutation_importance
result=permutation_importance(model,X_test,y_test,random_state=42)
print(result.importances_mean)
