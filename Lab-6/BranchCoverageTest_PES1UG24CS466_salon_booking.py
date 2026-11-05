"""Branch coverage tests for salon_booking.py: every decision goes both ways."""
import pytest
from salon_booking import extra_time_charge, can_book, arrival_status


@pytest.mark.parametrize("service", ["massage", "", "HAIRCUT"])
def test_unknown_service_raises(service):
    with pytest.raises(ValueError, match="unknown service"):
        extra_time_charge(service, 30, "junior", False)


def test_negative_duration_raises():
    with pytest.raises(ValueError, match="invalid duration"):
        extra_time_charge("haircut", -1, "junior", False)


@pytest.mark.parametrize(
    "service, duration, level, member, expected",
    [
        # No charge at or below the included time
        ("haircut", 0, "junior", False, 0),
        ("haircut", 30, "junior", False, 0),
        ("colour", 60, "senior", False, 0),
        ("spa", 90, "senior", False, 0),
        # Just over the included time
        ("haircut", 31, "junior", False, 10),
        ("haircut", 31, "senior", False, 18),
        # Members get 15 more minutes, except on spa
        ("haircut", 45, "junior", True, 0),
        ("haircut", 46, "junior", True, 10),
        ("colour", 75, "senior", True, 0),
        ("colour", 100, "senior", True, 450),
        ("spa", 100, "senior", True, 180),
        # Exactly 60 extra minutes has no long overrun surcharge
        ("haircut", 90, "junior", False, 600),
        ("haircut", 90, "senior", False, 1080),
        # Over 60 extra minutes: surcharge, plus more for senior only
        ("haircut", 91, "junior", False, 1098),
        ("haircut", 91, "senior", False, 1830),
        ("haircut", 91, "mid", False, 1586),
        ("haircut", 100, "senior", False, 2100),
    ],
)
def test_extra_time_charge(service, duration, level, member, expected):
    assert extra_time_charge(service, duration, level, member) == expected


@pytest.mark.parametrize(
    "party, services, walk_in, expected",
    [
        # Walk-ins depend only on party size
        (2, 1, True, True),
        (3, 1, True, False),
        (2, 5, True, True),
        # Bookings allow up to 4 people and 2 services
        (2, 1, False, True),
        (4, 2, False, True),
        (5, 1, False, False),
        (4, 3, False, False),
    ],
)
def test_can_book(party, services, walk_in, expected):
    assert can_book(party, services, walk_in) is expected


@pytest.mark.parametrize(
    "minutes, colour, weekend, expected",
    [
        # Weekday, not colour: cutoff 5
        (5, False, False, "open"),
        (4, False, False, "late"),
        (-10, False, False, "late"),
        (-11, False, False, "closed"),
        # Weekday, colour: cutoff 10
        (10, True, False, "open"),
        (9, True, False, "late"),
        (-5, True, False, "late"),
        (-6, True, False, "closed"),
        # Weekend, not colour: cutoff 15
        (15, False, True, "open"),
        (14, False, True, "late"),
        (0, False, True, "late"),
        (-1, False, True, "closed"),
        # Weekend, colour: cutoff 20
        (20, True, True, "open"),
        (19, True, True, "late"),
        (5, True, True, "late"),
        (4, True, True, "closed"),
    ],
)
def test_arrival_status(minutes, colour, weekend, expected):
    assert arrival_status(minutes, colour, weekend) == expected
