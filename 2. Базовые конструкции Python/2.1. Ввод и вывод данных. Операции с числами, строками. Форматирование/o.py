from datetime import date, datetime, time, timedelta

h, m, t = [int(input()) for _ in range(3)]

dt = datetime.combine(date.today(), time(hour=h, minute=m)) + timedelta(minutes=t)
print(dt.time().strftime('%H:%M'))
