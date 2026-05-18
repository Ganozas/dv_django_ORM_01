import os

import django

from django.db import models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    passcards =  Passcard.objects.all()
    some_passcard = passcards[0]
    active_passcards = Passcard.objects.filter(is_active=True).count()
   
    print('Активных пропусков:', active_passcards)
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
