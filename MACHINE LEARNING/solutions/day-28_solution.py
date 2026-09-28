# Suggested solution for Day 28: Feature engineering
    # Do not treat this as the only correct solution.

    df['score_per_hour']=df['score']/df['hours_studied']
print(df[['score','hours_studied','score_per_hour']])
