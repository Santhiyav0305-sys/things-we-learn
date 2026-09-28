# Suggested solution for Day 09: Exploratory Data Analysis
    # Do not treat this as the only correct solution.

    print(df.describe(include='all'))
print(df.isna().sum())
print(df.corr(numeric_only=True)['score'].sort_values())
