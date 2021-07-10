# Generated by Django 3.2 on 2021-07-10 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('estd', models.DateField()),
                ('email', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=14)),
                ('website', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('salary_range', models.CharField(max_length=254)),
                ('experience', models.CharField(max_length=100)),
                ('seats_available', models.IntegerField()),
                ('skills_required', models.CharField(max_length=254)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
            ],
        ),
    ]