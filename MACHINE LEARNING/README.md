# Machine Learning From Scratch — 45-Day Guided Learning Repository

This repository turns the uploaded curriculum into a **beginner-friendly, hands-on 45-day ML program**.

## What you will learn

1. Python for Machine Learning
2. NumPy, Pandas, Matplotlib and EDA
3. Machine-learning concepts and terminology
4. Regression, classification, decision trees and K-Means
5. ML project organization, Git/GitHub and experiment tracking
6. Feature engineering, PCA, cross-validation and hyperparameter tuning
7. Reading research papers and implementing ideas
8. Neural networks, CNNs and RNN concepts
9. A complete capstone project

> The capstone is kept separate from the 45 training days, matching the curriculum image.

## How to use this repository

Study **one day at a time**:

1. Read `days/day-XX/lesson.md`
2. Run `days/day-XX/starter.py`
3. Complete `days/day-XX/exercises.md` without looking at the solution
4. Compare with `solutions/day-XX_solution.py`
5. Write down what you learned in `progress/`
6. Commit your work to Git

## Recommended setup

Python 3.11+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Run the checks:

```bash
python scripts/check_setup.py
```

Open Jupyter:

```bash
jupyter lab
```

## Git workflow

```bash
git init
git add .
git commit -m "Machine Learning"
git branch -M main
git remote add origin https://github.com/Santhiyav0305-sys/things-we-learn//tree/main/MACHINE%20LEARNING
git push -u origin main
```

## Repository map

```text
ml-from-scratch-45-day/
├── README.md
├── 45_DAY_ROADMAP.md
├── LEARNING_METHOD.md
├── requirements.txt
├── .gitignore
├── days/                  # 45 guided lessons
├── solutions/             # exercise solutions
├── notebooks/             # guided Jupyter notebooks
├── projects/              # mini-projects + capstone template
├── data/                  # small local practice datasets
├── src/                   # reusable ML utilities
├── tests/                 # simple tests
├── scripts/               # setup/check/helper scripts
├── progress/              # your daily learning log
└── references/            # cheat sheets and paper-reading guide
```

## Important rule

Do not try to memorize every API. Learn the workflow:

**Problem → Data → Inspect → Clean → Split → Baseline → Train → Evaluate → Improve → Explain → Reproduce**

Happy learning!
