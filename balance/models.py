from django.db import models


class Balance(models.Model):
    total=models.DecimalField(max_digits=10,decimal_places=1)
    
    def __str__(self):
        return f"{self.total}"
