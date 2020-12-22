from datetime import date, timedelta

x = {}
x['date_today'] = date.today()
x['date_tomorrow'] = date.today() + timedelta(days=1)
print(x)

y = datetime.date(2020, 12, 16)
