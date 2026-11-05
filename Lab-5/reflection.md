# Lab 5 Reflection

The README asks for four reflection questions from the handout, but the handout does not list them. These are the usual questions for a static analysis lab.

## 1. Which issues were easiest to fix, and which were hardest? Why?

The style issues were easiest, such as `== None`, long lines, and missing docstrings. Each one has a single clear fix and does not change what the program does.

The hardest were `eval` and `grace_marks`. Removing `eval` meant changing how `compute_weighted_gpa` is called while keeping the GPA at 4.35. `grace_marks` was hard because the tools only said it was unused. They could not say whether to delete it or apply it, so I had to work out what the code was meant to do.

## 2. Did the tools report any false positives?

Partly. Bandit's MD5 warning (B324) depends on how the hash is used. If it were only a non-security label for a student id, MD5 would do no harm, although moving to SHA-256 cost nothing. B105 is a pattern match on the variable name, so it is only a guess, but here it was correct because the token really was hardcoded.

The tools also missed real problems. None of them noticed that the program printed the token, that marks above 100 were accepted, or that a student with no marks would crash it. A clean report does not prove the code is correct.

## 3. How would you integrate static analysis into your development workflow?

I would run Flake8 and Bandit in a pre-commit hook, so problems are caught before code is shared. I would also run all three tools in CI on every pull request and block merging on Bandit High or Medium findings or a Pylint score below an agreed level. Tests are still needed alongside them, because these tools do not check whether results are correct.

## 4. What improvements did you observe after fixing the issues?

- **Security:** there is no more `eval` or shell call, and the token is no longer in the code or the output. PINs now come from a secure generator.
- **Reliability:** bad input is rejected, a student with no marks no longer crashes the program, and errors are no longer silently ignored.
- **Readability:** every function has a docstring, naming is consistent, and the shared average calculation is in one place.
- **Output:** the grade sheet is now valid JSON that other programs can read.
- **Scores:** Pylint went from 5.51 to 10.00, and Bandit and Flake8 now report nothing.
