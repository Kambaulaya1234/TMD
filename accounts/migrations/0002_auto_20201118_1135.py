# Generated by Django 3.1.3 on 2020-11-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(default='/images/default/profile/logo.png', upload_to='images/users'),
        ),
    ]