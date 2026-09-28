# Suggested solution for Day 06: Pandas Series and DataFrames
    # Do not treat this as the only correct solution.

    import pandas as pd
df=pd.read_csv('data/student_scores.csv')
print(df['score'].mean())
