# Generated by Django 2.2.6 on 2020-01-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plagiarism', '0002_auto_20200107_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
