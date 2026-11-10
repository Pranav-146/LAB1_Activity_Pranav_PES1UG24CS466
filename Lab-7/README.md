# Lab 7: Fuzz Testing

**Student:** Pranav &bull; **SRN:** PES1UG24CS466  
**Assigned repo:** [SETAPESU26/L6_L7_42_salon_booking](https://github.com/SETAPESU26/L6_L7_42_salon_booking) (`Lab 7` folder)  
**Tools:** Python 3.12.0, Hypothesis 6.170.15, pytest 9.2.0

The handout calls the files `processor.py` and `test_processor.py`. In the assigned repo they are `salon_booking.py` and `test_salon_booking.py`.

## Results

| Run | Result |
|-----|--------|
| Original `salon_booking.py` | 10 failed, 2 passed |
| Fixed `salon_booking.py` | 12 passed (also with `--hypothesis-seed` 1 to 5) |

## Tests

The starter file had three empty test headers. Each function now has four Hypothesis tests:

- **no_crash**: any text, `None`, or a string built from tricky pieces (`nan`, `inf`, `1e400`, `-5`, separators, an Arabic digit) must not raise.
- **output_is_valid**: the result must be `None` (rejected) or a finite, in-range value.
- **valid_input**: well-formed input must still give the right answer, so rejecting everything cannot pass.
- **rejects_\***: zero or negative minutes and negative discounts must be rejected.

## Bugs found and fixed

| Function | Input found | Original behaviour | Fix |
|----------|-------------|--------------------|-----|
| All three | `None` | `AttributeError` on `.split` | Return `None` if input is not a string |
| `parse_booking` | `''` | `ValueError` on unpacking | Require exactly one `:` |
| `parse_booking` | `':'` | `ValueError` from `float('')` | Convert inside `try`/`except` |
| `parse_booking` | `'0:1E400'` | Returns `inf` minutes | Reject `nan` and `inf` |
| `parse_booking` | `'0:0'`, `'A:0'` | Accepts 0 minutes | Minutes must be above 0 and up to 1440 |
| `parse_booking` | `':0'` | Accepts an empty service name | Name must contain a letter |
| `duration_average` | `''` | `ValueError` from `int('')` | Convert inside `try`/`except` |
| `duration_average` | `'0'` | Average of 0 minutes | Each value must be 1 to 1440 |
| `payable_bill` | `''` | `ValueError` on unpacking | Require exactly one `\|` |
| `payable_bill` | `'\|'` | `ValueError` from `float('')` | Convert inside `try`/`except` |
| `payable_bill` | `'0\|-1E400'` | Returns `inf` | Reject `nan` and `inf` |
| `payable_bill` | `'0\|-1'` | Negative discount raises the bill | Amounts must be 0 to 10,000,000 |
| `payable_bill` | `'1\|1'` | `0.17999999999999994` | Round to 2 decimal places |

Invalid input now returns `None`, and `main()` prints what format is expected instead of crashing.

## Deliverables

| Deliverable | File |
|-------------|------|
| PDF with screenshots | [Lab_7_Fuzz_Testing_Report_PES1UG24CS466.pdf](Lab_7_Fuzz_Testing_Report_PES1UG24CS466.pdf) |
| Fixed script | [salon_booking.py](salon_booking.py) |
| Updated tests | [test_salon_booking.py](test_salon_booking.py) |
| Screenshots | [screenshots/](screenshots) |
| Full pytest output | [outputs/fuzz_before_fix.txt](outputs/fuzz_before_fix.txt), [outputs/fuzz_after_fix.txt](outputs/fuzz_after_fix.txt) |

The original script is in the first Lab 7 commit. The screenshots were drawn by a script from the real output of the commands below, rather than captured from a terminal window.

## Run it

```bash
pip install hypothesis pytest
python salon_booking.py
python -m pytest test_salon_booking.py
```
