# Generated by Django 2.2.3 on 2019-07-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0007_offeredachievement_generic'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]