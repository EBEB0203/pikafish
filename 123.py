from datetime import datetime,timezone,timedelta
dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
dt2 = dt1.astimezone(timezone(timedelta(hours=8))) 
tz = timezone(timedelta(hours=+8))
print( datetime.now(tz))
print( datetime.now())
print(dt1)
print(tz)