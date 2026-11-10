import math

MAX_MINUTES = 24 * 60          # no single service can take longer than a day
MAX_AMOUNT = 10_000_000        # upper limit for a bill or discount, in rupees
GST_RATE = 1.18


def _to_number(text):
    """Return text as a finite float, or None if it is not a real number."""
    try:
        value = float(text)
    except ValueError:
        return None
    return value if math.isfinite(value) else None


def parse_booking(text):
    """'service:minutes' -> (Service, minutes), or None if the input is invalid."""
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    service = parts[0].strip()
    minutes = _to_number(parts[1])
    if not any(ch.isalpha() for ch in service):
        return None
    if minutes is None or not 0 < minutes <= MAX_MINUTES:
        return None
    return service.title(), minutes


def duration_average(durations_csv):
    """'30,45,60' -> whole-minute average, or None if any value is invalid."""
    if not isinstance(durations_csv, str):
        return None
    values = []
    for part in durations_csv.split(','):
        try:
            value = int(part)
        except ValueError:
            return None
        if not 0 < value <= MAX_MINUTES:
            return None
        values.append(value)
    return sum(values) // len(values)


def payable_bill(text):
    """'bill|discount' -> bill with GST minus discount, or None if invalid."""
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    bill = _to_number(parts[0])
    discount = _to_number(parts[1])
    if bill is None or discount is None:
        return None
    if not 0 <= bill <= MAX_AMOUNT or not 0 <= discount <= MAX_AMOUNT:
        return None
    total = bill * GST_RATE - discount
    return round(max(total, 0), 2)


def main():
    print("==== Running parse_booking ====")
    user_input = input("Enter service:duration in min (e.g. haircut:45): ")
    result = parse_booking(user_input)
    if result is None:
        print("Invalid booking. Use service:minutes, with minutes above 0 and up to 1440.")
    else:
        print("Service and Duration:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter durations as CSV (e.g. 30,45,60): ")
    result = duration_average(user_input)
    if result is None:
        print("Invalid durations. Use whole minutes from 1 to 1440, separated by commas.")
    else:
        print("Average Duration:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 800|100): ")
    result = payable_bill(user_input)
    if result is None:
        print("Invalid bill. Use bill|discount with amounts from 0 to 10000000.")
    else:
        print("Payable Bill:", result)


if __name__ == "__main__":
    main()
