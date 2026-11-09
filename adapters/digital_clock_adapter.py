from datetime import datetime

from interfaces import BaseDigitalClock, BaseAnalogClock
from consts import DayNightDivision


class DigitalClockAdapter(BaseDigitalClock):
    def __init__(self, analog_clock: BaseAnalogClock):
        self.analog_clock = analog_clock

    def set_date_time(self, date: datetime) -> None:
        year = date.year
        month = date.month
        day = date.day

        hour = date.hour % 12
        minute = date.minute
        second = date.second

        if date.hour < 12:
            day_night = DayNightDivision.AM
        else:
            day_night = DayNightDivision.PM

        hour_angle = 30 * hour + 0.5 * minute + second / 120
        minute_angle = 6 * minute + 0.1 * second
        second_angle = 6 * second

        self.analog_clock.set_date_time(
            year,
            month,
            day,
            hour_angle,
            minute_angle,
            second_angle,
            day_night
        )

    def get_date_time(self) -> datetime:
        year = self.analog_clock.get_year()
        month = self.analog_clock.get_month()
        day = self.analog_clock.get_day()

        hour_angle = self.analog_clock.get_hour_angle()
        minute_angle = self.analog_clock.get_minute_angle()
        second_angle = self.analog_clock.get_second_angle()

        day_night = self.analog_clock.get_day_night_division()

        hour = int(hour_angle // 30)
        minute = int(minute_angle // 6)
        second = int(second_angle // 6)

        if day_night == DayNightDivision.PM:
            hour += 12

        return datetime(year, month, day, hour, minute, second)
