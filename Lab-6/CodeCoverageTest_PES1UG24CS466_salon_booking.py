"""Line coverage tests for salon_booking.py: every line runs at least once."""
import pytest
from salon_booking import extra_time_charge, can_book, arrival_status


def test_within_included_time():
    assert extra_time_charge("haircut", 20, "junior", False) == 0


def test_can_book():
    assert can_book(2, 1, False) is True


def test_unknown_service_raises():
    with pytest.raises(ValueError, match="unknown service"):
        extra_time_charge("massage", 30, "junior", False)


def test_negative_duration_raises():
    with pytest.raises(ValueError, match="invalid duration"):
        extra_time_charge("haircut", -1, "junior", False)


def test_member_gets_extra_included_time():
    # colour includes 60 + 15 for members, so 25 extra minutes at rate 18
    assert extra_time_charge("colour", 100, "senior", True) == 450


def test_junior_rate():
    # spa includes 90, so 10 extra minutes at rate 10
    assert extra_time_charge("spa", 100, "junior", False) == 100


def test_senior_long_overrun_rate():
    # 70 extra minutes at rate 18 + 8 + 4
    assert extra_time_charge("haircut", 100, "senior", False) == 2100


def test_walk_in_small_party():
    assert can_book(2, 1, True) is True


def test_large_party_rejected():
    assert can_book(5, 1, False) is False


def test_arrival_open_colour_weekend():
    assert arrival_status(20, True, True) == "open"


def test_arrival_late():
    assert arrival_status(0, False, False) == "late"


def test_arrival_closed():
    assert arrival_status(-20, False, False) == "closed"
