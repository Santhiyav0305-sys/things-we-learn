# Suggested solution for Day 07: Data cleaning
    # Do not treat this as the only correct solution.

    df['score']=pd.to_numeric(df['score'], errors='coerce')
df=df.drop_duplicates()
df['score']=df['score'].fillna(df['score'].median())
