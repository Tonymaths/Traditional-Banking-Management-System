# Generated by Django 2.0.7 on 2018-08-12 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact_no',
            field=models.IntegerField(default='0', unique=True),
        ),
    ]