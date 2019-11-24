# Generated by Django 2.0.7 on 2019-11-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('start', models.TextField()),
                ('end', models.TextField()),
                ('stops', models.TextField()),
                ('date', models.DateField()),
                ('time_dep', models.DateTimeField()),
                ('time_arr', models.DateTimeField()),
                ('car_model', models.TextField()),
                ('car_cap', models.IntegerField()),
                ('cigs', models.BooleanField()),
                ('pets', models.BooleanField()),
                ('price', models.FloatField()),
            ],
        ),
    ]