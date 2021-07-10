# Generated by Django 3.2.4 on 2021-07-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('image', models.ImageField(upload_to='user/images/')),
                ('skills', models.CharField(max_length=254)),
            ],
        ),
    ]