import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SrikanthFTL.settings')
import django
django.setup()

#fake population Script

import random
import datetime
from myapp.models import User,ActivityPeriod

from faker import Faker
from password_generator import PasswordGenerator

pwo = PasswordGenerator()


fakegen = Faker()
timezones = ['Asia/Kolkata','Asia/Kabul','Africa/Luanda','Antarctica/Mawson','Asia/Yerevan','America/Aruba','Europe/Sarajevo','Pacific/Rarotonga','Europe/Berlin','America/Grenada','Asia/Jakarta']


def add_user():
        fake_name = fakegen.name()
        userid = pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789',8)
        timezone = random.choice(timezones)
        obj = User.objects.get_or_create(user_id=userid,real_name=fake_name,time_zone=timezone)[0]
        return obj

def populate(N=5):
    for entry in range(N):
        user = add_user()
        start = datetime.date(year=2021, month=2, day=18)
        end = datetime.date(year=2021, month=2, day=19)
        start_time = fakegen.date_time_between(start_date=start, end_date=end)
        end_time = fakegen.date_time_between(start_date=start, end_date=end)
        if start_time > end_time:
            start_time, end_time = end_time, start_time
        activity = ActivityPeriod.objects.get_or_create(user=user, start_time=start_time, end_time=end_time)

if __name__ == '__main__':
    print('populating scripts')
    populate(2)
    print('complete')

