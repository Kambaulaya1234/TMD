from django.db import models
from member.models import Member


class Loan(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='loan', blank=True, null=True)
    amount = models.FloatField()
    profit_amount = models.FloatField(blank=True, null=True)
    insurance = models.FloatField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'loans'

    def __str__(self):
        return f"{self.member}"

    def save(self, *args, **kwargs):
        self.insurance = self.amount*.01
        self.profit_amount = self.amount+self.amount*.1
        super().save(*args, **kwargs)
