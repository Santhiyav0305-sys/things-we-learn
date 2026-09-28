# Suggested solution for Day 29: Missing values and categorical features
    # Do not treat this as the only correct solution.

    from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
num=['age']; cat=['city']
pre=ColumnTransformer([('num',Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler())]),num),('cat',OneHotEncoder(handle_unknown='ignore'),cat)])
