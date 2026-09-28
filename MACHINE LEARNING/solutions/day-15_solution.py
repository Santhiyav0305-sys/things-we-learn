# Suggested solution for Day 15: Classification and logistic regression
    # Do not treat this as the only correct solution.

    from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
X=df[['hours_studied','attendance']]; y=(df['score']>=70).astype(int)
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
m=LogisticRegression().fit(Xtr,ytr); print(classification_report(yte,m.predict(Xte),zero_division=0))
