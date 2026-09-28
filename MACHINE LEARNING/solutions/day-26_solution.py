# Suggested solution for Day 26: Experiment tracking
    # Do not treat this as the only correct solution.

    import json
experiment={'model':'tree','max_depth':3,'metric':'accuracy','score':0.83}
print(json.dumps(experiment,indent=2))
