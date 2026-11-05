# Lab 5: Static Code Analysis

**Student:** Pranav &bull; **SRN:** PES1UG24CS466  
**Assigned repo:** [SETAPESU26/L5_42_student_grade_system](https://github.com/SETAPESU26/L5_42_student_grade_system)  
**Tools:** Pylint 4.1.3, Bandit 1.9.4, Flake8 7.5.0

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.51/10 | 10.00/10 |
| Bandit | 6 issues (2 High, 1 Medium, 3 Low) | No issues |
| Flake8 | 8 issues | No issues |

No findings were hidden with `# nosec`, `# noqa`, or `# pylint: disable` comments.

## Deliverables

| Deliverable | File |
|-------------|------|
| Cleaned code | [student_grade_system.py](student_grade_system.py) |
| Issue table | [issues.md](issues.md) |
| Reflection | [reflection.md](reflection.md) |
| Reports before fixes | [reports/before](reports/before) |
| Reports after fixes | [reports/after](reports/after) |

## Commits

The history has one commit for each tool, as the handout requires. They are titled:

1. `Fix Bandit findings in student grade system`
2. `Fix Flake8 findings in student grade system`
3. `Fix Pylint findings in student grade system`

A further commit, `Fix logic bugs no tool reported`, covers the problems found by running and reading the code.

## Behaviour changes

- `compute_weighted_gpa` now takes a numeric `scale` (default `20.0`) instead of a text expression.
- `addGrade` is now `add_grade`, and marks must be between 0 and 100.
- A student passes if their average plus 5 grace marks reaches the threshold, so averages from 45 to 49.99 now pass.
- The grade sheet is written as JSON.
- The portal token comes from the `GRADE_PORTAL_TOKEN` environment variable and is never printed.

## Run it

```bash
python student_grade_system.py
```
