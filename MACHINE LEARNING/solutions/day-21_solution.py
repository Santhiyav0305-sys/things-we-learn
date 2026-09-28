# Suggested solution for Day 21: ML project folder structure
    # Do not treat this as the only correct solution.

    from pathlib import Path
for p in ['data','src','notebooks','tests','reports','models']:
    Path(p).mkdir(exist_ok=True)
