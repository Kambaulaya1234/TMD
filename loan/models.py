from django.db import models
from member.models import Member
from django.urls import reverse
from django.conf import settings
import random
import string

User = settings.AUTH_USER_MODEL


class Loan(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='loan', blank=True, null=True)
    loan_round= models.ForeignKey(
        'LoanRound', on_delete=models.CASCADE, related_name='loans', blank=True, null=True)
    amount = models.FloatField()
    profit_amount = models.FloatField(blank=True, null=True)
    insurance = models.FloatField(blank=True, null=True)
    paid = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'loans'

    def __str__(self):
        return f"{self.member}"

    def show(self):
        return reverse('loan:show', kwargs={
            'id': self.id
        })

    def remained_amount(self):
        return (self.amount+self.profit_amount)-self.paid

    def delete(self):
        return reverse('loan:delete', kwargs={'id': self.id})

    def payloan(self):
        return reverse('loan:paid', kwargs={'id': self.id})

    @property
    def total(self):
        return self.amount-(self.profit_amount+self.insurance)

    @property
    def return_amount(self):
        return self.amount+self.profit_amount

    def percent(self):
        if self.paid > 0:
            _percent = (self.paid*100)/(self.amount+self.profit_amount)
        else:
            _percent = 0
        return _percent

    def save(self, *args, **kwargs):
        self.insurance = self.amount*.01
        self.profit_amount = self.amount*.1
        super().save(*args, **kwargs)


class Payment(models.Model):
    loan = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='payments')
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    paid = models.DecimalField(max_digits=10, decimal_places=1)
    date = models.DateTimeField()
    by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='payments', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.loan}"

    def reference_code(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

    def delete(self):
        return reverse('loan:delete_payment', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        self.ref_code = self.reference_code().upper()
        super().save(*args, **kwargs)


class LoanRound(models.Model):
    name = models.IntegerField(default=0, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"ROUND {self.name}"
    
    
