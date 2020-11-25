from django.core.management.base import BaseCommand, CommandError
from django.core import management
from accounts.models import *
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User, Group, Permission
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Create seed'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    # def success(self, *args, **options):

    def handle(self, *args, **options):
        admin_password='directoratlaz'
        User.objects.all().delete()
        Profile.objects.all().delete()
        management.call_command('flush')
        contexts = [
            {'first_name': 'Conic', 'last_name': 'Bunih', 'username': 'conic', 'email': 'cbunih@gmail.com', 'password': 'abgoogle',
             'is_superuser': True, 'is_staff': True, 'date_joined': f'{ timezone.now() }'},

            # ============================================Normal Account====================================================

            {'first_name': 'Cuthbert', 'last_name': 'Cornel', 'username': 'admin', 'email': 'atlaz.director@gmail.com', 'password': f'{admin_password}',
             'is_superuser': True, 'date_joined': f'{ timezone.now() }'},
        ]

        self.stdout.write(self.style.SUCCESS('\n'))
        self.stdout.write(self.style.SUCCESS('\t LIST OF SEEDED USERs'))
        self.stdout.write(self.style.SUCCESS('\n'))

        for context in contexts:
            try:
                user = User.objects.create_user(**context)
                profile = Profile.objects.create(
                    user=user, phone='', location='')
                self.stdout.write(self.style.SUCCESS(
                    f'| ------>user {user.username } seeded  successfully! '))
                if user.username == 'admin':
                    self.stdout.write(self.style.SUCCESS(
                        f"| ------>user {user.username } passcode: '{admin_password}'' seeded  successfully! "))
                # self.stdout.write(self.style.SUCCESS(f'| ------>profile for {profile.user } created successfully! ' ))
            except User.DoesNotExist:
                raise CommandError('Error creating User')
        if user.username == 'admin':
            Group.objects.all().delete()
            groupAdministrator = Group.objects.create(name='administrator')
            perms = Permission.objects.all()
            groupAdministrator.permissions.set(perms)
            user.groups.add(groupAdministrator)

        self.stdout.write(self.style.SUCCESS('\n'))
        self.stdout.write(self.style.SUCCESS(
            '---------------------------------------------'))
        self.stdout.write(self.style.SUCCESS(
            f'Congrats! {len(contexts)} Default Users seeded Successfully!'))
        self.stdout.write(self.style.SUCCESS(
            '---------------------------------------------'))
