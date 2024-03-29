from django.db import models
from django.urls import reverse
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Member(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='member', unique=True)
    is_member = models.BooleanField(default=False)
    has_fine = models.BooleanField(default=False, blank=True, null=True)
    fine_count= models.IntegerField(default=0, blank=True, null=True)
    sponsored_by=models.OneToOneField(
       User, on_delete=models.CASCADE, related_name='sponsor',blank=True, null=True)
    is_member = models.BooleanField(default=False)

    class Meta:
        db_table = 'members'
        ordering = ['id']

    def __str__(self):
        return f'{self.user.username} | {self.user.get_full_name() }'

    def edit(self):
        return reverse('member:edit', kwargs={'id': self.id})

    def delete(self):
        return reverse('member:delete', kwargs={'id': self.id})

    def activate(self):
        return reverse('member:activate', kwargs={'id': self.id})

    def payloan(self):
        return reverse('member:payloan', kwargs={'id': self.id})

    def get_profile(self):
        return reverse('member:profile', kwargs={'id': self.id})


# class Member(models.Model):
#     firstname = models.CharField(max_length=255, blank=True, null=True)
#     lastname = models.CharField(max_length=255, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     username = models.CharField(max_length=255, unique=True)
#     profile = models.ImageField(
#         upload_to="images/users", default='/images/default/profile/logo.png')
#     is_active = models.BooleanField(default=False)

#     class Meta:
#         db_table = 'members'

#     def __str__(self):
#         return f'{self.username}'

#     def delete(self):
#         return reverse('member:delete', kwargs={'id': self.id})
