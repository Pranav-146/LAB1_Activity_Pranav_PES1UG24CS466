# Lab 6: Code and Branch Coverage

**Student:** Pranav &bull; **SRN:** PES1UG24CS466  
**Assigned repo:** [SETAPESU26/L6_L7_42_salon_booking](https://github.com/SETAPESU26/L6_L7_42_salon_booking)  
**Tools:** Coverage.py 7.17.2, pytest 9.2.0

## Results for `salon_booking.py`

| Test file | Tests | Line coverage | Branch coverage |
|-----------|-------|---------------|-----------------|
| `test_salon_booking.py` (starter) | 2 | 38% | 32% (with `--branch`) |
| `CodeCoverageTest_PES1UG24CS466_salon_booking.py` | 12 | 100% | 98% (with `--branch`) |
| `BranchCoverageTest_PES1UG24CS466_salon_booking.py` | 44 | 100% | 100% |

The percentage with `--branch` counts lines and branches together, as Coverage.py does.

The code coverage tests run every line but miss branch `21->23`: an overrun of more than 60 minutes with a stylist who is not senior. This shows why 100% line coverage does not mean every path was tested. The branch coverage tests add that case, along with the exact boundary values for each decision.

## Deliverables

| Deliverable | File |
|-------------|------|
| Code coverage tests | [CodeCoverageTest_PES1UG24CS466_salon_booking.py](CodeCoverageTest_PES1UG24CS466_salon_booking.py) |
| Branch coverage tests | [BranchCoverageTest_PES1UG24CS466_salon_booking.py](BranchCoverageTest_PES1UG24CS466_salon_booking.py) |
| Code coverage output | [screenshots/code_coverage.png](screenshots/code_coverage.png) |
| Branch coverage output | [screenshots/branch_coverage.png](screenshots/branch_coverage.png) |

`salon_booking.py` and `test_salon_booking.py` are the original files, unchanged.

The two images were drawn by a script from the real output of the commands below, rather than captured from a terminal window.

## Test quality check

To confirm the tests check results and not just run lines, 18 small bugs were put into a temporary copy of the module, one at a time. The branch tests caught 17. The other changed `extra <= 0` to `extra < 0`, which makes no difference because an `extra` of 0 still gives a charge of 0.

## Run it

```bash
pip install coverage pytest
coverage run -m pytest CodeCoverageTest_PES1UG24CS466_salon_booking.py
coverage report -m
coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS466_salon_booking.py
coverage report -m
```
