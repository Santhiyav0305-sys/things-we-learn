# Suggested solution for Day 33: Hyperparameter tuning
    # Do not treat this as the only correct solution.

    from sklearn.model_selection import GridSearchCV
search=GridSearchCV(model,{'max_depth':[1,2,3,5,None]},cv=5)
# search.fit(X,y); print(search.best_params_)
