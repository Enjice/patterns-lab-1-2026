# Диаграмма


classDiagram
class BaseDigitalClock {
<<interface>>
+set_date_time(date)
+get_date_time()
}

    class BaseAnalogClock {
        <<interface>>
        +set_date_time(year, month, day, hour_angle, minute_angle, second_angle, day_night_division)
        +get_hour_angle()
        +get_minute_angle()
        +get_second_angle()
        +get_year()
        +get_month()
        +get_day()
        +get_day_night_division()
    }

    class AnalogClock {
        +set_date_time(...)
        +get_hour_angle()
        +get_minute_angle()
        +get_second_angle()
        +get_year()
        +get_month()
        +get_day()
        +get_day_night_division()
    }

    class DigitalClockAdapter {
        -analog_clock
        +set_date_time(date)
        +get_date_time()
    }

    class ClockFacade {
        -clock
        -formatter
        -history
        +set_date_time(date)
        +get_date_time()
        +get_formatted_time(fmt)
        +get_history()
    }

    class ClockFormatter {
        +format(value, fmt)
    }

    class ClockHistory {
        -items
        +add(value)
        +all()
    }

    class DigitalClockDisplay {
        -clock
        +render()
    }

    BaseAnalogClock <|.. AnalogClock
    BaseDigitalClock <|.. DigitalClockAdapter

    DigitalClockAdapter *-- AnalogClock

    ClockFacade --> DigitalClockAdapter
    ClockFacade --> ClockFormatter
    ClockFacade --> ClockHistory

    DigitalClockDisplay --> BaseDigitalClock
