from django.db import models
from django.conf import settings
from django.urls import reverse
from member.models import Member
from datetime import datetime
# Create your models here.
User = settings.AUTH_USER_MODEL

MONTH_CODE_CHOICES = [
    (1, 'JANUARY'),
    (2, 'FEBRUARY'),
    (3, 'MARCH'),
    (4, 'APRIL'),
    (5, 'MAY'),
    (6, 'JUNE'),
    (7, 'JULY'),
    (8, 'AUGUST'),
    (9, 'SEPTEMBER'),
    (10, 'OCTOBER'),
    (11, 'NOVEMBER'),
    (12, 'DECEMBER'),
]


class YearModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'year'


class MonthModel(models.Model):
    name = models.IntegerField(choices=MONTH_CODE_CHOICES)
    year = models.ForeignKey(
        YearModel, on_delete=models.CASCADE, related_name='month')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'month'

    def __str__(self):
        return f"{self.name}"


class WeekModel(models.Model):
    name = models.CharField(max_length=100)
    month = models.ForeignKey(
        MonthModel, on_delete=models.CASCADE, related_name='week')
    year = models.ForeignKey(
        YearModel, on_delete=models.CASCADE, related_name='week', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}|{self.month}|{self.year}"

    class Meta:
        db_table = 'week'


class Share(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='share')
    week = models.ForeignKey(
        WeekModel, on_delete=models.CASCADE, related_name='share')
    month = models.ForeignKey(
        MonthModel, on_delete=models.CASCADE, related_name='share', blank=True, null=True)
    year = models.ForeignKey(
        YearModel, on_delete=models.CASCADE, related_name='share', blank=True, null=True)
    hisa = models.PositiveIntegerField(default=0)
    jamii = models.FloatField(blank=True, null=True, default=0)
    fine = models.FloatField(blank=True, null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'share'

    def amount(self):
        rate = 30000
        return self.hisa*rate

    def fine_amount(self):
        hisa_rate = 10000
        jamii_fine = 10000
        fine = 0.0
        if (self.hisa < 1 and self.jamii < 5000):
            fine = (hisa_rate+jamii_fine)
            return fine
        elif(self.hisa < 1 or self.jamii < 5000):
            fine += jamii_fine
            return fine

    def __str__(self):
        return f"{self.member} | {self.week}| {self.year}"

    def delete(self):
        return reverse('share:delete', kwargs={'id': self.id})


FILE_FORMAT_CHOICES = [
    ('excel', 'Excel Type'),
    ('csv', 'CSV Type')
]


class Fine(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='fines')
    hisa_amount = models.FloatField(blank=True, null=True, default=0)
    jamii_amount = models.FloatField(blank=True, null=True, default=0)
    week = models.ForeignKey(
        WeekModel, on_delete=models.CASCADE, related_name='fines')

    def __str__(self):
        return f"{self.member} | {self.week}"

    @property
    def fine_sum(self):
        return self.hisa_amount+self.jamii_amount


# class ShareFile(models.Model):
#     file_format = models.CharField(max_length=100,choices=FILE_FORMAT_CHOICES)
#     file = models.FileField(upload_to='uploaded')

#     def __str__(self):
#         return f"{self.file}"

#     class Admin:
#         list_display = ['file_format', 'file']
