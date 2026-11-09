from datetime import datetime

from clocks import AnalogClock
from adapters.digital_clock_adapter import DigitalClockAdapter
from facades.clock_facade import ClockFacade
from services.clock_formatter import ClockFormatter
from services.clock_history import ClockHistory


def create_facade():
    analog_clock = AnalogClock()
    adapter = DigitalClockAdapter(analog_clock)

    formatter = ClockFormatter()
    history = ClockHistory()

    return ClockFacade(adapter, formatter, history)


def test_facade_sets_and_gets_date_time():
    clock = create_facade()

    date = datetime(2026, 9, 1, 14, 28, 42)
    clock.set_date_time(date)

    assert clock.get_date_time() == date


def test_facade_formats_date_time():
    clock = create_facade()

    date = datetime(2026, 9, 1, 14, 28, 42)
    clock.set_date_time(date)

    assert clock.get_formatted_time() == "01.09.2026 14:28:42"


def test_facade_custom_format():
    clock = create_facade()

    date = datetime(2026, 9, 1, 14, 28, 42)
    clock.set_date_time(date)

    assert clock.get_formatted_time("%H:%M") == "14:28"


def test_facade_history():
    clock = create_facade()

    first_date = datetime(2026, 9, 1, 14, 28, 42)
    second_date = datetime(2026, 9, 1, 14, 29, 42)
    third_date = datetime(2026, 9, 1, 14, 30, 42)

    clock.set_date_time(first_date)
    clock.set_date_time(second_date)
    clock.set_date_time(third_date)

    assert clock.get_history() == (
        first_date,
        second_date,
        third_date
    )


def test_facade_empty_history():
    clock = create_facade()

    assert clock.get_history() == ()
