from datetime import datetime

from facades.clock_facade import ClockFacade

clock = ClockFacade()

clock.set_date_time(datetime(2026, 9, 1, 12, 18, 26))

print("Какая-то дата и время:")
print(clock.get_date_time())

print("\nФорматированное время:")
print(clock.get_formatted_time())

print("\nИстория изменений:")
for date in clock.get_history():
    print(date)
