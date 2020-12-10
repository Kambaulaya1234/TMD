# Generated by Django 3.1.3 on 2020-12-05 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='loan.loan'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='ref_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]