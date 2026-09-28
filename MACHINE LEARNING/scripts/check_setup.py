def check(name, fn):
    try:
        fn()
        print(f"[OK] {name}")
    except Exception as exc:
        print(f"[FAIL] {name}: {exc}")

check("Python", lambda: __import__("sys").version)
check("NumPy", lambda: __import__("numpy").__version__)
check("Pandas", lambda: __import__("pandas").__version__)
check("Matplotlib", lambda: __import__("matplotlib").__version__)
check("scikit-learn", lambda: __import__("sklearn").__version__)
check("joblib", lambda: __import__("joblib").__version__)
print("Setup check complete.")
