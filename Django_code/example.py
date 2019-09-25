# import urllib.request
# print(urllib.request.urlopen("http://www.example.com").read().decode('utf-8'))

# from django.db import models

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)



# import pytz

# for tz in pytz.all_timezones:
#     print(tz)


import datetime
from pytz import timezone, utc

KST = timezone('Asia/Seoul')
now = datetime.datetime.utcnow()

print(utc.localize(now))

print(KST.localize(now))

print(utc.localize(now).astimezone(KST))