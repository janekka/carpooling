# Generated by Django 2.0.7 on 2019-11-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('start', models.TextField()),
                ('end', models.TextField()),
                ('distance', models.FloatField()),
                ('date', models.DateField()),
                ('time_dep', models.DateTimeField()),
                ('time_arr', models.DateTimeField()),
                ('cigs', models.BooleanField()),
                ('pets', models.BooleanField()),
                ('max_cost', models.FloatField()),
            ],
        ),
    ]
