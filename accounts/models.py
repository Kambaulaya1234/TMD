from django.db import models
from django.contrib.auth.models import User
from member.models import Member


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=10, default='Active')
    phone = models.CharField(max_length=10, blank=True, null=True)
    is_member = models.BooleanField(default=False)
    location = models.CharField(max_length=100, blank=True, null=True)
    ref_number = models.CharField(max_length=100, blank=True, null=True)
    sirname = models.CharField(max_length=100, blank=True, null=True)
    profile = models.ImageField(
        upload_to="images/users", default='/images/default/profile/logo.png')

    def __str__(self):
        return f'{self.user}'


class Credential(models.Model):
    member = models.OneToOneField(
        Member, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.member}'
