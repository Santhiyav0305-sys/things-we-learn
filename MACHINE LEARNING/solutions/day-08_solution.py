# Suggested solution for Day 08: Matplotlib visualization
    # Do not treat this as the only correct solution.

    import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data/student_scores.csv')
plt.scatter(df['hours_studied'], df['score'])
plt.xlabel('Hours studied'); plt.ylabel('Score'); plt.title('Study hours vs score'); plt.show()
