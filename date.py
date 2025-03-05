#Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print(new_date.strftime("%Y-%m-%d"))

#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#Write a Python program to drop microseconds from datetime.

from datetime import datetime

current_datetime = datetime.now()

print("Current datetime:", current_datetime)

#Write a Python program to calculate two date difference in seconds.

from datetime import datetime

date1 = datetime(2025, 7, 1)
date2 = datetime(2025, 9, 24)

difference = date2 - date1
difference_in_seconds = difference.total_seconds()

print("Difference in seconds:", difference_in_seconds)