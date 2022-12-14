import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    before_balance = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    available_balance = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    payday = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.user.username

    @property
    def days_til_next_payday(self):
        return (self.payday - datetime.date.today()).days
