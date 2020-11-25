# Generated by Django 3.1.3 on 2020-11-15 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('status', models.CharField(default='Active', max_length=10)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('profile', models.ImageField(default='/static/profile/logo.png', upload_to='images/users')),
            ],
        ),
    ]
