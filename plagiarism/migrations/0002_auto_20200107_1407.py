# Generated by Django 2.2.6 on 2020-01-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plagiarism', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user2',
            name='user_type',
            field=models.CharField(default='null', max_length=100, null=True),
        ),
    ]