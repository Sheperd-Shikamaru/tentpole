# Generated by Django 5.0.6 on 2024-05-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_insight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetinsight',
            name='month',
            field=models.CharField(max_length=20, null=True),
        ),
    ]