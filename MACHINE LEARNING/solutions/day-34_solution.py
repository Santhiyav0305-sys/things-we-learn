# Suggested solution for Day 34: Model evaluation and error analysis
    # Do not treat this as the only correct solution.

    errors=y_test-model.predict(X_test)
print(errors.sort_values().head())
