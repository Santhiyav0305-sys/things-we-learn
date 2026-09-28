# Suggested solution for Day 03: Functions and modules
    # Do not treat this as the only correct solution.

    def normalize_0_1(values):
    lo, hi=min(values), max(values)
    return [(x-lo)/(hi-lo) for x in values]
print(normalize_0_1([10,20,30]))
