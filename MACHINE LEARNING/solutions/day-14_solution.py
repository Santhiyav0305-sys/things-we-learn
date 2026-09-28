# Suggested solution for Day 14: Linear regression
    # Do not treat this as the only correct solution.

    from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
X=df[['hours_studied']]; y=df['score']
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42)
m=LinearRegression().fit(Xtr,ytr); p=m.predict(Xte)
print(m.coef_,m.intercept_,mean_absolute_error(yte,p))
