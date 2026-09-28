# Suggested solution for Day 13: Train/validation/test and leakage
    # Do not treat this as the only correct solution.

    from sklearn.model_selection import train_test_split
X=df[['hours_studied','attendance']]; y=df['score']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42)
