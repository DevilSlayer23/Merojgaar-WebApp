# Generated by Django 3.2 on 2021-07-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_auto_20210710_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Half Time', 'Half Time'), ('Temporary', 'Temporary'), ('Permanent', 'Permanent')], default='Full Time', max_length=100),
        ),
    ]
