# Generated by Django 3.0.4 on 2020-05-12 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Capitalcity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=100)),
                ('State', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WebApp.State')),
            ],
        ),
    ]
