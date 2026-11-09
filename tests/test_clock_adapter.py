from datetime import datetime

from clocks import AnalogClock
from adapters.digital_clock_adapter import DigitalClockAdapter
from consts import DayNightDivision


def test_adapter_converts_datetime_to_analog_clock():
    adapter = DigitalClockAdapter(AnalogClock())

    date = datetime(2026, 9, 1, 14, 28, 42)
    adapter.set_date_time(date)

    analog_clock = adapter.analog_clock

    assert analog_clock.get_year() == 2026
    assert analog_clock.get_month() == 9
    assert analog_clock.get_day() == 1

    assert analog_clock.get_day_night_division() == DayNightDivision.PM

    assert analog_clock.get_hour_angle() == 74.35
    assert analog_clock.get_minute_angle() == 172.2
    assert analog_clock.get_second_angle() == 252


def test_adapter_handles_midnight():
    adapter = DigitalClockAdapter(AnalogClock())

    # Проверяем полночь
    midnight = datetime(2026, 9, 1, 0, 0, 0)
    adapter.set_date_time(midnight)

    assert adapter.get_date_time() == midnight
    assert adapter.analog_clock.get_day_night_division() == DayNightDivision.AM


def test_adapter_handles_noon():
    adapter = DigitalClockAdapter(AnalogClock())

    # Проверяем полдень
    noon = datetime(2026, 9, 1, 12, 0, 0)
    adapter.set_date_time(noon)

    assert adapter.get_date_time() == noon
    assert adapter.analog_clock.get_day_night_division() == DayNightDivision.PM
