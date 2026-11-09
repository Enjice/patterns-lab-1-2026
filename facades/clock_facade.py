from datetime import datetime

from interfaces import BaseDigitalClock
from services.clock_formatter import ClockFormatter
from services.clock_history import ClockHistory


class ClockFacade:
    def __init__(
            self,
            clock: BaseDigitalClock,
            formatter: ClockFormatter,
            history: ClockHistory
    ):
        self.clock = clock
        self.formatter = formatter
        self.history = history

    def set_date_time(self, date: datetime) -> None:
        self.clock.set_date_time(date)
        self.history.add(date)

    def get_date_time(self) -> datetime:
        return self.clock.get_date_time()

    def get_formatted_time(self, fmt: str = "%d.%m.%Y %H:%M:%S") -> str:
        date = self.get_date_time()
        return self.formatter.format(date, fmt)

    def get_history(self) -> tuple[datetime, ...]:
        return self.history.all()
