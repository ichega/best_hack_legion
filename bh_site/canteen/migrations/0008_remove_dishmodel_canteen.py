# Generated by Django 2.0 on 2019-03-18 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0007_auto_20190318_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishmodel',
            name='canteen',
        ),
    ]
