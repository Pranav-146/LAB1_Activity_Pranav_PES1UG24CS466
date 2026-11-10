"""Hypothesis fuzz tests for salon_booking.py (Lab 7).

Each function gets three kinds of test:
  * no_crash   - any text (or None) must never raise an exception.
  * output     - whatever comes back must be either None (input rejected)
                 or a sensible value (finite, positive, in range).
  * valid      - well-formed input must still give the right answer, so a
                 "fix" that rejects everything cannot pass.

The fixed module returns None for input it cannot use.
"""

import math

from hypothesis import given, settings, strategies as st

from salon_booking import parse_booking, duration_average, payable_bill

settings.register_profile("lab7", max_examples=300, deadline=None)
settings.load_profile("lab7")

MAX_MINUTES = 24 * 60

# Plain random text rarely contains "nan", "inf" or a lone separator, so we
# also build strings out of tokens that are known to trip up number parsing.
TOKENS = [
    "45", "30", "0", "-5", "+7", "3.5", "1e400", "-1e400", "nan", "inf",
    "-inf", "1_0", "٣", " ", "", ":", "|", ",", "haircut", "spa",
    "9" * 30,
]
tricky_text = st.lists(st.sampled_from(TOKENS), max_size=8).map("".join)
any_input = st.text() | st.none() | tricky_text

service_names = st.text(
    alphabet=st.characters(categories=("L",)), min_size=1, max_size=20
)
padding = st.text(alphabet=" ", max_size=3)
minutes_values = st.integers(1, MAX_MINUTES) | st.floats(
    min_value=0.01, max_value=MAX_MINUTES, allow_nan=False
)


# ---------------------------------------------------------------- parse_booking

@given(any_input)
def test_parse_booking_no_crash(s):
    try:
        parse_booking(s)
    except Exception as e:
        assert False, f"parse_booking crashed with: {e!r}"


@given(any_input)
def test_parse_booking_output_is_valid(s):
    result = parse_booking(s)
    if result is None:
        return
    service, minutes = result
    assert isinstance(service, str) and service.strip()
    assert math.isfinite(minutes), f"duration is not a real number: {minutes}"
    assert 0 < minutes <= MAX_MINUTES, f"duration out of range: {minutes}"


@given(padding, service_names, padding, minutes_values)
def test_parse_booking_valid_input(left, service, right, minutes):
    text = f"{left}{service}{right}:{minutes}"
    assert parse_booking(text) == (service.strip().title(), float(minutes))


@given(service_names, st.integers(max_value=0) | st.integers(min_value=MAX_MINUTES + 1))
def test_parse_booking_rejects_out_of_range_minutes(service, minutes):
    assert parse_booking(f"{service}:{minutes}") is None


# ------------------------------------------------------------- duration_average

@given(any_input)
def test_duration_average_no_crash(s):
    try:
        duration_average(s)
    except Exception as e:
        assert False, f"duration_average crashed with: {e!r}"


@given(any_input)
def test_duration_average_output_is_valid(s):
    result = duration_average(s)
    if result is None:
        return
    assert isinstance(result, int)
    assert 0 < result <= MAX_MINUTES, f"average out of range: {result}"


@given(st.lists(st.integers(1, MAX_MINUTES), min_size=1, max_size=20), padding)
def test_duration_average_valid_input(values, pad):
    csv = ",".join(f"{pad}{v}{pad}" for v in values)
    result = duration_average(csv)
    assert result == sum(values) // len(values)
    assert min(values) <= result <= max(values)


@given(st.lists(st.integers(1, MAX_MINUTES), max_size=5), st.integers(max_value=0))
def test_duration_average_rejects_non_positive(values, bad):
    csv = ",".join(str(v) for v in values + [bad])
    assert duration_average(csv) is None


# ----------------------------------------------------------------- payable_bill

@given(any_input)
def test_payable_bill_no_crash(s):
    try:
        payable_bill(s)
    except Exception as e:
        assert False, f"payable_bill crashed with: {e!r}"


@given(any_input)
def test_payable_bill_output_is_valid(s):
    result = payable_bill(s)
    if result is None:
        return
    assert math.isfinite(result), f"bill is not a real number: {result}"
    assert result >= 0, f"bill is negative: {result}"


@given(st.integers(0, 1_000_000), st.integers(0, 1_000_000))
def test_payable_bill_valid_input(bill, discount):
    result = payable_bill(f"{bill}|{discount}")
    assert result == round(max(bill * 1.18 - discount, 0), 2)
    assert result <= round(bill * 1.18, 2), "a discount must never raise the bill"


@given(st.integers(0, 1_000_000), st.integers(max_value=-1))
def test_payable_bill_rejects_negative_discount(bill, discount):
    assert payable_bill(f"{bill}|{discount}") is None
