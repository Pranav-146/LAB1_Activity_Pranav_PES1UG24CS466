# Lab 5 Issue Table

Line numbers refer to the original `student_grade_system.py`. Severity is Bandit's rating where Bandit reported the issue.

## Security issues (Bandit)

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Shell command injection (B605) | Security, High | 60 | `os.system` passed `filename` to a shell, so a crafted filename could run commands | Removed the shell call and used `print` |
| Weak MD5 hash (B324) | Security, High | 49 | MD5 is broken and should not be used for identifiers that need to be trustworthy | Switched to `hashlib.sha256` |
| Use of `eval` (B307, W0123) | Security, Medium | 44 | `eval(gpa_expr)` runs any Python code passed to it | Replaced the expression with a numeric `scale` parameter, keeping the result at 4.35 |
| Predictable PIN (B311) | Security, Low | 53 | `random` is not safe for generating PINs | Used `secrets.randbelow`, which keeps the 1000 to 9999 range |
| Hardcoded token (B105) | Security, Low | 64 | The portal token was stored in the source code | Read it from the `GRADE_PORTAL_TOKEN` environment variable |
| Errors silently ignored (B110, W0702, E722) | Security / Bug, Low | 26-27 | Bare `except: pass` hid every error, including unknown student ids | Replaced with an explicit check that returns `False` |

## Bugs and quality issues (Pylint, Flake8)

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Mutable default argument (W0102) | Bug | 15 | `grade_list=[]` was shared across every call | Default to `None` and create the list inside the function |
| Unused grace marks (W0612, F841) | Bug | 31 | `grace_marks` was set but never used in the pass check | Applied it: `average + grace_marks >= pass_threshold` |
| Unused import (W0611, F401) | Quality | 6 | `json` was imported but never used, and the grade sheet was written with `str()` | Used `json.dump`, so the sheet is now valid JSON |
| File handling (R1732, W1514) | Quality | 57-59 | The file would stay open after an error, and no encoding was set | Used `with open(..., encoding="utf-8")` |
| `== None` comparison (C0121, E711) | Style | 32 | `None` should be compared with `is` | Changed to `is None` |
| Redundant if/else (R1703, R1705) | Style | 35-38 | The `if` returned `True` or `False` directly | Return the comparison itself |
| Function name (C0103) | Style | 15 | `addGrade` was not snake_case | Renamed to `add_grade` |
| Old string formatting (C0209) | Style | 19 | Used `%` formatting | Changed to an f-string |
| Missing docstrings (C0116) | Style | 15, 23, 30, 41, 48, 52, 56, 63 | No function had a docstring | Added a docstring to each function |
| Long lines (E501) | Style | 19, 34 | Lines were over 79 characters | Shortened them |
| Missing final newline (C0304, W292) | Style | 75 | The file did not end with a newline | Added one |

## Problems no tool reported

The README warned that not every problem would be flagged. These came from running the program and reading the code.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Secret printed to the console | Security | 72 | The program printed the full portal token | It now prints only whether a token is configured |
| No upper limit on marks | Bug | 16 | Marks above 100 were accepted, such as 150 | Added `MAX_MARK = 100` and a range check |
| Crash on empty marks | Bug | 34, 43 | A student with no marks caused `ZeroDivisionError` | Added `average_mark`, which handles an empty list |
| Decimal marks cut off in the log | Bug | 19 | `%d` logged 92.5 as 92 | The f-string logs the exact mark |
| Code ran on import | Bug | 75 | `main()` ran whenever the module was imported | Added an `if __name__ == "__main__":` guard |

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.51/10 | 10.00/10 |
| Bandit | 6 issues (2 High, 1 Medium, 3 Low) | No issues |
| Flake8 | 8 issues | No issues |
